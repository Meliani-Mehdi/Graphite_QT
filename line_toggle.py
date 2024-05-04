import sys
from PyQt6.QtWidgets import QApplication, QDialog, QVBoxLayout, QCheckBox, QPushButton

class LineDialog(QDialog):
    def __init__(self, ax, parent=None):
        super(LineDialog, self).__init__(parent)
        self.ax = ax

        self.lines = []
        self.checkboxes = []

        for line in self.ax.lines:
            line_name = line.get_label()
            checkbox = QCheckBox(line_name)
            checkbox.setChecked(True)
            checkbox.stateChanged.connect(lambda state, l=line: self.toggle_line(state, l))
            self.checkboxes.append(checkbox)

        layout = QVBoxLayout()
        for checkbox in self.checkboxes:
            layout.addWidget(checkbox)

        button = QPushButton("Close")
        button.clicked.connect(self.close_dialog)
        layout.addWidget(button)

        self.setLayout(layout)

    def toggle_line(self, state, line):
        line.set_visible(state == 2)

    def close_dialog(self):
        self.close()

if __name__ == '__main__':
    app = QApplication(sys.argv)

    import matplotlib.pyplot as plt
    import numpy as np
    fig, ax = plt.subplots()
    x = np.linspace(0, 10, 100)
    for i in range(1, 6):
        y = np.sin(x) * i
        ax.plot(x, y, label=f'Line {i}')

    dialog = LineDialog(ax)
    dialog.show()
    sys.exit(app.exec())
