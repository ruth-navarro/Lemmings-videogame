# Lemmings-videogame

This version of the Lemmings videogame is made with pyxel. The goal of this project is practice with Object Oriented Programming.
The work has been divided in the following steps:

  1) Objects and graphical interface. Creating a class for each of the game elements, generating the board (lemmings, tools, platforms and scores indicating the lemmings that are alive
and dead.

  2) Basic lemming movement and tools placement. Make a single lemming go out from the entry door and move right or left considering the borders of the board and the possible obstacles. If it finds an obstacle it will change direction. The movement of the lemming will be continuous. If the lemming falls at the end of a platform, it will automatically die, no matter the height it falls from. Use of the keyboard to place the tools: right or left ladders,
umbrellas to avoid dying when falling or blockers to chang the movement direction. To place a tool, the arrow keys will be used to select the cell and and
another key will be used to place each type of tool. 

  3) Using ladders and umbrellas. Once a first lemming reaches a cell where a ladder/umbrella has been placed the tool will be activated. In the case of ladders, they will be automatically drawn. A ladder can only occupy a single cell, but many ladders can be placed to allow lemming to reach higher platforms. Umbrellas will avoid lemmings dying when falling. A cell can only contain a tool. If a new tool is placed, the old one will be removed, but if a ladder has been constructed it cannot be removed. Allow lemmings to go up and down ladders and to fall slowly using umbrellas.
  
  4) Basic game. Activate blockers: once a first lemming reaches a cell where a blocker is placed it will stand, acting as an obstacle. The remaining lemmings will bound on it and change their direction. Implement the basic game: a random number of 10 to 20 lemmings appear and move. If a lemming falls with no umbrella it will die, updating the counters. If a lemming reaches a non-built ladder it will build it step by step (unlike in the previous step); the ladder cannot be used until it is totally built. Every time a lemming reaches the exit door it will be removed from the
game and the scores updated accordingly. Implement the movement animations and the ladder building ones. The number of available tools will be limited to enforce the user to follow a solving strategy.
