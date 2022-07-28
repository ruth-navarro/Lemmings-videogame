class Ladder:
    _cx, _cy = 0, 0  # coordinates of the ladder
    active = False

    def __init__(self, x: int, y: int):
        self._cy = y
        self._cx = x

    def activate(self):
        self.active = True
