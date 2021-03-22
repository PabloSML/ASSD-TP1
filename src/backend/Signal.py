

class Signal():

    def __init__(self, tValues=None, yValues=None):
        self.tValues = tValues
        self.yValues = yValues

    def duplicate_signal(self, target_signal):
        self.tValues = target_signal.tValues.copy()
        self.yValues = target_signal.yValues.copy()

    def set_point_values(self, new_tValues, new_yValues):
        self.tValues = new_tValues.copy()
        self.yValues = new_yValues.copy()