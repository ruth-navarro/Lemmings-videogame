class Lemming:  # add an image attribute
    __cx, __cy = 0, 48
    life: bool
    direction = True
    alive: bool = True
    lemming_tool = False
    # ascending: bool
    falling: bool = False
    image: tuple = (0, 48, 0, 16, 16, 0)

    def __init__(self, x, y, direction):
        self.__cx = x
        self.__cy = y
        self.__direction = direction

    @property
    def x(self):
        return self.__cx

    @x.setter
    def x(self, value):
        self.__cx = value

    @property
    def y(self):
        return self.__cy

    @y.setter
    def y(self, value):
        self.__cy = value

    @property
    def direction(self):
        return self.__direction

    @direction.setter
    def direction(self, value):
        self.__direction = value

    def fall(self):
        self.falling = True

    def movement(self):
        if self.falling == False:
            if self.direction == True:
                self.__cx += 1
            elif self.direction == False:
                self.__cx -= 1
        else:
            self.__cy += 1

    def tool(self):
        self.lemming_tool = True

    def fall(self):
        self.falling = True

    def notfalling(self):
        if self.falling == True and self.lemming_tool == False:
            self.alive = False
            self.image = (0, 48, 16, 16, 16, 0)
        elif self.falling == True and self.lemming_tool == True:
            self.lemming_tool = False
        self.falling = False

    def changedirection(self):
        if self.direction == True:
            self.direction = False
        elif self.direction == False:
            self.direction = True
