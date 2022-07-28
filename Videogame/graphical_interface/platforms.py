class Platforms:
    _cx, _cy = 0, 48
    width = 5

    def __init__(self, x, y, width):
        if x in range(0, 256):
            self._cx = x
        else:
            self.cx = 0
        if y in range(48, 256):
            self._cy = y
        else:
            self._cy = 0
        if width >= 5 and width <= 10:
            self.width = 16 * width
        else:
            self.width = 80
