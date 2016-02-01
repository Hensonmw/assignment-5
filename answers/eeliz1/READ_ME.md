# Assigment 5

We're going to be dealing with functions for this assignment.  As with the previous assignment, fork and clone this repository. Then create a directory equivalent to your username in the `answers` directory.  Within your `answers/username` directory, write a program to complete each task, below. Name each of the programs you are writing, according to the "task" (e.g. task1.py). Commit those programs, push them up to your cloned repository, and make a pull request.


## Task 1

This one is pretty simple. Write a program that calls a function that prints "2, 4, 6, 8: Who do we appreciate?" to the screen.  Use the `range()` function to generate the numbers.  **Do not** (!!) use an "ifmain" statement and **do not** use a `main()` function in this program - simply call the function you wrote in the body of the program.

## Task 2

Write a second program that uses the program you wrote for [Task 1](task-1) to demonstrate why I have suggested that you should always use a `main()` function along with the "ifmain" statement.  **Do not** alter your first program.

## Task 3

Now, we are going to play with writing a function that calls some internal Python functions.  Start with `π` (which you can find in the `math` module - no need to define it).  Write a function that accepts `π` as an argument, then prints each of the following: (1) `π` converted to a string, (2) `π` converted to an integer, and (3) `π` rounded to a single decimal place.  Return the unmodified value of `π` and print that, as well.

## Task 4

*e* is a mathematical constant that is sometimes known as [Euler's](https://en.wikipedia.org/wiki/Leonhard_Euler) number (for the history of *e*, see [Wikpedia](https://en.wikipedia.org/wiki/E_(mathematical_constant)).  The value of *e* is **approximately** 2.71828. The reason that *e* is an approximate value is because it is computed as:

![e formula](images/e.png)

So, now the tricky part.  Write a program that includes a function to calculate *e*.  Because *e* is computed as the limit approaches infinity, you probably want to limit the upper range of values you input to the function to something (1000 < *value* <10,000).  Once your function has computed e, return the approximation of *e* to the main loop, and print the approximate value out.

**PS**: There is a way you can compute *e* in a single line (and not just using `math.e`, which is **not** the correct solution - I want you to implement the formula).  Bonus karma if you can figure out how.

## Task 5

Copy the program you wrote for [Task 3](task-3) and save it as `task5.py`.  Modify the function you wrote to take `π` as a **default argument**.  Include in this program the function you wrote to generate *e*.  Call the function that produces `e`, and have it return a value.  Pass that value of `e` to the function where you made `π` the default argument.
