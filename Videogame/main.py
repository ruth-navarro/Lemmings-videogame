import pyxel
from random import randint
from graphical_interface.cell import Cell
from graphical_interface.gates import Gates
from graphical_interface.platforms import Platforms
from graphical_interface.scores import Scores
from sprite.lemming import Lemming
from tools.blocker import Blocker
from tools.ladder import Ladder
from tools.umbrella import Umbrella

class Game:
    # x, y = 0, 0
    # z = Cell
    first = True
    cx, cy = 128, 128
    coordx, coordy = 0, 32  # These are the coordinates to move on the board
    WIDTH, HEIGHT = 256, 256  # The size of the board
    CONSTANT = 16
    row = int(WIDTH / CONSTANT)  # number of rows
    column = int((HEIGHT - 32) / CONSTANT)  # number of columns
    grid = []
    color = 12
    tools = []  # Empty list filled with lists where all the tools are
    umbrella = []  # empty list that will be filled with 5 umbrella objects
    blockers = []  # empty list that will be filled with 5 blockers objects
    ladders = []  # empty list that will be filled with 6 ladders objects (Right and Left)
    lemmings = []  # empty list where all the lemmings will be. Cambiar nombre lemmings_alive
    platforms = []
    gates = []
    MAX_LEMMINGS = randint(10, 20)
    MIERDA = MAX_LEMMINGS
    lemmings_dead = []
    scores = Scores(1, 0, 0, 0, 5, 15, 7)

    def __init__(self):
        pyxel.init(self.WIDTH, self.HEIGHT, caption="Pyxel Lemmings")
        for i in range(self.row):
            self.grid.append([])
            for j in range(self.column):  # coordinates for the board
                cell = Cell(i, j)
                self.grid[i].append(cell)
        pyxel.load(
            "assets\lemmingsVisuals.pyxres")  # We upload the file where all the images are (umbrellas, blockers, lemmings,
        images = pyxel.load("assets\lemmingsVisuals.pyxres")  # ladders and the images of the platforms

        pyxel.run(self.update, self.draw)

    def exist_floor(self,
                    lemming):  # This method detects if the coordinates of the lemming coincide with the coordinaates of the platform
        for floor in self.platforms:
            if lemming.y + 16 == floor._cy:
                if lemming.x not in range(floor._cx - 8, floor._cx + floor.width - 6):
                    lemming.fall()
                else:
                    lemming.notfalling()


def tool(self, lemming):  # This method activates the tools

    for blocker in self.blockers:
        if lemming.x == blocker._cx and lemming.y == blocker._cy:
            lemming.changedirection()
            blocker.active()
    for umbrella in self.umbrella:
        if lemming.x == umbrella._cx and lemming.y == umbrella._cy:
            lemming.tool()
            umbrella.activate()
    for ladder in self.ladders:
        if lemming.x == ladder._cx and lemming._cy == ladder._cy:
            ladder.active()


def check_tool(self, tool_placed, tool_type):
    if tool_type == "umbrella":
        tool_list = self.umbrella
    elif tool_type == "blocker":
        tool_list = self.blockers
    elif tool_type == "ladder":
        tool_list = self.ladders
    for e in tool_list:
        if tool_placed._cx == e._cx and tool_placed._cy == e._cy and e.active == False:
            del (tool_list[tool_list.index(e)])
            return None
    tool_list.append(tool_placed)
    return False


def update(self):
    if pyxel.btnp(pyxel.KEY_Q):
        pyxel.quit()
    # Move the cursor on the board
    if pyxel.btnp(pyxel.KEY_RIGHT):
        if self.coordx + 16 <= self.WIDTH - 16:
            self.coordx += 16
    if pyxel.btnp(pyxel.KEY_LEFT):
        if self.coordx - 16 >= 0:
            self.coordx -= 16

    if pyxel.btnp(pyxel.KEY_UP):
        if self.coordy - 16 >= 32:
            self.coordy -= 16
    if pyxel.btnp(pyxel.KEY_DOWN):
        if self.coordy + 16 <= self.HEIGHT - 16:
            self.coordy += 16
    if pyxel.btnp(pyxel.KEY_SPACE):
        row = int(self.coordy / 16)
        col = int(self.coordx / 16)

    # Tools

    # Stores the position where the user press the corresponding key to use a tool. The position is the same
    # as the one of the cursor
    if pyxel.btnp(pyxel.KEY_ENTER) and len(self.umbrella) < 5:
        umbrella_tool = Umbrella(self.coordx, self.coordy)
        self.check_tool(umbrella_tool, "umbrella")

    if pyxel.btnp(pyxel.KEY_R) and len(self.ladders) < 15:
        ladder_tool = Ladder(self.coordx, self.coordy)
        self.check_tool(ladder_tool, "ladder")  # ladder
    if pyxel.btnp(pyxel.KEY_B) and len(self.blockers) < 7:
        blocker_tool = Blocker(self.coordx, self.coordy)
        self.check_tool(blocker_tool, "blocker")  # blocker

    # Platforms#
    for i in range(0, 7):
        var_x = randint(0, 11) * 16
        floor = Platforms(var_x, (15 - (2 * i)) * 16, randint(5, 10))

        if len(self.platforms) < 7:
            self.platforms.append(floor)
    # Gates:
    StartGate = Gates(self.platforms[0]._cx + 16, self.platforms[0]._cy - 16, "start")
    EndGate = Gates(self.platforms[6]._cx + 16, self.platforms[6]._cy - 16, "end")
    while len(self.gates) < 2:
        self.gates.append(StartGate)
        self.gates.append(EndGate)

    # Lemmings
    if pyxel.frame_count % 30 == 0:
        if self.MAX_LEMMINGS > 0:
            lemming = Lemming(self.platforms[6]._cx + 16, self.platforms[6]._cy - 16,
                              True)  # create a variable with the attributes of the class Lemming
            self.lemmings.append(lemming)  # append 3 lemmings into the empty list lemmings
            self.MAX_LEMMINGS -= 1
            # self.scores.addlemming_alive(lemmings)
    # The movement of the lemmings
    for lemming in self.lemmings:
        if lemming.alive == True:
            self.exist_floor(lemming)
            self.tool(lemming)
            lemming.movement()
            if lemming.direction == True and lemming.x + 16 > self.WIDTH:  # if the x coordinate of the lemming is bigger than
                lemming.changedirection()  # the width of the board it changes direction
            elif lemming.x < 0:  # if the coordinate of the lemmings is smaller than 0, it changes direction
                lemming.changedirection()
        else:
            aux_var = lemming
            self.lemmings.remove(lemming)
            self.lemmings_dead.append(aux_var)

    self.scores.addlemming_alive(self.lemmings)


def draw(self):
    pyxel.cls(self.color)
    # pyxel.blt(1, 120, 0, 0, 0, 16, 16, 0) "umbrellas draw"
    # pyxel.blt(1, 140, 0, 0, 0, 16, 16, 1)
    # Text with the scores
    pyxel.text(10, 10, "Level: 0", 7)
    pyxel.text(70, 10, ("Alive: " + str(self.scores.alive)), 7)
    pyxel.text(120, 10, "Saved: 0", 7)
    pyxel.text(200, 10, ("Died: " + str(len(self.lemmings_dead))), 7)
    pyxel.text(10, 25, ("Umbrellas: " + str(len(self.umbrella))), 7)
    pyxel.text(70, 25, "Ladders: 0", 7)
    pyxel.text(120, 25, "Blockers: 0", 7)
    pyxel.blt(self.coordx, self.coordy, 0, 16, 32, 16, 16, 0)
    # pyxel.blt(120, 140, 0, 48, 0, 16, 16, 0)  # The drawing of a single lemming
    #     pyxel.blt(self.coordx, self.coordy, 0, 0, 0, 16, 16, 1)

    # Drawing the tools on the board
    for umbrella in self.umbrella:
        pyxel.blt(umbrella._cx, umbrella._cy, 0, 0, 0, 16, 16, 0)
    for ladder in self.ladders:
        pyxel.blt(ladder._cx, ladder._cy, 0, 32, 0, 16, 16, 0)
    for blocker in self.blockers:
        pyxel.blt(blocker._cx, blocker._cy, 0, 16, 0, 16, 16, 0)

    # Drawing the lemmings on the board
    for lemming in self.lemmings:
        pyxel.blt(lemming.x, lemming.y, *lemming.image)
    for lemming in self.lemmings_dead:
        pyxel.blt(lemming.x, lemming.y, *lemming.image)  # drawing of the list lemmings
    # Drawing the platforms
    for floor in self.platforms:
        for mandarina in range(0, floor.width, 16):
            pyxel.blt(floor._cx + mandarina, floor._cy, 0, 0, 16, 16, 16, 0)
    # draw gates:
    for gate in self.gates:
        pyxel.blt(gate._cx, gate._cy, *gate.image)

    # Drawing of the board
    for i in range(self.row):
        for j in range(self.column):
            cell = self.grid[i][j]


Game()
