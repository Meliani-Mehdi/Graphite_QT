import sys
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


        #types
        self.ui.plot.clicked.connect(self.toPlot)
        self.ui.piechart.clicked.connect(self.toPiechart)
        self.ui.histogram.clicked.connect(self.toBar)

        self.tabs = []

    def exit_app(self):
        QApplication.quit()

    def on_combo_box_changed(self, index):
        self.ui.mode_frames.setCurrentIndex(index)

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
            print("Dropped files:", files)
            # Handle dropped files here
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
