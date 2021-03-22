

class Block:
    def __init__(self):
        self.isActive = True

    def toggle_active(self):
        self.isActive = not self.isActive