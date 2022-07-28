class Scores:
    __level, __alive, __save = 1, 0, 0
    __dead, __umbrellas, __ladders, __blockers = 0, 0, 0, 0

    def __init__(self, level, alive, save, dead, umbrellas, ladders, blockers):
        self.__level = level
        self.__alive = alive
        self.__save = save
        self.__dead = dead
        self.__umbrellas = umbrellas
        self.__ladders = ladders
        self.__blockers = blockers

    @property
    def level(self):
        return self.__level

    @level.setter
    def level(self, value):
        self.__alive = value

    @property
    def alive(self):
        return self.__alive

    @alive.setter
    def alive(self, value):
        self.__alive = value

    def addlemming_alive(self, lemming_list):
        self.__alive = len(lemming_list)

