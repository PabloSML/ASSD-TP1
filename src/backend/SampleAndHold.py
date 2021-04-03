from src.backend.Signal import Signal
from src.backend.SignalControlled import SignalControlled
import numpy as np

class SampleAndHold(SignalControlled):

    def __init__(self, samplingSignal=None):
        super().__init__(samplingSignal)

    def process_signal(self, input_signal):
        output_signal = Signal()
        output_signal.set_point_values(input_signal.tValues, input_signal.yValues)
        output_signal.description = 'Output Sample and Hold'

        if self.isActive:

            hold_time = 1 / self.samplingSignal.frequency_hz
            step_time = input_signal.tValues[1] - input_signal.tValues[0]

            jump = max(1, int(np.round(hold_time / step_time, 0)))
            output_signal.yValues = \
                np.repeat(output_signal.yValues[::jump], jump)[: output_signal.yValues.size]
            if output_signal.yValues.size < output_signal.tValues.size:
                output_signal.yValues = np.append(output_signal.yValues,
                                                  np.full(output_signal.tValues.size -
                                                          output_signal.yValues.size,
                                                          output_signal.yValues[-1]))

        output_signal.analize_fft()
        return output_signal
