from src.backend.Block import Block
from src.backend.Signal import Signal
import scipy.signal as ss
import numpy as np


class Filter(Block):

    def __init__(self, filterName):
        super().__init__()

        self.filterName = filterName

        # self.num = 1  # todo Ver que filtro aplicar
        # self.den = 1

        # self.filterType = 'lowpass'
        # self.filter_order1 = 6
        # self.minAttStopBand_dB1 = 53
        # self.freqAtFirstMinAttWn1 = 2 * np.pi * 7500
        # self.analogFilter = True

        self.num = np.array([1])
        self.den = np.array([6.76557460457869e-48, 3.32746503042674e-42, 1.76054639575565e-36,
                             5.27229824209111e-31, 1.39076912014791e-25, 2.60148265256641e-20,
                             3.89149907555e-15, 4.0930562e-10, 2.8835e-05, 1])

        # self.num, self.den = ss.cheby2(self.filter_order1, self.minAttStopBand_dB1, self.freqAtFirstMinAttWn1,
        #                                  self.filterType,
        #                                  analog=self.analogFilter)

        self.H = ss.TransferFunction(self.num, self.den)

    def process_signal(self, input_signal):
        output_signal = Signal()
        output_signal.set_point_values(input_signal.tValues, input_signal.yValues)
        # output_signal.set_spectral_values(input_signal.fValues, input_signal.ampValues)
        output_signal.description = 'Output FAA' if self.filterName == 'FAA' else 'Output FR/Xout'

        if self.isActive:
            output_signal.tValues, output_signal.yValues, dump = ss.lsim(self.H,
                                                      input_signal.yValues, input_signal.tValues)
                                                        # aplica filtro a señal todo transitorio?
            # output_signal.cut_first_period()
            # output_signal.set_point_values(out_tValues, out_yValues)

        output_signal.analize_fft()
        return output_signal
