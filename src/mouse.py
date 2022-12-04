class Mouse:

    def __init__(self):
        self.x = 0
        self.y = 0
        self.button = None

    def update(self, pos):
        self.x, self.y = pos


