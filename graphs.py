import pyqtgraph as pg
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class Tab(QWidget):
    def __init__(self, tab_widget, dataframe, name):
        super().__init__()

        self.hex_colors = [
            '#8ca252',
            '#1f77b4',
            '#ff7f0e',
            '#2ca02c',
            '#d62728',
            '#9467bd',
            '#8c564b',
            '#e377c2',
            '#7f7f7f',
            '#bcbd22',
            '#17becf',
            '#393b79',
            '#5254a3',
            '#6b6ecf',
            '#9c9ede',
            '#637939',
            '#b5cf6b',
            '#cedb9c',
            '#e7cb94',
            '#e7ba52',
            '#bd9e39',
            '#8c6d31',
            '#bd3939',
            '#ad494a',
            '#d6616b',
            '#e7969c',
            '#7b4173',
            '#a55194',
            '#ce6dbd',
        ]
        self.tab_widget = tab_widget
        self.dataframe = dataframe
        self.name = name

        self.plot_widget = pg.PlotWidget()
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.plot_widget)
        self.setLayout(self.layout)
        self.to_plot()

        self.add_to_tab_widget()

    def customPlot(self, title, xlabel, ylabel, colors=None, legend=True):
        self.plot_widget.setTitle(title)
        self.plot_widget.setLabel('bottom', xlabel)
        self.plot_widget.setLabel('left', ylabel)
        if legend:
            self.plot_widget.addLegend()

        plots = self.plot_widget.listDataItems()

        for i, plot in enumerate(plots):
            plot.setPen(pg.mkPen(color=colors[i] if colors else (0, 255, 0)))

    def to_plot(self):
        self.plot_widget.clear()
        for _, col in enumerate(self.dataframe.columns[1:]):
            try:
                self.plot_widget.plot(self.dataframe.iloc[:, 0], self.dataframe[col], name=col)
            except Exception as e:
                print(f"Skipping column '{col}' because it could not be plotted: {e}")

        self.customPlot(self.name, 'X Axis', 'Y Axis', self.hex_colors, True)

    def to_pie_chart(self):
        self.plot_widget.clear()
        
        # Check if the dataframe is not empty and has at least two rows
        if not self.dataframe.empty and len(self.dataframe) >= 2:
            # Use the first row as labels and the second row as values
            labels = self.dataframe.iloc[0, :].tolist()
            values = self.dataframe.iloc[1, :].tolist()
            
            # Create PiePlotItem
            pie = pg.PiePlotItem(labels=labels, values=values, brush=pg.intColor(0))
            
            # Create PlotWidget
            self.customPlot("Pie Chart", 'X Axis', 'Y Axis', self.hex_colors, legend=False)
            
            # Add PiePlotItem to PlotWidget
            self.plot_widget.addItem(pie)
        else:
            # Handle case where dataframe is empty or doesn't have enough rows
            print("Dataframe is empty or does not have enough rows. Cannot plot pie chart.")

    def to_bar_chart(self):
        self.plot_widget.clear()
        # Assume self.dataframe has the data for the bar chart
        bar_data = self.dataframe.iloc[:, 1].values  # Example data
        x = range(len(bar_data))
        self.plot_widget.plot(x, bar_data, pen=None, symbolBrush=self.hex_colors[:len(bar_data)], symbolPen=None, symbol='s')
        self.customPlot("Bar Chart", 'X Axis', 'Y Axis', self.hex_colors[:len(bar_data)], legend=False)

    def closePlot(self):
        self.plot_widget.clear()
        self.plot_widget.close()

    def add_to_tab_widget(self):
        self.tab_widget.addTab(self, self.name)
