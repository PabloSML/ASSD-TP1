
class step(object):
    def __init__(self,name='', t=None, y=None, color=None):
        super(step, self).__init__()
        self.name = name
        self.color = color
        self.draw = False
# --------------------------------------------------------------
    def makeMe(self, name, color):
        self.name = name
        self.color = color
        self.draw = False
        self.bypass = False

    def setColor(self, color):
        self.color = color

    def toggleDraw(self):
        self.draw = not self.draw
