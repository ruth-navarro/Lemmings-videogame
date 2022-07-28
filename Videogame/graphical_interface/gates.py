class Gates:
    _cx,_cy = 0, 0
    image : tuple
    def __init__(self,x : int ,y : int,type : str):
        self._cx = x
        self._cy = y
        self.type = type
        if type == "end":
            self.image = (0, 16, 16, 16, 16, 0) #puerta azul (final)
        else:
            self.image = (0, 32, 16, 16, 16, 0) #puerta verde (start)
