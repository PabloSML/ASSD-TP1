import numpy as np
import scipy.signal as ss

class Signal():

    def __init__(self, tValues=None, yValues=None, frequency_hz=None, signal=None):
        if signal is not None:
            self.duplicate_signal(signal)
        else:
            self.tValues = tValues
            self.yValues = yValues
            self.frequency_hz = frequency_hz

    def duplicate_signal(self, target_signal):
        self.tValues = target_signal.tValues.copy()
        self.yValues = target_signal.yValues.copy()
        self.frequency_hz = target_signal.frequency_hz

    def set_point_values(self, new_tValues, new_yValues):
        self.tValues = new_tValues.copy()
        self.yValues = new_yValues.copy()

    def gen_cosine(self, amp, freq_hz, phase=0):

        self.yValues = amp*np.cos(2 * np.pi * freq_hz * self.tValues)
        self.frequency_hz = freq_hz

    def gen_square(self, duty, frec_hz):

        self.yValues = 0.5 * ss.square(2 * np.pi * frec_hz * self.tValues, duty/100) + 0.5
        self.frequency_hz = frec_hz