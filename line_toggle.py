from PySide6.QtWidgets import  QDialog, QHBoxLayout, QLabel, QVBoxLayout, QCheckBox, QLineEdit, QPushButton
import matplotlib.container as container

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
        for i, _ in enumerate(self.artists):
            holder = QHBoxLayout()
            layout.addLayout(holder)
            label= None
            try:
                label = self.plot.get_legend().get_texts()[i].get_text()
            except Exception as e:
                print("no lab")
            checkbox = QCheckBox()
            t = self.isVis(self.artists[i])
            checkbox.setChecked(t)
            checkbox.stateChanged.connect(lambda state, idx=i: self.toggle_legend(idx, state))
            holder.addWidget(checkbox)

            if label:
                line_edit = QLineEdit(label)
                line_edit.textChanged.connect(self.apply_legend_names)
                self.legend_widgets.append(line_edit)
                holder.addWidget(line_edit)
            else:
                lab = QLabel(f'Level {i+1}')
                holder.addWidget(lab)

    def isVis(self, artist) -> bool:
        if isinstance(artist, container.BarContainer):
            return artist[0].get_visible()
        else:
            return artist.get_visible()

    def toggle_legend(self, idx, state):
        artist = self.artists[idx]
        if isinstance(artist, container.BarContainer):
            for art in artist:
                art.set_visible(state)
        else:
            artist.set_visible(state)
        self.apply_legend_names()


    def apply_legend_names(self):
        self.plot.legend([widget.text() for widget in self.legend_widgets], loc=self.tab.legend_location).set_visible(self.tab.legend)
        self.tab.plot_widget.draw()
