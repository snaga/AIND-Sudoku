# Artificial Intelligence Nanodegree
## Introductory Project: Diagonal Sudoku Solver

# Question 1 (Naked Twins)
Q: How do we use constraint propagation to solve the naked twins problem?  
A: First, we search a pair of boxes which have the same 2-possible values (e.g.'23') in the unit. Second, those 2-possible values (e.g. '2' and '3') in the other boxes must be eliminated from the possible values because those two values can be appered only in the pair of boxes. Thus, "constraint" (reduced possibilities) could be propagated to the other boxes by eliminating possible characters with the Naked Twins technique.

# Question 2 (Diagonal Sudoku)
Q: How do we use constraint propagation to solve the diagonal sudoku problem?  
A: The diagonal constraint looks similar to the regular (rows, cols and squares) constraints. Every value can be appeared only once in the unit (a diagonal), so we can eliminate the (possible) value which is already determined in the other boxes in the unit. Thus, eliminating possible values (constraint) in diagonals can be propagated to the other units (rows, cols, squares and another diagonal).

### Install

This project requires **Python 3**.

We recommend students install [Anaconda](https://www.continuum.io/downloads), a pre-packaged Python distribution that contains all of the necessary libraries and software for this project. 
Please try using the environment we provided in the Anaconda lesson of the Nanodegree.

##### Optional: Pygame

Optionally, you can also install pygame if you want to see your visualization. If you've followed our instructions for setting up our conda environment, you should be all set.

If not, please see how to download pygame [here](http://www.pygame.org/download.shtml).

### Code

* `solutions.py` - You'll fill this in as part of your solution.
* `solution_test.py` - Do not modify this. You can test your solution by running `python solution_test.py`.
* `PySudoku.py` - Do not modify this. This is code for visualizing your solution.
* `visualize.py` - Do not modify this. This is code for visualizing your solution.

### Visualizing

To visualize your solution, please only assign values to the values_dict using the ```assign_values``` function provided in solution.py

### Data

The data consists of a text file of diagonal sudokus for you to solve.