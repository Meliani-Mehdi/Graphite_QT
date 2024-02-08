import matplotlib.pyplot as plt
from PySide6.QtWidgets import QWidget, QVBoxLayout
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class Tab(QWidget):
    def __init__(self, tab_widget, dataframe, name):
        super().__init__()

        plt.style.use('dark_background')
        # Initialize the container (tab widget) and DataFrame
        self.tab_widget = tab_widget
        self.dataframe = dataframe
        self.name = name

        # Create a figure and axes for plotting
        self.figure, self.axes = plt.subplots()
        self.canvas = FigureCanvas(self.figure)

        # Create a layout for the tab
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

        # Plot the DataFrame on initialization
        self.plot_data()

        # Add the tab to the container
        self.add_to_tab_widget()

    def plot_data(self):
        # Plot DataFrame data
        # Example: plot first column as x-axis and second column as y-axis
        self.axes.plot(self.dataframe.iloc[:, 0], self.dataframe.iloc[:, 1])

        self.customPlot(self.name, 'X Axis', 'Y Axis')



    def customPlot(self,title,xlabel,ylabel):
        # Set plot title and labels
        self.axes.set_title(title)
        self.axes.set_xlabel(xlabel)
        self.axes.set_ylabel(ylabel)

        # Refresh canvas
        self.canvas.draw()


    def to_plot(self):
        pass

    def to_pie_chart(self):
        pass

    def to_bar_chart(self):
        pass

    def add_to_tab_widget(self):
        self.tab_widget.addTab(self, self.name)
