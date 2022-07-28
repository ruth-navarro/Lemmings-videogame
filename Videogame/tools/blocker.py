class Blocker:
    _cx, _cy = 0, 0  # coordinates of the blocker
    active = False
    def __init__(self, x, y):
        self._cy = y
        self._cx = x
    def activate(self):
        self.active = True
