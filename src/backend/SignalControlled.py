from src.backend.Block import Block
from src.backend.Signal import Signal

class SignalControlled(Block):

    def __init__(self, samplingSignal=None):
        super().__init__()
        self.samplingSignal = Signal()
        if samplingSignal is not None:
            self.set_sampling_signal(samplingSignal)

    def set_sampling_signal(self, newSignal):
        self.samplingSignal.duplicate_signal(newSignal)