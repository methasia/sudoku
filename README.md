# sudoku
a python library that allows translating a sudoku game into an object

# how to use
first, import the library
```py
import sudoku
```

in order to translate a sudoku game into an object, call the `Sudoku` class and pass the game as a list made out of 9 lists which represent the rows of the game

```py
import sudoku

sud = sudoku.Sudoku([[6, 5, 4, None, None, 3, None, None, 9], [3, None, 1, None, None, 9, 4, None, 6], [9, 8, 7, 4, 5, 6, None, 2, None], [2, None, 9, 6, None, 8, 3, 4, None], [5, 4, 3, 9, 1, 2, None, 7, 8], [8, None, None, 3, 4, 5, 9, 1, 2], [None, None, None, None, 6, None, 2, 3, None], [4, 3, None, 8, None, None, 5, 6, 7], [None, None, None, 2, 3, None, None, 9, None]])
```

an empty space can be represented by `None`. this will allow the sudoku to be solved, using the method solve, which returns a list with (hopefully) all solutions to the sudoku

```
print(sud.solve())
```

an object can be translated back into a list using the variable `game`

```
print(sud.game)
```
