# First Attempt

from pyamaze import agent, maze


class Robot(agent): # this Traces The path of the Cells

    def look(self, direction):
        while (direction != self._orient):
            self._RCW()

    def turnLeft(self): #check left wall first
        direction = (self._orient - 1) % 4
        self.look(direction)

    def turnBack(self): # turn back when there is nowhere to go
        self.turnLeft()
        self.turnLeft()

    def turnRight(self):
        self.turnBack()
        self.turnLeft()

    def forward(self): # Move Forward
        if self.blocked:
            raise Exception("Can't drive into a wall") # Can't drive into a wall
        [
            self.moveUp,  # Ways To go
            self.moveRight,
            self.moveDown,
            self.moveLeft
        ][self._orient](None)

    @property
    def walls(self):
        return self._parentMaze.maze_map[self.position]

    @property
    def blocked(self): # Directions
        facing = ["N", "E", "S", "W", "NW", "NE", "SE", "SW"][self._orient]
        return self.walls[facing] == 0

    def navigate(self): # How To Move Around
        self.turnLeft()
        while self.blocked:
            self.turnRight()
        self.forward()

    def escape(self): # Navigates Around
        path = [self.position]
        self.navigate()
        path.append(self.position)
        while self.position != (20, 20): # Gets Position
            self.navigate()
            path.append(self.position)
        return path


def main():

    # Create maze and robot
    m = maze(20, 20)
    m.CreateMaze(loadMaze="20x20.csv")
    r = Robot(m, shape="arrow")

   
if __name__ == "__main__":
    main()
