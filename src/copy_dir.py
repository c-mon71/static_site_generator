from os import(
    path,
    listdir,
    mkdir)
from shutil import(
    copy,
    rmtree)

"""Write a recursive function that copies all the contents from a source directory
   to a destination directory (in our case, static to public)
   It should first delete all the contents of the destination directory (public)
   to ensure that the copy is clean.
   It should copy all files and subdirectories, nested files, etc.
   I recommend logging the path of each file you copy, so you can see what's
   happening as you run and debug your code."""


def copy_dir(source, destination, logfile):
    f = open(logfile, "rw+")
    if not f:
        raise RuntimeError (f"Problem accessing {logfile}")
    if not path.exists(source):
        raise FileNotFoundError (f"{source} does not exsist" )
    if not path.exists(destination):
        raise FileNotFoundError(f"{destination} does not exsist")

    return
