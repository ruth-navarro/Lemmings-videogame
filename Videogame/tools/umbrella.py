class Umbrella:
    _cx, _cy = 0, 0  # coordinates of the umbrella
    active = False

    def __init__(self, x, y):
        self._cy = y
        self._cx = x

    def activate(self):
        self.active = True
