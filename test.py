from unittest import TestCase
from main import Robot, maze
class MazeTest(TestCase):

    def setUp(self):
        self.maze = maze()
        self.maze.CreateMaze(loadMaze="04x04.csv")
        self.robot = Robot(self.maze, shape="arrow")
    
    def tearDown(self):
        pass

    def test_start_location(self):
        start = self.robot.position
        self.assertTupleEqual((4, 4), start)

    def test_end_location(self):
        self.robot.escape()
        end = self.robot.position
        self.assertTupleEqual((1, 1), end)
    
    def test_path_correct(self):
        path = self.robot.escape()
        self.assertListEqual(path, [
            (4, 4), (4, 3), (3, 3), (2, 3),
            (2, 2), (3, 2), (3, 1), (4, 1),
            (4, 2), (4, 1), (3, 1), (2, 1),
            (3, 1), (3, 2), (2, 2), (2, 3),
            (3, 3), (4, 3), (4, 4), (3, 4),
            (2, 4), (1, 4), (1, 3), (1, 2),
            (1, 1)
        ])
