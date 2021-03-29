
class plot_list_specs(object):
    def __init__(self):
        super(plot_list_specs, self).__init__()
        self.all_together = [['Xin', None, False],['FAA', None, False],['SH', None, False],['LA', None, False],['FR', None, False]] #[Nombre,color,draw]
# --------------------------------------------------------------
    def setColor(self, who, color):
        for i in range(len(self.all_together)):
            if who == self.all_together[i][0]:
                self.all_together[i][1] = color

    def toggleDraw(self,who):
        for i in range(len(self.all_together)):
            if who == self.all_together[i][0]:
                self.all_together[i][2] = not self.all_together[i][2]
