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
            # out_tValues = input_signal.tValues.copy()
            # out_yValues = input_signal.yValues.copy()

            for t_i in range(0, len(input_signal.tValues)):
                if self.samplingSignal.yValues[t_i] > 0.5:
                    output_signal.yValues[t_i] = input_signal.yValues[t_i]
                else:
                    output_signal.yValues[t_i] = 0

            # output_signal.set_point_values(out_tValues, out_yValues)

        output_signal.analize_fft()
        return output_signal
