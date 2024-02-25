import sys
import numpy as np
import os
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtCore import QDir
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QFileSystemModel, QAbstractItemView, QDialog
from ui_form import Ui_Graphite
from ui_customize_dialog import Ui_Dialog as custom
from ui_export import Ui_Dialog as export
from graphs import Tab

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

class Graphite(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Graphite()
        self.ui.setupUi(self)
        self.ui.graphTab.tabCloseRequested.connect(self.close_tab)
        shortcut = QShortcut(QKeySequence("Alt+d"), self.ui.graphTab)
        shortcut.activated.connect(self.close_current_tab)

        #menu functions
        self.ui.open_file.triggered.connect(self.open_file_dialog)
        self.ui.open_folder.triggered.connect(self.open_folder_dialog)
        self.ui.save_as.triggered.connect(self.saveAs)
        self.ui.exit_app.triggered.connect(self.exit_app)

        self.ui.MathMode.triggered.connect(lambda: self.ui.mode_frames.setCurrentIndex(0))
        self.ui.BchimieMode.triggered.connect(lambda: self.ui.mode_frames.setCurrentIndex(2))

        self.ui.min_max.clicked.connect(self.get_min_max_values)
        self.ui.Polynome.clicked.connect(self.perform_polynomial_fitting)
        self.ui.linear.clicked.connect(self.perform_linear_fit)

        #types
        self.ui.plot.clicked.connect(self.toPlot)
        self.ui.piechart.clicked.connect(self.toPiechart)
        self.ui.histogram.clicked.connect(self.toBar)

        self.tabs = []

        self.customize_dialog = CustomizeDialog(self)
        self.customize_dialog.ui.apply_btn.clicked.connect(self.apply_custom)
        self.ui.custom_button.clicked.connect(self.show_customize_dialog)

        self.export_dialog = ExportDialog(self)
        self.export_dialog.ui.expo.clicked.connect(self.export)
        self.ui.expo.triggered.connect(self.show_export_dialog)


    def perform_polynomial_fitting(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]

            x_data = tab.dataframe.iloc[:, 0].values
            y_data = tab.dataframe.iloc[:, 1].values

            degree = 2  
            coeffs = np.polyfit(x_data, y_data, degree)

            x_values = np.linspace(min(x_data), max(x_data), 100)
            y_values = np.polyval(coeffs, x_values)

            tab.plot_polynomial_curve(x_data, y_data, x_values, y_values)


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


                ## customize ##

    def show_customize_dialog(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            self.customize_dialog.show()
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            self.customize_dialog.ui.graph_title.setPlainText(tab.name)
            self.customize_dialog.ui.xLabel.setPlainText(tab.xlabel)
            self.customize_dialog.ui.yLabel.setPlainText(tab.ylabel)
            self.customize_dialog.ui.lagend.setChecked(tab.legend)

    def apply_custom(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab =self.tabs[tab_index]
            title = self.customize_dialog.ui.graph_title.toPlainText() 
            xlabel = self.customize_dialog.ui.xLabel.toPlainText() 
            ylabel = self.customize_dialog.ui.yLabel.toPlainText() 
            legend = self.customize_dialog.ui.lagend.isChecked()
            tab.name=title
            tab.xlabel=xlabel
            tab.ylabel=ylabel
            tab.legend=legend
            tab.custom_plot()
            self.customize_dialog.reject()


                ## export ##

    def show_export_dialog(self):
        current_index = self.ui.graphTab.currentIndex()
        if current_index != -1:
            self.export_dialog.show()
            widget = self.ui.graphTab.widget(current_index)
            tab_index = self.tabs.index(widget)
            tab = self.tabs[tab_index]
            self.export_dialog.ui.filename.setText(tab.name)

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

    def open_folder_dialog(self):
        options = QFileDialog.Options()
        folder_path = QFileDialog.getExistingDirectory(self, "Open Folder", options=options)

        if folder_path:
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
            
            self.ui.treeView.setDragEnabled(True)
            self.ui.treeView.setAcceptDrops(True)
            self.ui.treeView.setDropIndicatorShown(True)
            
            self.ui.treeView.setDragDropMode(QAbstractItemView.InternalMove)
            
            self.ui.treeView.dragEnterEvent = self.dragEnterEvent
            self.ui.treeView.dragMoveEvent = self.dragMoveEvent
            self.ui.treeView.dropEvent = self.dropEvent
            
            self.ui.treeView.doubleClicked.connect(self.treeFileIndex)
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
                        self.tabs.append(Tab(self.ui.graphTab, df, name))
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
            self, "Open File", "", "Excel Files (*.xlsx);;CSV Files (*.csv);;JSON Files (*.json)", options=options)
        if file_name:
            self.open_file(file_name)

    def open_file(self, file_path):
        if file_path:
            df = pd.DataFrame()
            name, ext = os.path.splitext(file_path)
            supported_formats = ['.csv', '.xlsx', '.json']
            if ext in supported_formats:
                try:
                    if ext == '.csv':
                        df = pd.read_csv(file_path)
                    elif ext == '.xlsx':
                        df = pd.read_excel(file_path)
                    elif ext == '.json':
                        df = pd.read_json(file_path)
                    name = os.path.basename(name)
                    self.tabs.append(Tab(self.ui.graphTab, df, name))
                except Exception as e:
                    QMessageBox.warning(self, 'Error', f'Error loading file: {e}')
            else:
                QMessageBox.warning(self, 'Warning', 'Unsupported file format. Please select a CSV, Excel, JSON.')

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
                print(file_path,file_format)
                return tab.saveFile(file_path, file_format)
        return False


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Graphite()
    widget.show()
    sys.exit(app.exec())
