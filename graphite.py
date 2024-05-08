import sys
import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import math
import platform
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtCore import QDir,Qt, QPointF
from PySide6.QtWidgets import  QApplication, QMainWindow, QMessageBox, QFileDialog, QFileSystemModel, QAbstractItemView, QDialog,QInputDialog, QLineEdit,QVBoxLayout,QTableWidgetItem,QHeaderView,QAbstractScrollArea
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from ui_form import Ui_Graphite
from ui_customize_dialog import Ui_Dialog as custom
from ui_export import Ui_Dialog as export
from ui_worksheet_dialog import Ui_Dialog2 as worksheet
from ui_math_function import Ui_Dialog as function
from ui_interpolation import Ui_Dialog as interpolation
from graphs import Tab


class Worksheet(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = worksheet()
        self.ui.setupUi(self)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.ui.tableWidget.horizontalHeader().setMinimumSectionSize(100)
        self.ui.addwork.clicked.connect(self.add_row)
        self.ui.addwork_2.clicked.connect(self.add_column)
        self.ui.remrow.clicked.connect(self.remove_row)
        self.ui.remcol.clicked.connect(self.remove_column)

    def remove_row(self):
        selected_ranges = self.ui.tableWidget.selectedRanges()
        if selected_ranges:
            for selected_range in selected_ranges:
                for row in range(selected_range.topRow(), selected_range.bottomRow() + 1):
                    if 0 <= row < self.ui.tableWidget.rowCount():
                        self.ui.tableWidget.removeRow(row)
        else:
            row, ok = QInputDialog.getInt(self, "Remove Row", "Enter row number to remove:")
            if ok:
                row_index = row - 1
                if 0 <= row_index < self.ui.tableWidget.rowCount():
                    self.ui.tableWidget.removeRow(row_index)

    def remove_column(self):
        selected_ranges = self.ui.tableWidget.selectedRanges()
        if selected_ranges:
            for selected_range in selected_ranges:
                for column in range(selected_range.leftColumn(), selected_range.rightColumn() + 1):
                    if 0 <= column < self.ui.tableWidget.columnCount():
                        self.ui.tableWidget.removeColumn(column)
        else:
            column, ok = QInputDialog.getInt(self, "Remove Column", "Enter column number to remove:")
            if ok:
                column_index = column - 1
                if 0 <= column_index < self.ui.tableWidget.columnCount():
                    self.ui.tableWidget.removeColumn(column_index)

    def add_row(self):
        row_count = self.ui.tableWidget.rowCount()
        self.ui.tableWidget.setRowCount(row_count + 1)

    def add_column(self):
        column_count = self.ui.tableWidget.columnCount()
        self.ui.tableWidget.setColumnCount(column_count + 1)


class CustomizeDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = custom()
        self.ui.setupUi(self)
        self.ui.cancel_btn.clicked.connect(self.cancel)

    def cancel(self):
        reply = QMessageBox.question(self, 'Cancel', 'Are you sure you want to cancel?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()


class FunctionDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = function()
        self.ui.setupUi(self)
        self.ui.cancel.clicked.connect(self.cancel)

    def cancel(self):
        reply = QMessageBox.question(self, 'Cancel', 'Are you sure you want to cancel?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()

class ExportDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = export()
        self.ui.setupUi(self)
        self.ui.file.clicked.connect(self.setFile)
        self.ui.cancel.clicked.connect(self.cancel)

    def setFile(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", options=options)
        self.ui.location.setText(folder_path)

    def cancel(self):
        reply = QMessageBox.question(self, 'Cancel', 'Are you sure you want to cancel?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.reject()

class InterpolationDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = interpolation()
        self.ui.setupUi(self)
        self.name = ''
        self.coordinates = []
        self.points = []
        self.figure, self.ax = plt.subplots()
        self.ax.set_position([0, 0, 1, 1])
        self.ax.axis('off')
        self.plot_widget = FigureCanvasQTAgg(self.figure)
        self.ui.image.addWidget(self.plot_widget)

        self.figure.canvas.mpl_connect('button_press_event', self.onclick)
        self.delete_shortcut = QShortcut(QKeySequence(Qt.Key_Backspace), self)
        self.delete_shortcut.activated.connect(self.delete_last_point)

        self.ui.cancel.clicked.connect(self.cancel)

    def onclick(self, event):
        if event.inaxes == self.ax:
            x, y = event.xdata, event.ydata
            self.coordinates.append((x, y))
            point, = self.ax.plot(x, y, 'rx') 
            self.points.append(point)
            self.plot_widget.draw()

    def delete_last_point(self):
        if self.points:
            self.points[-1].remove()
            self.points.pop()
            self.coordinates.pop()
            print(self.coordinates)
            self.plot_widget.draw()

    def delete_all_points(self):
        while self.points:
            self.points[-1].remove()
            self.points.pop()
            self.coordinates.pop()


    def cancel(self):
        reply = QMessageBox.question(self, 'Cancel', 'Are you sure you want to cancel?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.close()

class Graphite(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Graphite()
        self.ui.setupUi(self)
        self.ui.graphTab.tabCloseRequested.connect(self.close_tab)
        self.full_screen = False
        shortcut = QShortcut(QKeySequence("Alt+d"), self.ui.graphTab)
        shortcut.activated.connect(self.close_current_tab)


        self.tabs = []

        #menu functions
        self.ui.open_file.triggered.connect(self.open_file_dialog)
        self.ui.open_folder.triggered.connect(self.open_folder_dialog)
        self.ui.save.triggered.connect(self.save)
        self.ui.save_as.triggered.connect(self.saveAs)
        self.ui.exit_app.triggered.connect(self.exit_app)

        #tree functions
        self.ui.treeView.setDragEnabled(True)
        self.ui.treeView.setAcceptDrops(True)
        self.ui.treeView.setDropIndicatorShown(True)
        
        self.ui.treeView.setDragDropMode(QAbstractItemView.InternalMove)

        self.ui.treeView.dragEnterEvent = self.dragEnterEvent
        self.ui.treeView.dragMoveEvent = self.dragMoveEvent
        self.ui.treeView.dropEvent = self.dropEvent
        
        self.ui.treeView.doubleClicked.connect(self.treeFileIndex)



        self.ui.MathMode.triggered.connect(lambda: self.ui.mode_frames.setCurrentIndex(0))
        self.ui.BchimieMode.triggered.connect(lambda: self.ui.mode_frames.setCurrentIndex(2))
        self.ui.actionfilters.triggered.connect(lambda: self.ui.mode_frames.setCurrentIndex(3))

        self.ui.min_max.clicked.connect(self.get_min_max_values)
        self.ui.Polynome.clicked.connect(self.perform_polynomial_fit)
        self.ui.linear.clicked.connect(self.perform_linear_fit)
        self.ui.quadraple.clicked.connect(self.perform_quadratic_fit)
        self.ui.cubic.clicked.connect(self.perform_cubic_fit)
        self.ui.expo_2.currentIndexChanged.connect(self.handle_fit_type_changed_expo)
        self.ui.power.clicked.connect(self.perform_power_fit)
        self.ui.log.currentIndexChanged.connect(self.handle_fit_type_changed_log)
        self.ui.gauss.currentIndexChanged.connect(self.handle_fit_type_changed_gauss)
        self.ui.weibull.currentIndexChanged.connect(self.handle_fit_type_changed_w)
        self.ui.fourier.currentIndexChanged.connect(self.handle_fit_type_changed_f)
        self.ui.spline.currentIndexChanged.connect(self.handle_fit_type_changed_s)

        self.ui.median.clicked.connect(self.apply_median_filter)
        self.ui.lowess.clicked.connect(self.apply_lowess_filter)
        self.ui.exponon.clicked.connect(self.apply_exponential_filter)
        self.ui.move.clicked.connect(self.apply_moving_average_filter)
        self.ui.savi.clicked.connect(self.apply_savitzky_golay_filter)
        self.ui.butter.clicked.connect(self.apply_butterworth_filter)
        self.ui.sheb.clicked.connect(self.apply_chebyshev_filter)
        self.ui.gaus.clicked.connect(self.apply_gaussian_filter)
        self.ui.boxcar.clicked.connect(self.apply_boxcar_filter)
        self.ui.kalman.clicked.connect(self.apply_kalman_filter)
        # self.ui.notch.clicked.connect(self.apply_notch_filter)
        self.ui.passe.currentIndexChanged.connect(self.handle_fit_type_changed_pass)




        #types
        self.ui.plot.clicked.connect(self.toPlot)
        self.ui.piechart.clicked.connect(self.toPiechart)
        self.ui.histogram.clicked.connect(self.toBar)
        self.ui.fill_between.clicked.connect(self.toFill)
        self.ui.stackplot.clicked.connect(self.toStack)

        #buttons

        self.ui.open_btn.clicked.connect(self.open_file_dialog)
        self.ui.save_btn.clicked.connect(self.save)
        self.ui.export_btn.clicked.connect(self.show_export_dialog)

        self.ui.focus.clicked.connect(self.focus)
        self.ui.focus_2.clicked.connect(self.focus)
        self.ui.fullscreen.clicked.connect(self.graph_full_screen)
        self.ui.backM.clicked.connect(self.graph_normal_screen)

        self.customize_dialog = CustomizeDialog(self)
        self.customize_dialog.ui.apply_btn.clicked.connect(self.apply_custom)
        self.ui.custom_button.clicked.connect(self.show_customize_dialog)

        self.export_dialog = ExportDialog(self)
        self.export_dialog.ui.expo.clicked.connect(self.export)
        self.ui.expo.triggered.connect(self.show_export_dialog)

        self.worksheet_dialog = Worksheet(self)
        self.worksheet_dialog.ui.plotwork.clicked.connect(self.plotwork)
        self.ui.worksheet.clicked.connect(self.show_worksheet)

        self.interpolation_dialog = InterpolationDialog(self)
        self.interpolation_dialog.ui.plot.clicked.connect(self.interpolate)

        self.function_dialog = FunctionDialog(self)
        self.function_dialog.ui.plot_btn.clicked.connect(self.fx)
        self.ui.actionfx.triggered.connect(self.show_function_dialog)





    def plotwork(self):
        table_widget = self.worksheet_dialog.ui.tableWidget

        selected_ranges = table_widget.selectedRanges()
        if selected_ranges:
            selected_range = selected_ranges[0]
            start_row = selected_range.topRow()
            end_row = selected_range.bottomRow()
            start_column = selected_range.leftColumn()
            end_column = selected_range.rightColumn()

            data = []
            headers = []
            for column in range(start_column, end_column + 1):
                header_item = table_widget.horizontalHeaderItem(column)
                if header_item is not None:
                    headers.append(header_item.text())
                else:
                    headers.append("test")
            for row in range(start_row, end_row + 1):
                row_data = []
                for column in range(start_column, end_column + 1):
                    item = table_widget.item(row, column)
                    if item is not None:
                        row_data.append(float(item.text()))
                    else:
                        row_data.append(np.nan)  # Handle empty cells
                data.append(row_data)

            df = pd.DataFrame(data, columns=headers)

            self.tabs.append(Tab(self.ui.graphTab, df, name="Selected Data", file=None))
        else:
            num_rows = table_widget.rowCount()
            num_cols = table_widget.columnCount()
            data = []
            for row in range(num_rows):
                row_data = []
                for col in range(num_cols):
                    item = table_widget.item(row, col)
                    if item is not None:
                        row_data.append(float(item.text()))
                    else:
                        row_data.append(np.nan)  # Handle empty cells
                data.append(row_data)

            df = pd.DataFrame(data)
            self.tabs.append(Tab(self.ui.graphTab, df, name="Worksheet", file=None))




    def apply_chebyshev_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            Wn, ok1 = QInputDialog.getDouble(self, "Chebyshev Filter", "Enter the critical frequency (0-1):", value=0.5, decimals=2)
            rp, ok2 = QInputDialog.getDouble(self, "Chebyshev Filter", "Enter the passband ripple (dB):", value=1.0)
            rs, ok3 = QInputDialog.getDouble(self, "Chebyshev Filter", "Enter the stopband attenuation (dB):", value=20.0)

            if ok1 and ok2 and ok3:
                Wn /= 2.0
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                filtered_data = tab.apply_chebyshev_filter(tab.dataframe, Wn, rp, rs)
                filtered_data_trimmed = filtered_data[:, :-1]
                filtered_dataframe = pd.DataFrame(filtered_data_trimmed, columns=tab.dataframe.columns[1:], index=tab.dataframe.index)
                tab.plot_filtered_data(filtered_dataframe)


    def apply_median_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            kernel_size, ok = QInputDialog.getInt(self, "Median Filter", "Enter kernel size:", value=3)
            if ok:
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                filtered_data = tab.median_filter(tab.dataframe.iloc[:, 1:], kernel_size)
                tab.plot_filtered_data(pd.DataFrame(filtered_data, columns=tab.dataframe.columns[1:], index=tab.dataframe.index))


    def apply_lowess_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            frac, ok = QInputDialog.getDouble(self, "LOWESS Filter", "Enter smoothing fraction (0-1):", value=0.5, decimals=2)
            if ok:
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                x_data = tab.dataframe.index.values
                y_data = tab.dataframe.iloc[:, 1].values
                filtered_data = tab.lowess_filter(x_data, y_data, frac)
                tab.plot_filtered_data(pd.DataFrame(filtered_data, columns=[tab.dataframe.columns[1]], index=tab.dataframe.index))


    def apply_exponential_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            alpha, ok = QInputDialog.getDouble(self, "Exponential Filter", "Enter alpha value (0-1):", value=0.1, minValue=0.01, maxValue=0.99, decimals=2)
            if ok:
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                filtered_data = np.apply_along_axis(tab.exponential_filter, 0, tab.dataframe.iloc[:, 1:], alpha=alpha)
                tab.plot_filtered_data(pd.DataFrame(filtered_data, columns=tab.dataframe.columns[1:], index=tab.dataframe.index))

    def apply_butterworth_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            cutoff, ok = QInputDialog.getDouble(self, "Butterworth Filter", "Enter cutoff frequency:", value=0.1, decimals=2)
            if ok:
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                data = tab.dataframe.iloc[:, 1].values
                try:
                    filtered_data = tab.butterworth_filter(data, cutoff, fs=1, btype='lowpass', order=4)
                    filtered_dataframe = pd.DataFrame(filtered_data, columns=tab.dataframe.columns[1:], index=tab.dataframe.index)
                    tab.plot_filtered_data(filtered_dataframe)
                except ValueError as e:
                    print(e)

    def apply_moving_average_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            window_size, ok = QInputDialog.getInt(self, "Moving Average Filter", "Enter window size:", value=3, minValue=1)
            if ok:
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                filtered_data = np.convolve(tab.dataframe.iloc[:, 1].values, np.ones(window_size)/window_size, mode='valid')
                filtered_data = np.concatenate(([np.nan] * (window_size - 1), filtered_data))
                filtered_data = np.concatenate((filtered_data, [np.nan] * (len(tab.dataframe) - len(filtered_data))))
                tab.plot_filtered_data(pd.DataFrame(filtered_data, columns=[tab.dataframe.columns[1]], index=tab.dataframe.index))

    def apply_gaussian_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            sigma, ok = QInputDialog.getDouble(self, "Gaussian Filter", "Enter the standard deviation:", value=1.0)
            if ok:
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                data = tab.dataframe.iloc[:, 1:].values.flatten()
                filtered_data = tab.apply_gaussian_filter(data, sigma)
                filtered_data = filtered_data.reshape(-1, tab.dataframe.shape[1] - 1)
                filtered_dataframe = pd.DataFrame(filtered_data, columns=tab.dataframe.columns[1:], index=tab.dataframe.index)
                tab.plot_filtered_data(filtered_dataframe)

    def apply_boxcar_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            window_size, ok = QInputDialog.getInt(self, "Boxcar Filter", "Enter window size:", value=3)
            if ok:
                if window_size < 1:
                    window_size = 1
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                data = tab.dataframe.iloc[:, 1:].values
                filtered_data = tab.apply_boxcar_filter(data, window_size)
                filtered_dataframe = pd.DataFrame(filtered_data, columns=tab.dataframe.columns[1:], index=tab.dataframe.index)
                tab.plot_filtered_data(filtered_dataframe)

    def apply_kalman_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            process_noise, ok1 = QInputDialog.getDouble(self, "Kalman Filter", "Enter process noise:", value=0.01, decimals=3)
            measurement_noise, ok2 = QInputDialog.getDouble(self, "Kalman Filter", "Enter measurement noise:", value=0.01, decimals=3)
            if ok1 and ok2:
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                filtered_data = tab.apply_kalman_filter(tab.dataframe, process_noise, measurement_noise)
                tab.plot_filtered_data(pd.DataFrame(filtered_data, columns=tab.dataframe.columns[1:], index=tab.dataframe.index))

    # def apply_notch_filter(self):
    #    current_index = self.ui.graphTab.currentIndex()
     #   if current_index != -1:
      #      Q, ok1 = QInputDialog.getDouble(self, "Notch Filter", "Enter the Q factor:", value=10.0, decimals=1)
       #     freq, ok2 = QInputDialog.getDouble(self, "Notch Filter", "Enter the frequency to be filtered:", value=0.0)
        #    if ok1 and ok2:
         #       widget = self.ui.graphTab.widget(current_index)
          #      tab_index = self.tabs.index(widget)
           #     tab = self.tabs[tab_index]
            #    filtered_data = tab.apply_notch_filter(tab.dataframe, Q, freq)
             #   tab.plot_filtered_data(filtered_data)

    def apply_savitzky_golay_filter(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            window_length, ok1 = QInputDialog.getInt(self, "Savitzky-Golay Filter", "Enter window length:", value=5, minValue=3)
            polyorder, ok2 = QInputDialog.getInt(self, "Savitzky-Golay Filter", "Enter polynomial order:", value=2, minValue=0)
            if ok1 and ok2:
                widget = self.ui.graphTab.widget(current_index)
                tab_index = self.tabs.index(widget)
                tab = self.tabs[tab_index]
                filtered_data = tab.savitzky_golay_filter(tab.dataframe.iloc[:, 1].values, window_length, polyorder)
                padding_length = len(tab.dataframe) - len(filtered_data)
                if padding_length > 0:
                    filtered_data = np.concatenate((filtered_data, [np.nan] * padding_length))
                elif padding_length < 0:
                    filtered_data = filtered_data[:padding_length]

                tab.plot_filtered_data(pd.DataFrame(filtered_data, columns=[tab.dataframe.columns[1]], index=tab.dataframe.index))


    def perform_polynomial_fit(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            degree, ok = QInputDialog.getInt(self, 'Degree of Polynomial', 'Enter the degree of the polynomial:')
            if ok:
               widget = self.ui.graphTab.widget(current_index)
               tab_index = self.tabs.index(widget)
               tab = self.tabs[tab_index]

               x_data = tab.dataframe.iloc[:, 0].values
               y_data = tab.dataframe.iloc[:, 1].values

               tab.plot_polynomial_curve(x_data, y_data, degree)

    def perform_quadratic_fit(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]

            x_data = tab.dataframe.iloc[:, 0].values
            y_data = tab.dataframe.iloc[:, 1].values
            tab.plot_quadratic_fit(x_data, y_data)

    def handle_fit_type_changed_expo(self, index):
        selected_fit = self.ui.expo_2.itemText(index)

        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            x_data= tab.dataframe.iloc[:, 0].values
            y_data= tab.dataframe.iloc[:, 1].values
            if selected_fit == "expononcial":
                tab.plot_exponential_fit(x_data, y_data)
            elif selected_fit == "double expononcial":
                tab.plot_double_exponential_fit(x_data, y_data)
            elif selected_fit == "triple expononcial":
                tab.plot_triple_exponential_fit(x_data, y_data)
            else:
                print("Unsupported fit type selected")

    def handle_fit_type_changed_pass(self, index):
        selected_fit = self.ui.passe.itemText(index)

        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            if selected_fit == "Lowpass":
                cutoff, ok1 = QInputDialog.getDouble(self, "Lowpass Filter", "Enter the cutoff frequency:", value=0.5)
                fs, ok2 = QInputDialog.getDouble(self, "Lowpass Filter", "Enter the sampling frequency:", value=100.0)
                order, ok3 = QInputDialog.getInt(self, "Lowpass Filter", "Enter the filter order:", value=3)
                if ok1 and ok2 and ok3:
                    widget = self.ui.graphTab.widget(current_index)
                    tab_index = self.tabs.index(widget)
                    tab = self.tabs[tab_index]
                    filtered_data = tab.apply_lowpass_filter(tab.dataframe, cutoff, fs, order)
                    tab.plot_filtered_data(filtered_data)
            elif selected_fit == "Bandpass":
                lowcut, ok1 = QInputDialog.getDouble(self, "Bandpass Filter", "Enter the lowcut frequency:", value=0.1)
                highcut, ok2 = QInputDialog.getDouble(self, "Bandpass Filter", "Enter the highcut frequency:", value=0.9)
                fs, ok3 = QInputDialog.getDouble(self, "Bandpass Filter", "Enter the sampling frequency:", value=100.0)
                order, ok4 = QInputDialog.getInt(self, "Bandpass Filter", "Enter the filter order:", value=3)
                if ok1 and ok2 and ok3 and ok4:
                    widget = self.ui.graphTab.widget(current_index)
                    tab_index = self.tabs.index(widget)
                    tab = self.tabs[tab_index]
                    filtered_data = tab.apply_bandpass_filter(tab.dataframe, lowcut, highcut, fs, order)
                    tab.plot_filtered_data(filtered_data)
            elif selected_fit == "Hipass":
                cutoff, ok1 = QInputDialog.getDouble(self, "Highpass Filter", "Enter the cutoff frequency:", value=0.1)
                fs, ok2 = QInputDialog.getDouble(self, "Highpass Filter", "Enter the sampling frequency:", value=100.0)
                order, ok3 = QInputDialog.getInt(self, "Highpass Filter", "Enter the filter order:", value=3)
                if ok1 and ok2 and ok3:
                    widget = self.ui.graphTab.widget(current_index)
                    tab_index = self.tabs.index(widget)
                    tab = self.tabs[tab_index]
                    filtered_data = tab.apply_highpass_filter(tab.dataframe, cutoff, fs, order)
                    tab.plot_filtered_data(filtered_data)
            else:
                print("Unsupported fit type selected")

    def handle_fit_type_changed_w(self, index):
        selected_fit = self.ui.weibull.itemText(index)

        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            x_data= tab.dataframe.iloc[:, 0].values
            y_data= tab.dataframe.iloc[:, 1].values
            if selected_fit == "weibull":
                tab.plot_weibull_fit(x_data, y_data)
            elif selected_fit == "segmoidal":
                tab.plot_sigmoidal_fit(x_data, y_data)
            elif selected_fit == "meichaelis-menten":
                tab.plot_michaelis_menten_fit(x_data, y_data)
            elif selected_fit == "hill":
                tab.plot_hill_fit(x_data, y_data)
            elif selected_fit == "gompertz":
                tab.plot_gompertz_fit(x_data, y_data)
            else:
                print("Unsupported fit type selected")


    def handle_fit_type_changed_f(self, index):
        selected_fit = self.ui.fourier.itemText(index)

        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            x_data= tab.dataframe.iloc[:, 0].values
            y_data= tab.dataframe.iloc[:, 1].values
            if selected_fit == "fourier":
                tab.plot_fourier_fit(x_data, y_data)
            elif selected_fit == "sine":
                tab.plot_sine_fit(x_data, y_data)
            elif selected_fit == "cosine":
                tab.plot_cosine_fit(x_data, y_data)
            else:
                print("Unsupported fit type selected")

    def handle_fit_type_changed_s(self, index):
        selected_fit = self.ui.spline.itemText(index)

        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            x_data= tab.dataframe.iloc[:, 0].values
            y_data= tab.dataframe.iloc[:, 1].values
            if selected_fit == "spline":
                tab.plot_spline_fit(x_data, y_data)
            elif selected_fit == "lowess":
                tab.plot_lowess_fit(x_data, y_data)
            elif selected_fit == "Savitzky-Golay ":
                tab.plot_savitzky_golay_fit(x_data, y_data)
            else:
                print("Unsupported fit type selected")

    def handle_fit_type_changed_log(self, index):
        selected_fit = self.ui.log.itemText(index)

        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            x_data= tab.dataframe.iloc[:, 0].values
            y_data= tab.dataframe.iloc[:, 1].values
            if selected_fit == "logarithm":
                tab.plot_logarithmic_fit(x_data, y_data)
            elif selected_fit == "logistic":
                tab.plot_logistic_fit(x_data, y_data)
            else:
                print("Unsupported fit type selected")

    def handle_fit_type_changed_gauss(self, index):
        selected_fit = self.ui.gauss.itemText(index)

        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            x_data= tab.dataframe.iloc[:, 0].values
            y_data= tab.dataframe.iloc[:, 1].values
            if selected_fit == "Gaussian":
                tab.plot_gaussian_fit(x_data, y_data)
            elif selected_fit == "lorenzian":
                tab.plot_lorentzian_fit(x_data, y_data)
            elif selected_fit == "voigt":
                tab.plot_voigt_fit(x_data, y_data)
            else:
                print("Unsupported fit type selected")

    def perform_power_fit(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]

            x_data = tab.dataframe.iloc[:, 0].values  # Replace [...] with actual x-axis data
            y_data = tab.dataframe.iloc[:, 1].values  # Replace [...] with actual y-axis data

            tab.plot_power_fit(x_data, y_data)


    def perform_cubic_fit(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]

            x_data = tab.dataframe.iloc[:, 0].values
            y_data = tab.dataframe.iloc[:, 1].values

            coeffs = np.polyfit(x_data, y_data, 3)

            x_values = np.linspace(min(x_data), max(x_data), 100)

            y_values = np.polyval(coeffs, x_values)

            tab.plot_cubic_curve(x_data, y_data, x_values, y_values)



    def perform_linear_fit(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]

            x_data = tab.dataframe.iloc[:, 0].values  # Replace [...] with actual x-axis data
            y_data = tab.dataframe.iloc[:, 1].values  # Replace [...] with actual y-axis data

                    # Perform linear fitting
            coeffs = np.polyfit(x_data, y_data, 1)

                    # Create a linear function from the coefficients
            poly_linear = np.poly1d(coeffs)

                    # Generate the x values for the fitted line
            x_fit = np.linspace(min(x_data), max(x_data), 100)

                    # Generate the y values using the fitted line function
            y_fit = poly_linear(x_fit)

                    # Plot the original data and the fitted line using Matplotlib
            tab.plot_linear_fit(x_data, y_data, x_fit, y_fit)






                ## worksheet ##

    def show_worksheet(self):

        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            df = self.tabs[tab_index].dataframe
            data = df.values.tolist()
            columns = df.columns.tolist()
            self.worksheet_dialog.ui.tableWidget.setRowCount(len(data))
            self.worksheet_dialog.ui.tableWidget.setColumnCount(len(columns))
            self.worksheet_dialog.ui.tableWidget.setHorizontalHeaderLabels(columns)
            for row_idx, row_data in enumerate(data):
                for col_idx, cell_data in enumerate(row_data):
                    item = QTableWidgetItem(str(cell_data))
                    self.worksheet_dialog.ui.tableWidget.setItem(row_idx, col_idx, item)

                    # If there is no tab selected, clear the table
        else:
            self.worksheet_dialog.ui.tableWidget.setRowCount(0)
            self.worksheet_dialog.ui.tableWidget.setColumnCount(0)
            self.worksheet_dialog.ui.tableWidget.clear()
        self.worksheet_dialog.show()

                ## customize ##


    def show_customize_dialog(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            self.customize_dialog.show()
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            self.customize_dialog.ui.graph_title.setText(tab.name)
            self.customize_dialog.ui.xLabel.setText(tab.xlabel)
            self.customize_dialog.ui.yLabel.setText(tab.ylabel)
            self.customize_dialog.ui.lagend.setChecked(tab.legend)
            self.customize_dialog.ui.location.setCurrentIndex(tab.legend_location)
            self.customize_dialog.ui.marker.setCurrentIndex(tab.marker)
            self.customize_dialog.ui.bg_color.setCurrentIndex(tab.fig_color)
            self.customize_dialog.ui.bg_color_2.setCurrentIndex(tab.can_color)
            self.customize_dialog.ui.grid.setChecked(tab.grid)

    def apply_custom(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab =self.tabs[tab_index]
            title = self.customize_dialog.ui.graph_title.text() 
            xlabel = self.customize_dialog.ui.xLabel.text() 
            ylabel = self.customize_dialog.ui.yLabel.text() 
            marker = self.customize_dialog.ui.marker.currentIndex()
            bg_color = self.customize_dialog.ui.bg_color.currentIndex()
            bg_color_2 = self.customize_dialog.ui.bg_color_2.currentIndex()
            legend = self.customize_dialog.ui.lagend.isChecked()
            location = self.customize_dialog.ui.location.currentIndex()
            real_time = self.customize_dialog.ui.real.isChecked()
            grid = self.customize_dialog.ui.grid.isChecked()
            tab.name=title
            self.ui.graphTab.setTabText(current_index, title)
            tab.xlabel=xlabel
            tab.ylabel=ylabel
            tab.marker=marker
            tab.fig_color=bg_color
            tab.can_color=bg_color_2
            tab.legend=legend
            tab.legend_location=location
            tab.time_check=real_time 
            tab.grid=grid 
            tab.custom_plot()
            self.customize_dialog.close()


                ## export ##

    def show_export_dialog(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            self.export_dialog.show()
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            self.export_dialog.ui.filename.setText(tab.name)
            self.export_dialog.ui.location.setText(self.get_download_dir())
        else :
            QMessageBox.warning(self, 'Warning', 'No plot selected.')

    def export(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab =self.tabs[tab_index]
            location = self.export_dialog.ui.location.text()
            filename = self.export_dialog.ui.filename.text()
            file_path = os.path.join(location, filename).replace("\\", "/")
            format = self.export_dialog.ui.format.currentText()
            dpi = self.export_dialog.ui.dpi.text()
            transparent = self.export_dialog.ui.transparent.isChecked()
            padding = self.export_dialog.ui.padding.text()
            tab.export(file_path, format, dpi, transparent, padding)
            self.export_dialog.reject()
        else :
            QMessageBox.warning(self, 'Warning', 'No plot selected.')

                ## interpolation ##
    def show_interpolation(self, file):
        filename, _ = os.path.splitext(file)
        self.interpolation_dialog.name = os.path.basename(filename)
        self.interpolation_dialog.delete_all_points()

        self.interpolation_dialog.points = []
        self.interpolation_dialog.coordinates = []

        img = mpimg.imread(file)
        rotated_img = np.flipud(img)
        self.interpolation_dialog.figure.clear()
        self.interpolation_dialog.ax = self.interpolation_dialog.figure.add_subplot()
        self.interpolation_dialog.ax.axis('off')
        self.interpolation_dialog.ax.set_position([0, 0, 1, 1])
        self.interpolation_dialog.ax.imshow(rotated_img, origin='lower')
        self.interpolation_dialog.plot_widget.draw()
        self.interpolation_dialog.show()

    def interpolate(self):
        df = pd.DataFrame(self.interpolation_dialog.coordinates)
        self.tabs.append(Tab(self.ui.graphTab, df, self.interpolation_dialog.name, None))
        pass
                ## function ##

    def show_function_dialog(self):
        self.function_dialog.show()


    def fx(self):
        start = self.function_dialog.ui.starter.value()
        end = self.function_dialog.ui.end.value()
        step = self.function_dialog.ui.step.value()
        func = self.function_dialog.ui.function.text()

        if start > end:
            temp = start
            start = end
            end = temp

        self.calculate_function(func, start, end, step)


    def calculate_function(self, function, start, end, step):
        step = 0.1 if step is None else step
        try:
            x_values = np.arange(start, end + step, step)
            function_values = []  

            for x in x_values:
                try:
                    modified_function = function.replace('X', f'({x})').replace('x', f'({x})')

                    for old, new in [('e', 'math.exp'), ('ln', 'math.log'), 
                                     ('cos', 'math.cos'), ('sin', 'math.sin'), 
                                     ('tan', 'math.tan'), ('^', '**')]:
                        modified_function = modified_function.replace(old, new)

                    function_values.append(eval(modified_function, {'math': math, '__builtins__': {}}))  
                except Exception:
                    function_values.append(None)

            results_df = pd.DataFrame({'X': x_values, 'Y': function_values})

            self.tabs.append(Tab(self.ui.graphTab, results_df, function, None))
        except Exception as e:
            print(f"Error: {e}")
            



    def exit_app(self):
        QApplication.quit()

    def get_min_max_values(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            df = self.tabs[tab_index].dataframe
            x_column = df.columns[0]
            y_column = df.columns[1]
            min_val = np.min(df[y_column])
            max_val = np.max(df[y_column])
            QMessageBox.information(self, "Min/Max Values", f"Minimum Value: {min_val}\nMaximum Value: {max_val}")

    #change types
    def toPlot(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            self.tabs[tab_index].to_plot()

    def toPiechart(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            self.tabs[tab_index].to_pie_chart()

    def toBar(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            self.tabs[tab_index].to_bar_chart()

    def toFill(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            self.tabs[tab_index].to_fill_between()

    def toStack(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            self.tabs[tab_index].to_stack_plot()

    #closing logic
    def close_current_tab(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            self.close_tab(current_index)

    def close_tab(self, index):
        reply = QMessageBox.question(self, 'Close Tab', 'Are you sure you want to close this tab?',
            QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            widget = self.ui.graphTab.widget(index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs.pop(tab_index)
            self.ui.graphTab.removeTab(index)
            tab.closePlot()



    #file logic
    def open_folder_dialog(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", options=options)

        if folder_path:
            # Clear the existing model
            self.ui.treeView.setModel(None)
            
            model = QFileSystemModel()
            model.setRootPath(folder_path)
            model.setFilter(QDir.AllDirs | QDir.Files | QDir.NoDotAndDotDot)
            model.setNameFilters(["*.xlsx", "*.csv", "*.json"])
            model.setNameFilterDisables(False)
            
            self.ui.treeView.setModel(model)
            self.ui.treeView.setRootIndex(model.index(folder_path))
            self.ui.treeView.setSortingEnabled(True)
            
            for column in range(1, model.columnCount()):
                self.ui.treeView.setColumnHidden(column, True)
            
        else:
            QMessageBox.warning(self, 'Warning', 'No folder selected.')

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()
            files = [url.toLocalFile() for url in event.mimeData().urls()]
            if len(files) == 1:
                dropped_index = self.ui.treeView.indexAt(event.pos())
                if dropped_index.isValid() and self.ui.treeView.model().fileInfo(dropped_index).isFile():
                    dropped_file = self.ui.treeView.model().filePath(dropped_index)
                    ext1 = os.path.splitext(dropped_file)[1]
                    ext2 = os.path.splitext(files[0])[1]
                    supported_formats = ['.csv', '.xlsx', '.json']
                    if ext1 in supported_formats and ext2 in supported_formats:
                        df1 = pd.read_csv(dropped_file) if ext1 == '.csv' else pd.read_excel(dropped_file) if ext1 == '.xlsx' else pd.read_json(dropped_file) 
                        df2 = pd.read_csv(files[0]) if ext2 == '.csv' else pd.read_excel(files[0]) if ext2 == '.xlsx' else pd.read_json(files[0])
                        df = pd.concat([df1, df2], ignore_index=True)
                        name = os.path.splitext(os.path.basename(dropped_file))[0] + '_' + os.path.splitext(os.path.basename(files[0]))[0]
                        os.path.getctime
                        self.tabs.append(Tab(self.ui.graphTab, df, name, None))
                    else:
                        QMessageBox.warning(self, 'Warning', 'Unsupported file format. Please select a CSV, Excel, or JSON file.')
                else:
                    QMessageBox.warning(self, 'Warning', 'Please drop the file onto another file in the tree view.')
            else:
                QMessageBox.warning(self, 'Warning', 'Please drop exactly one file.')
        else:
            event.ignore()

    def treeFileIndex(self, index):
        self.open_file(self.ui.treeView.model().filePath(index)) 


    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(
            self, "Open File", "", "Excel Files (*.xlsx);;CSV Files (*.csv);;JSON Files (*.json);;PNG Files (*.png)", options=options)
        if file_name:
            self.open_file(file_name)

    def open_file(self, file_path):
        if file_path and not os.path.isdir(file_path):
            df = pd.DataFrame()
            name, ext = os.path.splitext(file_path)
            supported_formats = ['.csv', '.xlsx', '.json', '.png']
            if ext in supported_formats:
                try:
                    if ext == '.csv':
                        df = pd.read_csv(file_path)
                    elif ext == '.xlsx':
                        df = pd.read_excel(file_path)
                    elif ext == '.json':
                        df = pd.read_json(file_path)
                    elif ext == '.png':
                        self.show_interpolation(file_path)
                        return 
                    name = os.path.basename(name)
                    self.tabs.append(Tab(self.ui.graphTab, df, name, file_path))
                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'Error loading file: {e}')
            else:
                QMessageBox.warning(self, 'Warning', 'Unsupported file format. Please select a CSV, Excel, JSON.')

    def focus(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            tab.focus()


    def get_download_dir(self):
        if platform.system() == 'Windows':
            return os.path.join(os.environ['USERPROFILE'], 'Downloads')
        elif platform.system() == 'Darwin':
            return os.path.join(os.path.expanduser('~'), 'Downloads')
        else:
            return os.path.join(os.path.expanduser('~'), 'Downloads')

    def save(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            file_path = tab.file
            if not file_path:
                options = QFileDialog.Options()
                file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;CSV Files (*.csv);;JSON Files (*.json)", options=options)

            if file_path:
                file_format = os.path.splitext(file_path)[-1][1:]
                return tab.saveFile(file_path, file_format)
        else :
            QMessageBox.warning(self, 'Warning', 'No plot selected.')
        return False


    def saveAs(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            options = QFileDialog.Options()
            file_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "Excel Files (*.xlsx);;CSV Files (*.csv);;JSON Files (*.json)", options=options)
            if file_path:
                file_format = os.path.splitext(file_path)[-1][1:]
                return tab.saveFile(file_path, file_format)
        return False

    def graph_full_screen(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            self.lastTab = tab
            self.ui.menubar.hide()
            self.ui.main.setCurrentIndex(1)
            self.ui.canv.setLayout(tab.lay)

    def graph_normal_screen(self):
        self.lastTab.setLayout(self.lastTab.lay)
        self.ui.menubar.show()
        self.ui.main.setCurrentIndex(0)



    def keyPressEvent(self, event):
        if event.key() == Qt.Key_F11:
            self.toggle_full_screen()
        else:
            super().keyPressEvent(event)

    def toggle_full_screen(self):
        self.full_screen = not self.full_screen
        self.showFullScreen() if self.full_screen else self.showNormal()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Graphite()
    widget.show()
    sys.exit(app.exec())
