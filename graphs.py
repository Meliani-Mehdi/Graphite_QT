import matplotlib
import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class Tab(QWidget):
    def __init__(self, tab_widget, dataframe, name):
        super().__init__()

        plt.style.use('dark_background')

        self.hex_colors = [
                    "#7FFF00",  
                    "#FF5733",
                    "#33FFB8",
                    "#3366FF",
                    "#ADFF2F",  
                    "#2E8B57",  
                    "#FF33DD",
                    "#33FF57",
                    "#FF3366",
                    "#33B8FF",
                    "#FF5733",
                    "#32CD32",  
                    "#33FFB8",
                    "#3366FF",
                    "#FFD700",  
                    "#00FF00",  
                    "#3CB371",  
                    "#20B2AA",  
                    "#7FFFD4",
                    "#228B22"  
                            ]
        self.tab_widget = tab_widget
        self.dataframe = dataframe
        self.name = name

        self.figure, self.axes = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)
        self.to_plot()

        self.add_to_tab_widget()

    def customPlot(self, title, xlabel, ylabel, colors=None, legend=True):
        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)
        if legend:
            self.axes.legend()

        plot_objects = self.axes.get_children()

        for i, plot_object in enumerate(plot_objects):
            if isinstance(plot_object, matplotlib.lines.Line2D):  # Line plot
                plot_object.set_color(colors[i] if colors else 'blue')
            elif isinstance(plot_object, matplotlib.patches.Polygon):  # Histogram
                plot_object.set_facecolor(colors[i] if colors else 'blue')
            elif isinstance(plot_object, matplotlib.patches.Wedge):  # Pie chart
                plot_object.set_facecolor(colors[i] if colors else 'blue')
            elif isinstance(plot_object, matplotlib.collections.PolyCollection):  # Fill between
                plot_object.set_facecolor(colors[i] if colors else 'blue')
            elif isinstance(plot_object, matplotlib.container.BarContainer):  # Stack plot
                for stack, color in zip(plot_object, colors):
                    for bar in stack:
                        bar.set_color(color)

        self.canvas.draw()

    def to_plot(self):
        self.axes.clear()
        for _, col in enumerate(self.dataframe.columns[1:]):
            self.axes.plot(self.dataframe.iloc[:, 0], self.dataframe[col], label=col)

        self.customPlot(self.name, 'X Axis', 'Y Axis', self.hex_colors)

    def to_pie_chart(self):
        self.axes.clear()
        # Example pie chart using first row of data
        self.axes.pie(self.dataframe.iloc[0, 1:], labels=self.dataframe.columns[1:], autopct='%1.1f%%')
        self.customPlot(self.name, '', '', self.hex_colors, False)

    def to_bar_chart(self):
        self.axes.clear()
        # Example bar chart using first row of data
        self.axes.bar(self.dataframe.columns[1:], self.dataframe.iloc[0, 1:])
        self.customPlot(self.name, 'X Axis', 'Y Axis', self.hex_colors)

    def closePlot(self):
        self.axes.clear()
        plt.close(self.figure)
        self.canvas.draw()

    def add_to_tab_widget(self):
        self.tab_widget.addTab(self, self.name)
