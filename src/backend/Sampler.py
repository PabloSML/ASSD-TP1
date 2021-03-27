from src.backend.AnalogSwitch import AnalogSwitch
from src.backend.SampleAndHold import SampleAndHold
from src.backend.Filter import Filter
from src.backend.Signal import Signal
import matplotlib.pyplot as plt

class Sampler:

    def __init__(self):
        self.inputSignal = Signal()
        self.samplingSignal = Signal()
        self.analogSwitch = AnalogSwitch()
        self.sampleAndHold = SampleAndHold()
        self.antiAliasFilter = Filter()
        self.recoveryFilter = Filter()
        self.blockChain = [self.antiAliasFilter, self.analogSwitch, self.sampleAndHold, self.recoveryFilter]
        self.nodeList = [None, None, None, None, None]


    def toggle_FAA_active(self):
        self.antiAliasFilter.toggle_active()
        self.activate_awesome_magical_signal_processing()

    def toggle_switch_active(self):
        self.analogSwitch.toggle_active()
        self.activate_awesome_magical_signal_processing(skip_to_block=1)

    def toggle_sh_active(self):
        self.sampleAndHold.toggle_active()
        self.activate_awesome_magical_signal_processing(skip_to_block=2)

    def toggle_recov_active(self):
        self.recoveryFilter.toggle_active()
        self.activate_awesome_magical_signal_processing(skip_to_block=3)

    def set_input_signal(self, input_signal):
        if input_signal is not None:
            self.inputSignal.duplicate_signal(input_signal)
            self.nodeList[0] = self.inputSignal

    def set_sampling_signal(self, sampling_signal):
        if sampling_signal is not None:
            self.samplingSignal.duplicate_signal(sampling_signal)
            self.analogSwitch.set_sampling_signal(self.samplingSignal)
            self.sampleAndHold.set_sampling_signal(self.samplingSignal)

    def activate_awesome_magical_signal_processing(self, skip_to_block=0):
        for index in range(0 + skip_to_block, len(self.blockChain)):
            self.nodeList[index+1] = self.blockChain[index].process_signal(self.nodeList[index])

        # for node in self.nodeList:
        #     plt.plot(node.tValues, node.yValues)
        #     plt.axis([1, 1+5e-4, -10, 10])
        # plt.show()


