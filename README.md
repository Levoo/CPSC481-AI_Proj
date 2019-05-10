# CPSC481-AI_Proj
<<<<<<< HEAD
A project that will incorporate a genetic algorithm in order for a object to traverse a maze.
=======
PSEUDO-GENETIC MAZE NAVIGATOR
by Fernando Cuevas, Arnold Ruiz, Alex Ma, Ye-Rham Hwang
External libraries used: pygame
A project that will incorporate a genetic algorithm in order for a object to traverse a maze.

=============================================================================================
>>>>>>> traversal

Requirments:
python 3.6.8 (https://www.python.org/downloads/release/python-368/)

GUI: pygames (https://pypi.org/project/Pygame/)
pip install pygame

=======================================================

HOW TO:
1. Extract all the files into a folder location.

2. With a python scripter, run the "Maze.py" script to execute the program.

3. Once the program executes, a window should pop up with the title "PSEUDO-GENETIC MAZE NAVIGATOR", 
   a "Generations" panel with a + and - button, a start button, and a quit button.
	a. Clicking the + button will increase the generations of candidates, the - button will decrease it at a minimum of 1 generation.
	b. Clicking the start button will begin the process of creating generations of candidates and having them navigate the maze. 
	   (The process of maze navigating can only be exited by using the quit button on the program window.)
	c. Clicking the quit button will exit the program.

4. During the process of maze navigation, on the left will appear the maze, with candidates navigating the maze. 
   Below the maze is the current generation count. To the right of the generation count is a display of what parents will be used for the next generation.
   To the right of the maze is a display of candidates running through the maze, with the weights of each candidate displayed next to them.
   The process of maze navigation will continue until the number of generations created have been met.
