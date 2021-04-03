from src.backend.Signal import Signal
from src.backend.SignalControlled import SignalControlled

class AnalogSwitch(SignalControlled):

    def __init__(self, samplingSignal=None):
        super().__init__(samplingSignal)

    def process_signal(self, input_signal):
        output_signal = Signal()
        output_signal.set_point_values(input_signal.tValues, input_signal.yValues)
        output_signal.description = 'Output Llave Analogica'

        if self.isActive:
            output_signal.yValues = input_signal.yValues * self.samplingSignal.yValues

        output_signal.analize_fft()
        return output_signal
