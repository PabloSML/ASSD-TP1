from src.backend.Block import Block
from src.backend.Signal import Signal
import scipy.signal as ss
import numpy as np
import matplotlib.pyplot as plt


class Filter(Block):

    def __init__(self, filterName):
        super().__init__()

        self.filterName = filterName

        self.num = 1  # todo Ver que filtro aplicar
        self.den = 1

        self.filterType = 'lowpass'
        self.filter_order1 = 6
        self.minAttStopBand_dB1 = 53
        self.freqAtFirstMinAttWn1 = 2 * np.pi * 7500
        self.analogFilter = True

        self.num = np.array([0.0517])
        self.den = np.array([1.05271e-43, 4.16957e-38, 1.9946e-32,
                            4.90875e-27, 1.10912e-21, 1.65068e-16, 1.92125e-11, 1.3854e-6, 0.0517])

        # self.num, self.den = ss.cheby2(self.filter_order1, self.minAttStopBand_dB1, self.freqAtFirstMinAttWn1,
        #                                  self.filterType,
        #                                  analog=self.analogFilter)

        self.H = ss.TransferFunction(self.num, self.den)

    def process_signal(self, input_signal):
        output_signal = Signal()
        output_signal.set_point_values(input_signal.tValues, input_signal.yValues)
        output_signal.description = 'Output FAA' if self.filterName is 'FAA' else 'Output FR/Xout'

        if self.isActive:
            output_signal.tValues, output_signal.yValues, dump = ss.lsim(self.H,
                                                      input_signal.yValues, input_signal.tValues)
                                                        # aplica filtro a señal todo transitorio?
            # output_signal.set_point_values(out_tValues, out_yValues)

        output_signal.analize_fft()
        return output_signal
