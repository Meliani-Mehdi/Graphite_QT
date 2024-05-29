import matplotlib.pyplot as plt
import os
import numpy as np
import pandas as pd
import seaborn as sns
import shutil
import zipfile
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.patches import Rectangle
from PySide6.QtWidgets import QWidget, QHBoxLayout
from PySide6.QtCore import QTimer
from scipy.optimize import curve_fit
from scipy.special import voigt_profile
from scipy.interpolate import UnivariateSpline
from scipy.signal import savgol_filter, butter, filtfilt, medfilt, cheby1, butter
from statsmodels.nonparametric.smoothers_lowess import lowess
from scipy.ndimage import gaussian_filter1d



class Tab(QWidget):
    def __init__(self, tab_widget, dataframe, name, file):
        super().__init__()
        plt.style.use('dark_background')
        self.colors = [
            '#8ca252', '#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f',
            '#bcbd22', '#17becf', '#393b79', '#5254a3', '#6b6ecf', '#9c9ede', '#637939', '#b5cf6b', '#cedb9c',
            '#e7cb94', '#e7ba52', '#bd9e39', '#8c6d31', '#bd3939', '#ad494a', '#d6616b', '#e7969c', '#7b4173',
            '#a55194', '#ce6dbd',
        ]
        self.markers = ["None", ".", ",", "o", "^", "v", ">", "<", "2", "1", "4", "3", "8", "s", "p", "+", "P", "x", "X", "*", "h", "D", "d", "|", "_", 2, 3, 1, 0, 6, 7, 5, 4,]
        self.fig_colors = [ '#000000', '#2c2c2c', '#404040', '#D3D3D3', '#FFFFFF', '#008000', '#FFA500', '#FF0000', '#FFC0CB', '#FFFF00', '#FFFFE0', '#00FFFF', '#E0FFFF' ]
        self.rev_colors = self.rev_all(self.fig_colors)
        self.tab_widget = tab_widget
        self.dataframe = dataframe
        self.name = name
        self.fitted_dataframe = None
        self.file = file
        if self.file is not None:
            self.last_time = os.path.getmtime(self.file)
        self.xlabel = 'xlabel'
        self.ylabel = 'ylabel'
        self.artists = []
        self.legend = True
        self.legend_location = 0
        self.marker = 0
        self.last_marker = 0
        self.can_color = 0
        self.fig_color = 0
        self.grid = True

        self.time_check = False
        self.timer = QTimer(self)
        self.interval = 300
        self.timer.timeout.connect(self.realtime)
        self.last_plot = self.to_plot
        self.typeNum = None

        self.def_vals = None
        self.button_pressed = False
        self.zoom_rect = None
        self.press = None

        self.figure, self.ax = plt.subplots()
        self.plot_widget = FigureCanvasQTAgg(self.figure)
        self.lay = QHBoxLayout()
        self.lay.setContentsMargins(0, 0, 0, 0)
        self.lay.addWidget(self.plot_widget)

        self.text = self.figure.text(0.95, 0.95, '', ha='right')

        self.figure.canvas.mpl_connect('button_press_event', self.on_press)
        self.figure.canvas.mpl_connect('button_release_event', self.on_release)
        self.figure.canvas.mpl_connect('motion_notify_event', self.on_motion)
        self.figure.canvas.mpl_connect('scroll_event', self.on_scroll)

        self.setLayout(self.lay)
        self.to_plot()

        self.add_to_tab_widget()



    #interactive plots

    def on_press(self, event):
        if event.button == 1:
            self.button_pressed = True
            self.press_x = event.xdata
            self.press_y = event.ydata

        elif event.button == 3 and event.inaxes == self.ax:
            self.press = event.xdata, event.ydata
            if self.zoom_rect is not None:
                self.zoom_rect.remove()
            self.zoom_rect = Rectangle((self.press[0], self.press[1]), 0, 0,
                                        linewidth=1, edgecolor='r', facecolor='none')
            self.ax.add_patch(self.zoom_rect)
            self.figure.canvas.draw()

    def on_release(self, event):
        if event.button == 1:
            self.button_pressed = False
        if event.button == 3 and self.press is not None and event.inaxes == self.ax:
            xpress, ypress = self.press
            xrelease, yrelease = event.xdata, event.ydata
            xmin = min(xpress, xrelease)
            xmax = max(xpress, xrelease)
            ymin = min(ypress, yrelease)
            ymax = max(ypress, yrelease)
            self.ax.set_xlim(xmin, xmax)
            self.ax.set_ylim(ymin, ymax)
            if self.zoom_rect is not None:
                self.zoom_rect.remove()
            self.figure.canvas.draw()
            self.press = None
            self.zoom_rect = None


    def on_motion(self, event):
        if event.button == 3 and self.press is not None and event.inaxes == self.ax:
            xpress, ypress = self.press
            xrelease, yrelease = event.xdata, event.ydata
            xmin = min(xpress, xrelease)
            xmax = max(xpress, xrelease)
            ymin = min(ypress, yrelease)
            ymax = max(ypress, yrelease)
            self.zoom_rect.set_xy((xmin, ymin))
            self.zoom_rect.set_width(xmax - xmin)
            self.zoom_rect.set_height(ymax - ymin)
            self.figure.canvas.draw()

        if event.inaxes == self.ax:
            x = event.xdata
            y = event.ydata
            self.text.set_text(f'x={x:.2f}, y={y:.2f}')
            self.text.set_color(self.rev_colors[self.can_color])
            if x is not None and y is not None:
                if self.button_pressed:
                    dx = x - self.press_x
                    dy = y - self.press_y
                    self.ax.set_xlim(self.ax.get_xlim() - dx)
                    self.ax.set_ylim(self.ax.get_ylim() - dy)
        else:
            self.text.set_text('')
        self.figure.canvas.draw()
        self.text.set_text('')

    def on_scroll(self, event):
        if event.button == 'up':
            scale_factor = 0.9
        elif event.button == 'down':
            scale_factor = 1.1
        else:
            scale_factor = 1.0

        xdata, ydata = event.xdata, event.ydata
        xlim = self.ax.get_xlim()
        ylim = self.ax.get_ylim()

        new_xlim = (xlim[0] - xdata) * scale_factor + xdata, (xlim[1] - xdata) * scale_factor + xdata
        new_ylim = (ylim[0] - ydata) * scale_factor + ydata, (ylim[1] - ydata) * scale_factor + ydata

        self.ax.set_xlim(new_xlim)
        self.ax.set_ylim(new_ylim)
        self.figure.canvas.draw_idle()

    def focus(self):
        if self.def_vals is not None:
            self.ax.set_xlim(self.def_vals[0])
            self.ax.set_ylim(self.def_vals[1])
            self.plot_widget.draw()



    #filtters





    def plot_entered_function(self, function_str):
           try:
               x_values = np.linspace(-10, 10, 100)
               y_values = eval(function_str, {'np': np, 'x': x_values})
               self.ax.clear()
               self.ax.plot(x_values, y_values, color='red', label='Entered Function')
               self.custom_plot()
           except Exception as e:
              print( 'Error', f"Error plotting entered function: {e}")
    def plot_polynomial_curve(self, x_data, y_data, degree):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        coeffs = np.polyfit(x_data, y_data, degree)
        x_fit = np.linspace(min(x_data), max(x_data), 100)
        y_fit = np.polyval(coeffs, x_fit)
        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_fit, y_fit, 'r', label=f'Polynomial Fit (Degree {degree})')
        self.custom_plot()
        self.fitted_dataframe = pd.DataFrame({'x': x_fit, f'y_poly_fit_deg_{degree}': y_fit})
        #fitted_data = pd.DataFrame({'x': x_fit, 'y': y_fit})
        #self.dataframe = fitted_data


    def plot_cubic_curve(self, x_data, y_data, x_values, y_values):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_values, y_values, 'r', label='Cubic Curve')

        self.custom_plot()

    def plot_gaussian_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def gaussian_func(x, a, x0, sigma):
                return a * np.exp(-(x - x0)**2 / (2 * sigma**2))

            popt, pcov = curve_fit(gaussian_func, x_data, y_data)
            a, x0, sigma = popt
            y_fit = gaussian_func(x_data, a, x0, sigma)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Gaussian Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Gaussian fit: {e}")

    def plot_lorentzian_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def lorentzian_func(x, a, x0, gamma):
                return a * gamma**2 / ((x - x0)**2 + gamma**2)

            popt, pcov = curve_fit(lorentzian_func, x_data, y_data)
            a, x0, gamma = popt
            y_fit = lorentzian_func(x_data, a, x0, gamma)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Lorentzian Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Lorentzian fit: {e}")

    def plot_voigt_fit(self, x_data, y_data):
        try:
            self.figure.clear()
            self.ax = self.figure.add_subplot()

            def voigt_func(x, a, x0, sigma, gamma):
                return voigt_profile(x - x0, sigma, gamma) * a / (sigma * np.sqrt(2 * np.pi))


            initial_guesses = [1.0, np.mean(x_data), 1.0, 1.0]
            lower_bounds = [0.0, -np.inf, 0.0, 0.0]
            upper_bounds = [np.inf, np.inf, np.inf, np.inf]

            popt, pcov = curve_fit(voigt_func, x_data, y_data, p0=initial_guesses, bounds=(lower_bounds, upper_bounds))
            a, x0, sigma, gamma = popt
            y_fit = voigt_func(x_data, a, x0, sigma, gamma)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Voigt Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Voigt fit: {e}")


    def plot_fourier_fit(self, x_data, y_data, num_terms=3):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def fourier_series(x, *a):
                res = a[0] / 2
                for i in range(1, num_terms * 2, 2):
                    res += a[i] * np.sin(i * np.pi * x) + a[i + 1] * np.cos(i * np.pi * x)
                return res

            p0 = [1.0] * (num_terms * 2 + 1)
            popt, pcov = curve_fit(fourier_series, x_data, y_data, p0=p0)
            y_fit = fourier_series(x_data, *popt)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Fourier Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Fourier fit: {e}")

    def plot_sine_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def sine_func(x, a, b, c):
                return a * np.sin(b * x + c)

            initial_guesses = [max(y_data), 2 * np.pi / (max(x_data) - min(x_data)), 0]
            popt, pcov = curve_fit(sine_func, x_data, y_data, p0=initial_guesses)
            a, b, c = popt
            y_fit = sine_func(x_data, a, b, c)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Sine Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Sine fit: {e}")

    def plot_cosine_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def cosine_func(x, a, b, c):
                return a * np.cos(b * x + c)
            initial_guesses = [max(y_data), 2 * np.pi / (max(x_data) - min(x_data)), 0]
            popt, pcov = curve_fit(cosine_func, x_data, y_data, p0=initial_guesses)
            a, b, c = popt
            y_fit = cosine_func(x_data, a, b, c)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Cosine Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Cosine fit: {e}")


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
        self.fitted_dataframe = pd.DataFrame({'x': x_fit, 'y': y_fit})
        #fitted_data = pd.DataFrame({'x': x_fit, 'y': y_fit})
        #self.dataframe = fitted_data

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
            self.fitted_dataframe = pd.DataFrame({'x': x_fit, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_fit, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting exponential fit: {e}")

    def plot_double_exponential_fit(self, x_data, y_data): 
        self.figure.clear()
        self.ax = self.figure.add_subplot()

        try:
            def double_exponential_func(x, a1, b1, a2, b2):
                return a1 * np.exp(b1 * x) + a2 * np.exp(b2 * x)

            p0 = [1.0, 0.1, 1.0, 0.1]
            popt, pcov = curve_fit(double_exponential_func, x_data, y_data, p0=p0, maxfev=5000)
            a1, b1, a2, b2 = popt

            x_fit = np.linspace(min(x_data), max(x_data), 100)
            y_fit = double_exponential_func(x_fit, *popt)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_fit, y_fit, 'r', label='Double Exponential Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_fit, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_fit, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting double exponential fit: {e}")

    def moving_average_filter(self, data, window_size):
        return np.convolve(data, np.ones(window_size)/window_size, mode='valid')

    def savitzky_golay_filter(self, data, window_length, polyorder):
        return savgol_filter(data, window_length, polyorder)

    def butterworth_filter(self, data, cutoff, fs=1, btype='lowpass', order=4):
            b, a = butter(order, cutoff, btype=btype, fs=fs)
            padlen = 3 * max(len(a), len(b))
            if len(data) <= padlen:
                raise ValueError("Input data length must be greater than padlen")
            filtered_data = filtfilt(b, a, data)
            return filtered_data


    def median_filter(self, data, kernel_size):
        return medfilt(data, kernel_size)

    def exponential_filter(self, data, alpha):
        result = np.zeros_like(data)
        result[0] = data[0]
        for i in range(1, len(data)):
            result[i] = alpha * data[i] + (1 - alpha) * result[i-1]
        return result

    def apply_gaussian_filter(self, dataframe, sigma):
           filtered_data = gaussian_filter1d(dataframe, sigma, axis=0)
           return filtered_data


    def apply_chebyshev_filter(self, dataframe, Wn, rp, rs):
        b, a = cheby1(4, rp, Wn, 'lowpass', fs=1)
        filtered_data = np.apply_along_axis(lambda x: np.convolve(x, b/a, mode='same'), axis=0, arr=dataframe)
        self.dataframe = pd.DataFrame(filtered_data, columns=dataframe.columns)
        return filtered_data

    def apply_boxcar_filter(self, dataframe, window_size):
        kernel = np.ones(window_size) / window_size
        filtered_data = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), axis=0, arr=dataframe)
        return filtered_data



   # def create_notch_filter(fs, f0, Q):
    #    nyquist = 0.5 * fs
     #   w0 = f0 / nyquist
       # b, a = butter(2, (w0 - 1/(2*Q), w0 + 1/(2*Q)), btype='bandstop')
      #  return b, a

   # def apply_notch_filter(self, dataframe, Q, freq):
    #    b, a = notch(freq, Q)
     #   filtered_data = np.apply_along_axis(lambda x: np.convolve(x, b/a, mode='same'), axis=0, arr=dataframe)
      #  return filtered_data

    def apply_bandpass_filter(self, dataframe, lowcut, highcut, fs, order):
        b, a = butter(order, [lowcut, highcut], btype='band', fs=fs)
        filtered_data = filtfilt(b, a, dataframe, axis=0)
        return filtered_data

    def apply_lowpass_filter(self, dataframe, cutoff, fs, order):
        b, a = butter(order, cutoff, btype='low', fs=fs)
        filtered_data = filtfilt(b, a, dataframe, axis=0)
        return filtered_data

    def apply_highpass_filter(self, dataframe, cutoff, fs, order):
        b, a = butter(order, cutoff, btype='high', fs=fs)
        filtered_data = filtfilt(b, a, dataframe, axis=0)
        return filtered_data

    def lowess_filter(self, x_data, y_data, frac):
        smoothed = lowess(y_data, x_data, frac=frac)
        return smoothed[:, 1]

    def plot_triple_exponential_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

        try:
            def triple_exponential_func(x, a1, b1, a2, b2, a3, b3):
                return a1 * np.exp(b1 * x) + a2 * np.exp(b2 * x) + a3 * np.exp(b3 * x)

            p0 = [1.0, 0.1, 1.0, 0.1, 1.0, 0.1]
            popt, pcov = curve_fit(triple_exponential_func, x_data, y_data, p0=p0, maxfev=5000)
            a1, b1, a2, b2, a3, b3 = popt

            x_fit = np.linspace(min(x_data), max(x_data), 100)
            y_fit = triple_exponential_func(x_fit, *popt)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_fit, y_fit, 'r', label='Triple Exponential Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_fit, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_fit, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting triple exponential fit: {e}")




    def plot_filtered_data(self, filtered_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()
        for i, col in enumerate(filtered_data.columns):
            try:
                self.ax.plot(self.dataframe.iloc[:, 0], filtered_data[col], label=f'{col} (Filtered)', marker=self.markers[self.marker])
            except Exception as e:
               print(f"Skipping column '{col}' because it could not be plotted: {e}")
        self.custom_plot()

    def plot_spline_fit(self, x_data, y_data, smoothing_factor=0.1):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

                    # Perform Spline fitting
        try:
            spline = UnivariateSpline(x_data, y_data, s=smoothing_factor)
            y_fit = spline(x_data)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Spline Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Spline fit: {e}")

    def plot_lowess_fit(self, x_data, y_data, frac=0.1):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

                    # Perform LOWESS fitting
        try:
            lowess_data = lowess(y_data, x_data, frac=frac)
            x_fit, y_fit = lowess_data[:, 0], lowess_data[:, 1]

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_fit, y_fit, 'r', label='LOWESS Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_fit, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_fit, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting LOWESS fit: {e}")

    def plot_savitzky_golay_fit(self, x_data, y_data, window_length=5, polyorder=2):
        self.figure.clear()
        self.ax = self.figure.add_subplot()

                    # Perform Savitzky-Golay fitting
        try:
            y_fit = savgol_filter(y_data, window_length, polyorder)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Savitzky-Golay Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Savitzky-Golay fit: {e}")


    def plot_weibull_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def weibull_func(x, a, b, c):
                return a * np.exp(-(x / b) ** c)

            initial_guesses = [max(y_data), np.mean(x_data), 1.0]
            popt, pcov = curve_fit(weibull_func, x_data, y_data, p0=initial_guesses)
            a, b, c = popt
            y_fit = weibull_func(x_data, a, b, c)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Weibull Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Weibull fit: {e}")

    def plot_sigmoidal_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def sigmoidal_func(x, a, b, c, d):
                return a / (1 + np.exp(-c * (x - d))) + b

            initial_guesses = [max(y_data), min(y_data), 1.0, np.mean(x_data)]
            popt, pcov = curve_fit(sigmoidal_func, x_data, y_data,maxfev=10000, p0=initial_guesses)
            a, b, c, d = popt
            y_fit = sigmoidal_func(x_data, a, b, c, d)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Sigmoidal Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Sigmoidal fit: {e}")

    def plot_michaelis_menten_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def michaelis_menten_func(x, Vmax, Km):
                return Vmax * x / (Km + x)

            initial_guesses = [max(y_data), np.mean(x_data)]
            popt, pcov = curve_fit(michaelis_menten_func, x_data, y_data, p0=initial_guesses)
            Vmax, Km = popt
            y_fit = michaelis_menten_func(x_data, Vmax, Km)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Michaelis-Menten Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Michaelis-Menten fit: {e}")

    def plot_hill_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def hill_func(x, Vmax, Km, n):
                return Vmax * (x ** n) / ((Km ** n) + (x ** n))

            initial_guesses = [max(y_data), np.mean(x_data), 1.0]
            popt, pcov = curve_fit(hill_func, x_data, y_data, p0=initial_guesses )
            Vmax, Km, n = popt
            y_fit = hill_func(x_data, Vmax, Km, n)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Hill Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Hill fit: {e}")

    def plot_gompertz_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def gompertz_func(x, A, B, C):
                return A * np.exp(-B * np.exp(-C * x))

            initial_guesses = [max(y_data), 1.0, 1.0]
            popt, pcov = curve_fit(gompertz_func, x_data, y_data, p0=initial_guesses)
            A, B, C = popt
            y_fit = gompertz_func(x_data, A, B, C)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Gompertz Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting Gompertz fit: {e}")

    def plot_logarithmic_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            coeffs = np.polyfit(np.log(x_data), y_data, 1)
            a, b = coeffs
            y_fit = a * np.log(x_data) + b

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Logarithmic Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting logarithmic fit: {e}")

    def plot_logistic_fit(self, x_data, y_data):
        self.figure.clear()
        self.ax = self.figure.add_subplot()


        try:
            def logistic_func(x, L, k, x0):
                return L / (1 + np.exp(-k * (x - x0)))

            initial_guesses = [max(y_data), 1.0, np.mean(x_data)]
            popt, pcov = curve_fit(logistic_func, x_data, y_data, p0=initial_guesses)
            L, k, x0 = popt
            y_fit = logistic_func(x_data, L, k, x0)

            self.ax.plot(x_data, y_data, 'bx', label='Data')
            self.ax.plot(x_data, y_fit, 'r', label='Logistic Fit')
            self.custom_plot()
            self.fitted_dataframe = pd.DataFrame({'x': x_data, 'y': y_fit})
            #fitted_data = pd.DataFrame({'x': x_data, 'y': y_fit})
            #self.dataframe = fitted_data

        except Exception as e:
            print(f"Error plotting logistic fit: {e}")


    def plot_linear_fit(self, x_data, y_data, x_fit, y_fit):
        self.ax.clear()
        self.ax.plot(x_data, y_data, 'bx', label='Data')
        self.ax.plot(x_fit, y_fit, 'r', label='linear Curve')


        self.custom_plot()
        self.fitted_dataframe = pd.DataFrame({'x': x_fit, 'y': y_fit})
        #fitted_data = pd.DataFrame({'x': x_fit, 'y': y_fit})
        #self.dataframe = fitted_data


    #refresh


    def custom_plot(self):
        if self.last_marker != self.marker:
            self.last_marker = self.marker
            self.last_plot()
            return 
        self.ax.set_title(self.name, color=self.rev_colors[self.can_color])
        self.ax.set_xlabel(self.xlabel, color=self.rev_colors[self.can_color])
        self.ax.set_ylabel(self.ylabel, color=self.rev_colors[self.can_color])
        if self.last_plot not in [self.to_contour_plot, self.to_contourf_plot]:
            self.ax.legend(loc=self.legend_location, fancybox=True, framealpha=0.85, facecolor=self.fig_colors[self.fig_color], edgecolor=self.rev_colors[self.fig_color]).set_visible(self.legend)
            for text in self.ax.get_legend().get_texts():
                text.set_color(self.rev_colors[self.fig_color])
        if self.grid:
            self.ax.grid(True, color=self.rev_colors[self.fig_color])
        else:
            self.ax.grid(False)
        self.ax.set_facecolor(self.fig_colors[self.fig_color])
        self.figure.set_facecolor(self.fig_colors[self.can_color])
        for spine in self.ax.spines.values():
            spine.set_edgecolor(self.rev_colors[self.can_color])
        self.ax.tick_params(axis='x', labelcolor=self.rev_colors[self.can_color])
        self.ax.tick_params(axis='y', labelcolor=self.rev_colors[self.can_color])
        if self.time_check:
            self.timer.start(self.interval)
        else:
            self.timer.stop()
        self.text = self.figure.text(0.95, 0.95, '', ha='right')
        self.plot_widget.draw()





    #plot types

    def to_plot(self):
        self.figure.clear()
        self.artists.clear()
        self.ax = self.figure.add_subplot()
        for col in self.dataframe.columns[1:]:
            try:
                artist, = self.ax.plot(self.dataframe.iloc[:, 0], self.dataframe[col], label=col, marker=self.markers[self.marker])
                self.artists.append(artist)
            except Exception as e:
                print(f"Skipping column '{col}' because it could not be plotted: {e}")

        if self.typeNum != 0:
            self.typeNum = 0
            self.last_plot = self.to_plot
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.def_vals = [xlim, ylim]

        self.custom_plot()

    def to_pie_chart(self):
        self.figure.clear()
        self.artists.clear()
        self.last_plot = self.to_pie_chart
        self.ax = self.figure.add_subplot()
        data = self.dataframe.iloc[:, 1:].sum()
        artist = self.ax.pie(data, labels=data.index, colors=self.colors, autopct='%1.1f%%')
        self.artists.extend(artist[0])

        if self.typeNum != 1:
            self.typeNum = 1
            self.last_plot = self.to_pie_chart
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.def_vals = [xlim, ylim]

        self.custom_plot()

    def to_bar_chart(self):
        self.figure.clear()
        self.artists.clear()
        self.ax = self.figure.add_subplot()

        num_cols = len(self.dataframe.columns)
        total_width = 0.8  
        width = total_width / num_cols  

        for i, col in enumerate(self.dataframe.columns[1:]):
            data = self.dataframe[col]
            try:
                artist = self.ax.bar(data.index + i * width, data, width=width, label=col)
                self.artists.append(artist)
            except (ValueError, TypeError) as e:
                print(f"Error plotting column '{col}': {e}")


        if self.typeNum != 2:
            self.typeNum = 2
            self.last_plot = self.to_bar_chart
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.def_vals = [xlim, ylim]

        self.custom_plot()

    def to_fill_between(self):
        self.figure.clear()
        self.artists.clear()
        self.ax = self.figure.add_subplot()
        x = np.array(self.dataframe.iloc[:, 0])
        for col in self.dataframe.columns[1:]:
            y = np.array(self.dataframe[col])
            try:
                artist = self.ax.fill_between(x, y, label=col, alpha=0.5, linewidth=0)
                self.artists.append(artist)
            except Exception as e:
                print(f"Skipping column '{col}' because it could not be plotted: {e}")

        if self.typeNum != 3:
            self.typeNum = 3
            self.last_plot = self.to_fill_between
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.def_vals = [xlim, ylim]

        self.custom_plot()

    def to_stack_plot(self):
        self.figure.clear()
        self.artists.clear()
        self.ax = self.figure.add_subplot()

        try:
            artist = self.ax.stackplot(self.dataframe.iloc[:, 0], self.dataframe.iloc[:, 1:].T, labels=self.dataframe.columns[1:], alpha=0.8)
            self.artists.extend(artist)
        except Exception as e:
            print(f"Failed to create stack plot: {e}")


        if self.typeNum != 4:
            self.typeNum = 4
            self.last_plot = self.to_stack_plot
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.def_vals = [xlim, ylim]

        self.custom_plot()


    def to_contour_plot(self):
        self.figure.clear()
        self.artists.clear()
        self.ax = self.figure.add_subplot()

        try:
            artist = self.ax.contour(self.dataframe.iloc[1:, 1:], origin='upper')
            self.artists.extend(artist.collections)
        except Exception as e:
            print(f"Failed to create contour plot: {e}")

        if self.typeNum != 5:
            self.typeNum = 5
            self.last_plot = self.to_contour_plot
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.def_vals = [xlim, ylim]

        self.custom_plot()

    def to_contourf_plot(self):
        self.figure.clear()
        self.artists.clear()
        self.ax = self.figure.add_subplot()

        try:
            artist = self.ax.contourf(self.dataframe.iloc[1:, 1:], origin='upper')
            self.artists.extend(artist.collections)
        except Exception as e:
            print(f"Failed to create contour plot: {e}")

        if self.typeNum != 6:
            self.typeNum = 6
            self.last_plot = self.to_contourf_plot
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.def_vals = [xlim, ylim]

        self.custom_plot()


    def to_scatter_plot(self):
        self.figure.clear()
        self.artists.clear()
        self.ax = self.figure.add_subplot()
        for col in self.dataframe.columns[1:]:
            try:
                marker = self.markers[self.marker] if self.marker != 0 else 'o'
                artist = self.ax.scatter(self.dataframe.iloc[:, 0], self.dataframe[col], label=col, marker = marker)
                self.artists.append(artist)
            except Exception as e:
                print(f"Skipping column '{col}' because it could not be plotted: {e}")

        if self.typeNum != 7:
            self.typeNum = 7
            self.last_plot = self.to_scatter_plot
            xlim = self.ax.get_xlim()
            ylim = self.ax.get_ylim()
            self.def_vals = [xlim, ylim]

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
        

            ## general functions ##

    def complementary_color(self, hex_color):
        if hex_color.startswith('#'):
            hex_color = hex_color[1:]
        comp_hex_color = ''
        for hex in hex_color:
            component = int(hex, 16)
            comp_component = 15 - component
            comp_hex_color += f'{comp_component:1x}'
        
        return f'#{comp_hex_color}'

    def rev_all(self, arr):
        ren = []
        for c in arr:
            ren.append(self.complementary_color(c))
        return ren


    def saveFile(self, filepath, file_format):
        try:
            dataframe_to_save = self.fitted_dataframe if self.fitted_dataframe is not None else self.dataframe
            if file_format == 'csv':
                dataframe_to_save.to_csv(filepath, index=False)
            elif file_format == 'xlsx':
                with pd.ExcelWriter(filepath) as writer:
                    dataframe_to_save.to_excel(writer, index=False)
                #self.dataframe.to_excel(filepath, index=False)
            elif file_format == 'json':
                 dataframe_to_save.to_json(filepath, orient='record')
            else:
                raise ValueError("Unsupported file format. Please select 'csv', 'excel' or 'json'.")
            self.file = filepath
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

    def handle_missing_values(self, df):
        return df.fillna(df.mean())

    def generate_summary_statistics(self, df):
        summary_stats = df.describe().T
        return summary_stats

    def visualize_data_distribution(self, df, output_dir):
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        for column in df.columns:
            plt.figure(figsize=(12, 5))

            plt.subplot(1, 2, 1)
            sns.histplot(df[column], kde=True)
            plt.title(f'Histogram of {column}')

            plt.subplot(1, 2, 2)
            sns.boxplot(x=df[column])
            plt.title(f'Boxplot of {column}')

            plt.tight_layout()
            plt.savefig(f'{output_dir}/{column}_distribution.png')
            plt.close()

    def correlation_analysis(self, df, output_dir):
        corr_matrix = df.corr()

        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f', linewidths=0.5)
        plt.title('Correlation Matrix Heatmap')
        plt.savefig(f'{output_dir}/correlation_matrix.png')
        plt.close()

    def create_html_report(self, summary_stats, output_dir):
        html_report = "<!DOCTYPE html><html><head><title>Data Analysis Report</title></head><body>"

        html_report += "<h2>Summary Statistics</h2>"
        html_report += summary_stats.to_html()

        html_report += "<h2>Data Distribution</h2>"
        for column in summary_stats.index:
            html_report += f"<h3>{column}</h3>"
            html_report += f'<img src="{output_dir}/{column}_distribution.png" alt="{column} distribution">'

        html_report += "<h2>Correlation Matrix</h2>"
        html_report += f'<img src="{output_dir}/correlation_matrix.png" alt="Correlation Matrix">'

        html_report += "</body></html>"

        with open("report.html", "w") as file:
            file.write(html_report)

    def main_summary(self, output_dir):
        df = self.handle_missing_values(self.dataframe)
        summary_stats = self.generate_summary_statistics(df)
        self.visualize_data_distribution(df, output_dir)
        self.correlation_analysis(df, output_dir)
        self.create_html_report(summary_stats, output_dir)

    def package_report(self, file_path, zip_name):
        output_dir = "output"
        self.main_summary(output_dir)
        zip_name+=".zip"
        zip_file_path = os.path.join(file_path, zip_name)
        
        with zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
            if os.path.exists("report.html"):
                zipf.write("report.html", os.path.basename("report.html"))
            
            for root, dirs, files in os.walk(output_dir):
                for file in files:
                    file_path = os.path.join(root, file)
                    zipf.write(file_path, os.path.relpath(file_path, os.path.dirname(output_dir)))
        
        if os.path.exists("report.html"):
            os.remove("report.html")

        for root, dirs, files in os.walk(output_dir):
            for file in files:
                os.remove(os.path.join(root, file))
            for dir in dirs:
                shutil.rmtree(os.path.join(root, dir))

        if os.path.exists(output_dir):
            os.rmdir(output_dir)
    
    def realtime(self):
        if self.file is not None:
            new_time = os.path.getmtime(self.file)
            if(self.last_time != new_time):
                self.last_time = new_time
                self.update_df()

    def update_df(self,table_widget=None):

        if table_widget is not None:
                num_rows = table_widget.rowCount()
                num_cols = table_widget.columnCount()
                data = []
                for row in range(num_rows):
                    row_data = []
                    for col in range(num_cols):
                        item = table_widget.item(row, col)
                        if item is not None:
                            row_data.append(item.text())
                        else:
                            row_data.append(None)
                    data.append(row_data)

                self.dataframe = pd.DataFrame(data[1:], columns=data[0])
        else:
            _, ext = os.path.splitext(self.file)
            supported_formats = ['.csv', '.xlsx', '.json']
            if ext in supported_formats:
                try:
                    if ext == '.csv':
                        self.dataframe = pd.read_csv(self.file)
                    elif ext == '.xlsx':
                        self.dataframe = pd.read_excel(self.file)
                    elif ext == '.json':
                        self.dataframe = pd.read_json(self.file)
                except Exception:
                    pass

        self.last_plot()

    def closePlot(self):
        plt.close(self.figure)

    def add_to_tab_widget(self):
        self.tab_widget.addTab(self, self.name)
        self.tab_widget.setCurrentWidget(self)
