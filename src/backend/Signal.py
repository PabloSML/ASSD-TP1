import numpy as np
import scipy.signal as ss
from scipy.fft import fft, fftfreq
import matplotlib.pyplot as plt

class Signal():

    def __init__(self, tValues=None, yValues=None, frequency_hz=None, duty=None, description=None, signal=None):
        if signal is not None:
            self.duplicate_signal(signal)
        else:
            self.tValues = tValues
            self.yValues = yValues
            self.frequency_hz = frequency_hz
            self.duty = duty
            self.description = description

            self.ampValues = None
            self.fValues = None

    def duplicate_signal(self, target_signal):

        self.tValues = target_signal.tValues.copy()
        self.yValues = target_signal.yValues.copy()
        self.frequency_hz = target_signal.frequency_hz
        self.duty = target_signal.duty
        self.description = target_signal.description
        self.ampValues = target_signal.ampValues.copy() if target_signal.ampValues is not None else None
        self.fValues = target_signal.fValues.copy() if target_signal.fValues is not None else None

    def set_time_values(self, new_tValues):
        self.tValues = new_tValues.copy()

    def set_point_values(self, new_tValues, new_yValues):

        self.tValues = new_tValues.copy()
        self.yValues = new_yValues.copy()

    def gen_cosine(self, amp, freq_hz, phase=0):

        self.yValues = amp*np.cos(2 * np.pi * freq_hz * self.tValues + phase)
        self.frequency_hz = freq_hz
        self.description = str(amp) + ".cos(2pi." + str(int(freq_hz)) + "t + " + str(phase) + "rad/s)"

    def gen_square(self, duty, freq_hz):

        self.yValues = 0.5 * ss.square(2 * np.pi * freq_hz * self.tValues, duty/100) + 0.5
        self.frequency_hz = freq_hz
        self.duty = duty
        self.description = "Square wave with frec = " + str(freq_hz) + " and duty = " + str(duty) + "%"

    def analize_fft(self):

        self.ampValues = fft(self.yValues)
        T = np.abs(self.tValues[0] - self.tValues[1])
        N = self.yValues.size
        self.fValues = fftfreq(N, T)[:N // 2]

        # plt.plot(self.fValues, 2.0 / N * np.abs(self.ampValues[0:N // 2]))
        # plt.grid()
        # plt.show()