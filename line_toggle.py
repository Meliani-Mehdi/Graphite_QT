from PySide6.QtWidgets import  QDialog, QHBoxLayout, QLabel, QScrollArea, QVBoxLayout, QCheckBox, QLineEdit, QWidget
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
        layout = QVBoxLayout()

        scroll_area = QScrollArea()
        scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(scroll_widget)

        self.legend_widgets = []
        for i, _ in enumerate(self.artists):
            holder = QHBoxLayout()
            label= None
            try:
                label = self.plot.get_legend().get_texts()[i].get_text()
            except Exception:
                pass
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

            scroll_layout.addLayout(holder)

        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(scroll_widget)

        layout.addWidget(scroll_area)

        self.setLayout(layout)
        self.setMinimumSize(200, 150)

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
        if self.tab.last_plot not in [self.tab.to_contour_plot, self.tab.to_contourf_plot, self.tab.to_imshow_plot, self.tab.to_pcolormesh_plot]:
            self.plot.legend([widget.text() for widget in self.legend_widgets], loc=self.tab.legend_location, fancybox=True, framealpha=0.85, facecolor=self.tab.fig_colors[self.tab.fig_color], edgecolor=self.tab.rev_colors[self.tab.fig_color]).set_visible(self.tab.legend)
            for text in self.tab.ax.get_legend().get_texts():
                text.set_color(self.tab.rev_colors[self.tab.fig_color])
        self.tab.plot_widget.draw()
            
