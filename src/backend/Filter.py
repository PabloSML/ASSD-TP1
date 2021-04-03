from src.backend.Block import Block
from src.backend.Signal import Signal
import numpy as np



class Filter(Block):

    def __init__(self, filterName):
        super().__init__()

        self.filterName = filterName

        # self.num_coefs = np.array([1])
        self.den_coefs = np.array([6.76557460457869e-48, 3.32746503042674e-42, 1.76054639575565e-36,
                             5.27229824209111e-31, 1.39076912014791e-25, 2.60148265256641e-20,
                             3.89149907555e-15, 4.0930562e-10, 2.8835e-05, 1])

        # self.num_poly = np.poly1d(self.num_coefs)
        self.den_poly = np.poly1d(self.den_coefs)

    def process_signal(self, input_signal):
        output_signal = Signal()
        output_signal.set_point_values(input_signal.tValues, input_signal.yValues)
        output_signal.set_spectral_values(input_signal.fValues, input_signal.ampValues)
        output_signal.description = 'Output FAA' if self.filterName == 'FAA' else 'Output FR/Xout'

        if self.isActive:

            transf_values = 1.0 / self.den_poly(1j*2*np.pi*input_signal.fValues)
            output_signal.ampValues = input_signal.ampValues * transf_values

        output_signal.analize_ifft()
        return output_signal
