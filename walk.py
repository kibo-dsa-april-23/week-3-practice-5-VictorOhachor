from os import listdir
from os.path import isdir, join


def walk_directory(d, indent):
    # Implement recursive directory walk here
    for f in listdir(d):
        # print directory's content
        print(' ' * indent,
              '|__' if indent else '--', f)

        # get file path
        f_path = join(d, f)
        # recursively walk dir
        if isdir(f_path):
            walk_directory(f_path, indent + 2)


# '.' means current directory
walk_directory('Desktop', 0)
