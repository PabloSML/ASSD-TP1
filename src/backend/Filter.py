from src.backend.Block import Block
from src.backend.Signal import Signal
import scipy.signal as ss


class Filter(Block):

    def __init__(self):
        super().__init__()

        self.num = None  # todo Ver que filtro aplicar
        self.den = None

    def process_signal(self, input_signal):
        output_signal = Signal()
        output_signal.duplicate_signal(input_signal)

        if self.isActive:
            out_tValues, out_yValues, dump = ss.lsim((self.num, self.den),
                                                      input_signal.yValues, input_signal.tValues)
                                                        # aplica filtro a señal todo transitorio?
            output_signal.set_point_values(out_tValues, out_yValues)

        return output_signal
