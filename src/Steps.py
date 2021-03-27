
class step(object):
    def __init__(self,name='', t=None, y=None, color=None):
        super(step, self).__init__()
        self.name = name
        self.t = t
        self.y = y
        self.color = color
        self.draw = False
        self.bypass = False
# --------------------------------------------------------------
    def makeMe(self, name, t, y, color):
        self.name = name
        self.t = t
        self.y = y
        self.color = color
        self.draw = False
        self.bypass = False

    def setColor(self, color):
        self.color = color

    def toggleDraw(self):
        self.draw = not self.draw

    def toggleBypass(self):
        self.bypass = not self.bypass