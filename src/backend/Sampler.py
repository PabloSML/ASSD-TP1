from src.backend.AnalogSwitch import AnalogSwitch
from src.backend.SampleAndHold import SampleAndHold
from src.backend.Filter import Filter
from src.backend.Signal import Signal

class Sampler:

    def __init__(self):
        self.inputSignal = Signal()
        self.samplingSignal = Signal()
        self.analogSwitch = AnalogSwitch()
        self.sampleAndHold = SampleAndHold()
        self.antiAliasFilter = Filter()
        self.recoveryFilter = Filter()
        self.blockChain = [self.analogSwitch, self.sampleAndHold, self.antiAliasFilter, self.recoveryFilter]
        self.nodeList = [None, None, None, None, None]

    def set_input_signal(self, input_signal):
        if input_signal is not None:
            self.inputSignal.duplicate_signal(input_signal)
            self.nodeList[0] = self.inputSignal

    def set_sampling_signal(self, sampling_signal):
        if sampling_signal is not None:
            self.samplingSignal.duplicate_signal(sampling_signal)
            self.analogSwitch.set_sampling_signal(self.samplingSignal)
            self.sampleAndHold.set_sampling_signal(self.samplingSignal)

    def activate_awesome_magical_signal_processing(self):
        for index in range(0, len(self.blockChain)):
            self.nodeList[index+1] = self.blockChain[index].process_signal(self.nodeList[index])
