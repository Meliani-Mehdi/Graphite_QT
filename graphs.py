import matplotlib.pyplot as plt
from matplotlib.typing import MarkerType
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PySide6.QtWidgets import QWidget, QVBoxLayout
from PySide6.QtCore import Qt

class Tab(QWidget):
    def __init__(self, tab_widget, dataframe, name):
        super().__init__()
        plt.style.use('dark_background')
        self.colors = [
            '#8ca252', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
            '#bcbd22', '#17becf', '#393b79', '#5254a3', '#6b6ecf', '#9c9ede', '#637939', '#b5cf6b', '#cedb9c',
            '#e7cb94', '#e7ba52', '#bd9e39', '#8c6d31', '#bd3939', '#ad494a', '#d6616b', '#e7969c', '#7b4173',
            '#a55194', '#ce6dbd',
        ]
        self.tab_widget = tab_widget
        self.dataframe = dataframe
        self.name = name
        self.xlabel = 'xlabel'
        self.ylabel = 'ylabel'
        self.legend = True

        self.figure, self.ax = plt.subplots()
        self.plot_widget = FigureCanvasQTAgg(self.figure)
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.plot_widget)
        self.setLayout(self.layout)
        self.to_plot()

        self.add_to_tab_widget()

    def plot_polynomial_curve(self, x_data, y_data, x_values, y_values):
        self.ax.clear()
        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_values, y_values, 'r', label='Polynomial Curve')

        self.custom_plot()

    def custom_plot(self):
        self.ax.set_title(self.name)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.legend().set_visible(self.legend)
        self.plot_widget.draw()


    def to_plot(self):
        self.ax.clear()
        for _, col in enumerate(self.dataframe.columns[1:]):
            try:
                self.ax.plot(self.dataframe.iloc[:, 0], self.dataframe[col], label=col, marker='o')
            except Exception as e:
                print(f"Skipping column '{col}' because it could not be plotted: {e}")

        self.custom_plot()

    def to_pie_chart(self):
        self.ax.clear()
        data = self.dataframe.iloc[:, 1:].sum()
        self.ax.pie(data, labels=data.index, colors=self.colors, autopct='%1.1f%%')
        self.ax.set_title(self.name)
        self.custom_plot()

    def to_bar_chart(self):
        self.ax.clear()
        self.dataframe.plot(kind='bar', ax=self.ax)
        self.custom_plot()

    def close_plot(self):
        plt.close(self.figure)

    def add_to_tab_widget(self):
        self.tab_widget.addTab(self, self.name)
