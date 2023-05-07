# Recursive Directory Walk

In this exercise, you will use recursion to do a recursive traversal of a directory (computer folder) structure.

## Your Task

In `walk.py`, you will find the function `walk_directory()`, which should print a directory structure indented by spaces as appropriate to denote the levels of directories. See the below section for some sample output.

`walk_directory()` takes two parameters:

* `d`, which represents the directory we would like to recursively print.
* `indent`, a string that holds some number of spaces that represent the current level of indentation.

You should implement the rest of `walk_directory` to do the following:

* Print the name of each file in `d`.
* For any subdirectories in `d`, recursively print the contents of those subdirectories.

The program should continue recursively printing subdirectories until all files and directories are printed.

Here are some tips to help you implement this function:

* `listdir(d)` will return a list of all files and directories in `d`. The code should iterate over this list: `for f in listdir(d)`.
* You should never refer to the file `f` by itself -- you should always refer to it with its directory prefix `d`. You can do so using `join(d, f)`. This means that if `f` is `example.txt` and `d` is `Desktop/Documents`, then `join(d, f)` will be `Desktop/Documents/example.txt`.
* You can check whether any file `f` is actually a directory (that needs to be recursively printed) using `isdir(join(d, f))`.
* Every time you make a recursive call, you should increase the level of indentation. You can double the length of the existing indentation by using the `*` operator: `2 * indent`. If `indent` is `' '` (one space), then `2 * indent` will be `'  '` (two spaces).

## Testing

There is a sample call to `walk_directory()` at the bottom of `walk.py`. This sample call asks to walk the given `Desktop` directory with an initial indentation of one space (`' '`).

The output should look like the following:

```
 Documents
  taxes.docx
  Budgets
    FY2020.xlsx
    FY2022.xlsx
 Classes
  data-structures
    interview-notes.docx
    notes-week1.docx
  programming-1
    notes.docx
    homework.pdf
 Downloads
  cat_skateboarding.gif
 Pictures
  signature.jpg
  portrait.png
```
