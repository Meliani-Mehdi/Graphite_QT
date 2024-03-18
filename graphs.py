import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCore import Qt
from scipy.optimize import curve_fit
from scipy.special import voigt_profile

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
        layout = QHBoxLayout()
        layout.addWidget(self.plot_widget)
        self.setLayout(layout)
        self.to_plot()

        self.add_to_tab_widget()

    def plot_polynomial_curve(self, x_data, y_data, degree):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        coeffs = np.polyfit(x_data, y_data, degree)
        x_fit = np.linspace(min(x_data), max(x_data), 100)
        y_fit = np.polyval(coeffs, x_fit)
        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_fit, y_fit, 'r', label=f'Polynomial Fit (Degree {degree})')
        self.custom_plot()


    def plot_cubic_curve(self, x_data, y_data, x_values, y_values):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_values, y_values, 'r', label='Cubic Curve')

        self.custom_plot()

    def plot_gaussian_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

               # Perform Gaussian fitting
        try:
            def gaussian_func(x, a, x0, sigma):
                return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

            popt, pcov = curve_fit(gaussian_func, x_data, y_data)
            a, x0, sigma = popt
            y_fit = gaussian_func(x_data, a, x0, sigma)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Gaussian Fit')
            self.custom_plot()

        except Exception as e:
            print(f"Error plotting Gaussian fit: {e}")

    def plot_lorentzian_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

               # Perform Lorentzian fitting
        try:
            def lorentzian_func(x, a, x0, gamma):
                return a * gamma**2 / ((x - x0)**2 + gamma**2)

            popt, pcov = curve_fit(lorentzian_func, x_data, y_data)
            a, x0, gamma = popt
            y_fit = lorentzian_func(x_data, a, x0, gamma)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Lorentzian Fit')
            self.custom_plot()

        except Exception as e:
            print(f"Error plotting Lorentzian fit: {e}")

    def plot_voigt_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

               # Perform Voigt fitting
        try:
            def voigt_func(x, a, x0, sigma, gamma):
                return voigt_profile(x - x0, sigma, gamma) * a / (sigma * np.sqrt(2 * np.pi))

            popt, pcov = curve_fit(voigt_func, x_data, y_data)
            a, x0, sigma, gamma = popt
            y_fit = voigt_func(x_data, a, x0, sigma, gamma)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Voigt Fit')
            self.custom_plot()

        except Exception as e:
            print(f"Error plotting Voigt fit: {e}")



    def plot_power_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

        coeffs = np.polyfit(np.log(x_data), np.log(y_data), 1)
        a = np.exp(coeffs[1])
        b = coeffs[0]

        x_fit = np.linspace(min(x_data), max(x_data), 100)
        y_fit = a * np.power(x_fit, b)

        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_fit, y_fit, 'r', label='Power Fit')

        self.custom_plot()

    def plot_exponential_fit(self, x_data, y_data):
        def exponential_func(x, a, b):
            return a * np.exp(b * x)

        try:
            popt, pcov = curve_fit(exponential_func, x_data, y_data)
            a, b = popt

            x_fit = np.linspace(min(x_data), max(x_data), 100)
            y_fit = exponential_func(x_fit, *popt)

            self.figure.clear()
            self.ax = self.figure.add_subplot()
            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_fit, y_fit, 'r', label='Exponential Fit')
            self.custom_plot()

        except Exception as e:
            print(f"Error plotting exponential fit: {e}")

    def plot_double_exponential_fit(self, x_data, y_data):
        def double_exponential_func(x, a1, b1, a2, b2):
            return a1 * np.exp(b1 * x) + a2 * np.exp(b2 * x)

        try:
            popt, pcov = curve_fit(double_exponential_func, x_data, y_data)
            a1, b1, a2, b2 = popt

            x_fit = np.linspace(min(x_data), max(x_data), 100)
            y_fit = double_exponential_func(x_fit, *popt)

            self.figure.clear()
            self.ax = self.figure.add_subplot()
            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_fit, y_fit, 'r', label='Double Exponential Fit')
            self.custom_plot()

        except Exception as e:
            print(f"Error plotting double exponential fit: {e}")

    def plot_triple_exponential_fit(self, x_data, y_data):
        def triple_exponential_func(x, a1, b1, a2, b2, a3, b3):
            return a1 * np.exp(b1 * x) + a2 * np.exp(b2 * x) + a3 * np.exp(b3 * x)

        try:
            popt, pcov = curve_fit(triple_exponential_func, x_data, y_data)
            a1, b1, a2, b2, a3, b3 = popt

            x_fit = np.linspace(min(x_data), max(x_data), 100)
            y_fit = triple_exponential_func(x_fit, *popt)

            self.figure.clear()
            self.ax = self.figure.add_subplot()
            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_fit, y_fit, 'r', label='Triple Exponential Fit')
            self.custom_plot()

        except Exception as e:
            print(f"Error plotting triple exponential fit: {e}")


    def plot_logarithmic_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

                # Perform logarithmic fitting
        try:
            coeffs = np.polyfit(np.log(x_data), y_data, 1)
            a, b = coeffs
            y_fit = a * np.log(x_data) + b

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Logarithmic Fit')
            self.custom_plot()

        except Exception as e:
            print(f"Error plotting logarithmic fit: {e}")

    #def plot_logistic_fit(self, x_data, y_data):
      #  self.figure.clear()
      #  self.ax = self.figure.add_subplot()

                # Perform logistic fitting
       # try:
        #    def logistic_func(x, L, k, x0):
         #       return L / (1 + np.exp(-k * (x - x0)))

          #  popt, pcov = curve_fit(logistic_func, x_data, y_data)
           # L, k, x0 = popt
            #y_fit = logistic_func(x_data, L, k, x0)

           # self.ax.plot(x_data, y_data, 'bx', label='Data')
            #self.ax.plot(x_data, y_fit, 'r', label='Logistic Fit')
            #self.custom_plot()

        #except Exception as e:
         #   print(f"Error plotting logistic fit: {e}")


    def plot_linear_fit(self, x_data, y_data, x_fit, y_fit):
        self.ax.clear()
        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_fit, y_fit, 'r', label='linear Curve')


        self.custom_plot()

    def custom_plot(self):
        self.ax.set_title(self.name)
        self.ax.set_xlabel(self.xlabel)
        self.ax.set_ylabel(self.ylabel)
        self.ax.legend().set_visible(self.legend)
        self.plot_widget.draw()


    def to_plot(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        for _, col in enumerate(self.dataframe.columns[1:]):
            try:
                self.ax.plot(self.dataframe.iloc[:, 0], self.dataframe[col], label=col, marker='o')
            except Exception as e:
                print(f"Skipping column '{col}' because it could not be plotted: {e}")

        self.custom_plot()

    def to_pie_chart(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        data = self.dataframe.iloc[:, 1:].sum()
        self.ax.pie(data, labels=data.index, colors=self.colors, autopct='%1.1f%%')
        self.ax.set_title(self.name)
        self.custom_plot()

    def to_bar_chart(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

        num_cols = len(self.dataframe.columns)
        total_width = 0.8  
        width = total_width / num_cols  

        for i, col in enumerate(self.dataframe.columns):
            data = self.dataframe[col]
            try:
                self.ax.bar(data.index + i * width, data, width=width, label=col)
            except (ValueError, TypeError) as e:
                print(f"Error plotting column '{col}': {e}")

        self.custom_plot()

    def to_fill_between(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        x = np.array(self.dataframe.iloc[:, 0])
        for col in self.dataframe.columns[1:]:
            y = np.array(self.dataframe[col])
            try:
                self.ax.fill_between(x, y, alpha=0.5, linewidth=0)
            except Exception as e:
                print(f"Skipping column '{col}' because it could not be plotted: {e}")

        self.custom_plot()

    def to_stack_plot(self):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        x = self.dataframe.iloc[:, 0]
        y = self.dataframe.iloc[:, 1:].values.T
        labels = self.dataframe.columns[1:]
        colors = self.colors[:len(labels)]

        try:
            self.ax.stackplot(x, y, labels=labels, colors=colors, baseline='zero')
        except Exception as e:
            print(f"Error plotting stack plot: {e}")

        self.custom_plot()


    def plot_quadratic_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

        coeffs = np.polyfit(x_data, y_data, 2)

        x_fit = np.linspace(min(x_data), max(x_data), 100)

        y_fit = coeffs[0] * x_fit ** 2 + coeffs[1] * x_fit + coeffs[2]

        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_fit, y_fit, 'r', label='Quadratic Fit')

        self.custom_plot()
        
    def saveFile(self, filepath, file_format):
        print(filepath,file_format)
        try:
            if file_format == 'csv':
                self.dataframe.to_csv(filepath, index=False)
            elif file_format == 'xlsx':
                self.dataframe.to_excel(filepath, index=False)
            elif file_format == 'json':
                self.dataframe.to_json(filepath, orient='records')
            else:
                raise ValueError("Unsupported file format. Please select 'csv', 'excel' or 'json'.")
            return True
        except Exception as e:
            print(f"Error saving file: {e}")
            return False
    
    def export(self, filename, format='png', dpi=100, transparent=False, pad_inches=0.1):
        filepath = filename+'.'+format
        plt.savefig(filepath,
                    dpi=int(dpi),
                    transparent=transparent,
                    pad_inches=pad_inches)

    def closePlot(self):
        plt.close(self.figure)

    def add_to_tab_widget(self):
        self.tab_widget.addTab(self, self.name)
        self.tab_widget.setCurrentWidget(self)
