import sys
from PySide6.QtWidgets import QApplication, QDialog, QVBoxLayout, QWidget, QCheckBox, QLabel, QLineEdit, QPushButton
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import numpy as np

class MatplotlibLegendToggler(QDialog):
    def __init__(self, tab, parent=None):
        super().__init__(parent)
        self.tab = tab
        self.plot = tab.ax
        self.init_ui()
        self.show()

    def init_ui(self):
        layout = QVBoxLayout(self)

        self.legend_widgets = []
        for i, line in enumerate(self.plot.lines):
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
        self.plot.lines[idx].set_visible(state)
        self.plot.legend([widget.text() for widget in self.legend_widgets])
        self.plot.legend(loc=self.tab.legend_location).set_visible(self.tab.legend)
        self.tab.plot_widget.draw()

    def apply_legend_names(self):
        self.plot.legend([widget.text() for widget in self.legend_widgets],loc=self.tab.legend_location).set_visible(self.tab.legend)
        self.tab.plot_widget.draw()

# Example usage
# import matplotlib.pyplot as plt
#
# x = np.linspace(0, 10, 100)
# y1 = np.sin(x)
# y2 = np.cos(x)
#
# fig, ax = plt.subplots()
# ax.plot(x, y1, label='sin(x)')
# ax.plot(x, y2, label='cos(x)')
# ax.legend()
#
# app = QApplication(sys.argv)
# window = MatplotlibLegendToggler(ax)
# window.show()
# sys.exit(app.exec())
