import sys
import os
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox, QFileDialog
from ui_form import Ui_Graphite
from graphs import Tab
import pandas as pd

class Graphite(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_Graphite()
        self.ui.setupUi(self)
        self.ui.graphTab.tabCloseRequested.connect(self.close_tab)
        self.ui.open_file.triggered.connect(self.open_file_dialog)
        self.ui.exit_app.triggered.connect(self.exit_app)
        self.tabs = []

    def exit_app(self):
        sys.exit(app.exec())

    def close_tab(self, index):
        reply = QMessageBox.question(self, 'Close Tab', 'Are you sure you want to close this tab?',
                                     QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if reply == QMessageBox.Yes:
            self.ui.graphTab.removeTab(index)

    def open_file_dialog(self):
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Open File", "", "Excel Files (*.xlsx);;CSV Files (*.csv)", options=options)

        if file_name:

            name, _ = os.path.splitext(os.path.basename(file_name))
            if file_name.endswith('.csv'):
                df = pd.read_csv(file_name)
                self.tabs.append(Tab(self.ui.graphTab,df,name))  

            elif file_name.endswith('.xlsx'):
                df = pd.read_excel(file_name)
                self.tabs.append(Tab(self.ui.graphTab,df,name))  
            else:
                QMessageBox.warning(self, 'Warning', 'Unsupported file format. Please select a CSV or Excel file.')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = Graphite()
    widget.show()
    sys.exit(app.exec())
