# Pierce-Pymaze
My  pymaze project for Robotics

# Pierce Pymaze Introduction
This is a left hand wall following Python Maze. 
First you must follow the left hand wall of the random maze to map every cell of the Maze
Then you have to find the quickest way from the bottom right start, to the top left end.
I used a blue arrow to map all the cells.
Then I used a red square to show the quickest way out.
This was a hard project to work on. I worked out the left wall following first but it was doubling back so it was not a good path.
I watched so many different tutorials maybe about 100 on how to do mazes, but there was hardly any that showed how to map the left hand wall, so I had to try so many different ways from lots of diffent tutorials and try different  lists, 2D arrays, stacks, popping on and popping off different ways to sort. I learned alot but it too so much time to learn how to do this. 
I tried about 5 differnt versions before I finally got it to work properly and I used alot of the code from the first attempt that only mapped the left wall but doubled back. I used a long array which I learnt in one of the tutorials and had a list of all the cells, the position and where it repeated the position to know the path that was quickest in the end.

# Mapping Every Cell of the Maze


# Tranversal of the Maze


# Usage
When you run the Pymaze the program makes a random 20 X 20 Maze
The first the blue arrow starts at the bottom right of the Maze this is the Start position
The blue arrow follows the left wall and moves forward until there is no left wall then it has to move either turn aound, go up, go down and put the position of the cell into the long array. It doubles back on it self alot and you can see the path because the arrow shows you the direction it has gone, you can track the path.
Then the red square takes the quickest path and this happens very qickly because it dosent repeat any cells.
At the end of the code I give you three options you can either have both the mapping and the traversing happening right after each other so the progam running all the parts of the code. You can comment out if you want to see just the mapping or just the quickest path. I put comments in the code so you would know which one works  depending on what you want to look at. I would never use the Pymaze. I would not like to go in a real maze either because you might gets stuck, but I did learn that if you follow the left hand wall you will find the way out but it could take a very long time.

