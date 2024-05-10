import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QCheckBox, QLineEdit, QPushButton
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import numpy as np

class MatplotlibLegendToggler(QDialog):
    def __init__(self, tab, parent=None):
        super().__init__(parent)
        self.tab = tab
        self.plot = tab.ax
        self.artists = tab.artists
        self.init_ui()
        self.show()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.legend_widgets = []
        for i, artist in enumerate(self.artists):
            label = self.plot.get_legend().get_texts()[i].get_text()
            checkbox = QCheckBox()
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(lambda state, idx=i: self.toggle_legend(idx, state))
            layout.addWidget(checkbox)

            line_edit = QLineEdit(label)
            self.legend_widgets.append(line_edit)
            layout.addWidget(line_edit)

        apply_button = QPushButton('Apply')
        apply_button.clicked.connect(self.apply_legend_names)
        layout.addWidget(apply_button)

    def toggle_legend(self, idx, state):
        artist = self.artists[idx]
        artist.set_visible(state)

        self.tab.plot_widget.draw()

    def apply_legend_names(self):
        self.plot.legend([widget.text() for widget in self.legend_widgets], loc=self.tab.legend_location).set_visible(self.tab.legend)
        self.tab.plot_widget.draw()
