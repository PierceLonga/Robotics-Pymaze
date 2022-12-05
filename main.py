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

    # Find the path out of the maze
    pathWithAllCells = r.escape()  # visit all tiles using left wall algorithm
    longArray = pathWithAllCells  # copy of array

    targetIndex = longArray.index((1, 1))
    longArray = longArray[:targetIndex + 1]  # split array after end target

    for x in longArray:
        if longArray.count(x) == 2:  # if item is in list twice
            # get index's of repeat element
            indexPosition = [i for i in range(
                len(longArray)) if longArray[i] == x]
            # remove repeat sections from list
            longArray = longArray[:indexPosition[0] +
                                  1] + longArray[indexPosition[1] + 1:]

    shortestPath = longArray

    pathWithAllCells = [i for i in pathWithAllCells if i != (1, 1)] # To visit all the cells

    a = Robot(m, shape="arrow", footprints=True, color='blue') # Blue arrow for all Cells
    b = Robot(m, shape="square", footprints=True, color='red') # Red Square for Left wall short Path

    m.tracePath({a: pathWithAllCells}, delay=5) # Comment Out To View Shortest Path Only
    m.tracePath({b: shortestPath}, delay=5) # Comment out To view All Cells Only
    m.run() # Leave both Uncommented To run Both Shortest path Red Dot and all Cells Blue Arrow


if __name__ == "__main__":
    main()
