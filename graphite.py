import sys
import numpy as np
import os
from PySide6.QtGui import QKeySequence, QShortcut
from PySide6.QtCore import QDir
import pandas as pd
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog, QFileSystemModel, QAbstractItemView
from ui_form import Ui_Graphite
from graphs import Tab

class Graphite(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Graphite()
        self.ui.setupUi(self)
        self.ui.graphTab.tabCloseRequested.connect(self.close_tab)
        shortcut = QShortcut(QKeySequence("Alt+d"), self.ui.graphTab)
        shortcut.activated.connect(self.close_current_tab)
        self.ui.open_file.triggered.connect(self.open_file_dialog)
        self.ui.open_folder.triggered.connect(self.open_folder_dialog)
        self.ui.exit_app.triggered.connect(self.exit_app)

        self.ui.MathMode.triggered.connect(lambda: self.ui.mode_frames.setCurrentIndex(0))
        self.ui.BchimieMode.triggered.connect(lambda: self.ui.mode_frames.setCurrentIndex(2))

        self.ui.min_max.clicked.connect(self.get_min_max_values)

        #types
        self.ui.plot.clicked.connect(self.toPlot)
        self.ui.piechart.clicked.connect(self.toPiechart)
        self.ui.histogram.clicked.connect(self.toBar)

        self.tabs = []

    def exit_app(self):
        QApplication.quit()

    def get_min_max_values(self,df):
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
            model.setNameFilters(["*.xlsx", "*.csv"])
            model.setNameFilterDisables(False)
            
            self.ui.treeView.setModel(model)
            self.ui.treeView.setRootIndex(model.index(folder_path))
            self.ui.treeView.setSortingEnabled(True)
            
            # Hide the type, size, and date columns
            for column in range(1, model.columnCount()):
                self.ui.treeView.setColumnHidden(column, True)
            
            # Enable drag-and-drop
            self.ui.treeView.setDragEnabled(True)
            self.ui.treeView.setAcceptDrops(True)
            self.ui.treeView.setDropIndicatorShown(True)
            
            # Set drag-and-drop mode
            self.ui.treeView.setDragDropMode(QAbstractItemView.InternalMove)
            
            # Connect signal handlers for drag-and-drop events
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
                    if (ext1 == '.csv' or ext1 == '.xlsx') and (ext2 == '.csv' or ext2 == '.xlsx'):
                        df1 = pd.read_csv(dropped_file) if ext1 == '.csv' else pd.read_excel(dropped_file)
                        df2 = pd.read_csv(files[0]) if ext2 == '.csv' else pd.read_excel(files[0])
                        df = pd.concat([df1, df2], ignore_index=True)
                        name = os.path.basename(dropped_file) + '_' + os.path.basename(files[0])
                        self.tabs.append(Tab(self.ui.graphTab, df, name))
                    else:
                        QMessageBox.warning(self, 'Warning', 'Unsupported file format. Please select a CSV or Excel file.')
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
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx);;CSV Files (*.csv)", options=options)
        self.open_file(file_name)

    def open_file(self, file_path):
        if file_path:
            name, ext = os.path.splitext(file_path)
            if ext == '.csv' or ext == '.xlsx':
                df = None
                if ext == '.csv':
                    df = pd.read_csv(file_path)
                elif ext == '.xlsx':
                    df = pd.read_excel(file_path)
                if df is not None:
                    name = os.path.basename(name)
                    self.tabs.append(Tab(self.ui.graphTab, df, name))
            else:
                QMessageBox.warning(self, 'Warning', 'Unsupported file format. Please select a CSV or Excel file.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Graphite()
    widget.show()
    sys.exit(app.exec())
