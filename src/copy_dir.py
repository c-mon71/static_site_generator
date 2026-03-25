from os import(
    path,
    listdir,
    mkdir)
from shutil import(
    copy,
    rmtree)
from datetime import datetime

"""Write a recursive function that copies all the contents from a source directory
   to a destination directory (in our case, static to public)
   It should first delete all the contents of the destination directory (public)
   to ensure that the copy is clean.
   It should copy all files and subdirectories, nested files, etc.
   I recommend logging the path of each file you copy, so you can see what's
   happening as you run and debug your code."""

def write_to_log(logfile, log_value):
    logfile.write(f"{datetime.now()} {log_value}\n")

def remove_files_at_dest(dest, logfile):
    if not rmtree(dest):
        write_to_log(logfile, f"Error accesing {dest}.")
        close(logfile)
        raise RuntimeError(f"Error accesing {dest}. Exiting...")
    if not mkdir(dest):
        write_to_log(logfile, f"Error creating {dest}.")
        close(logfile)
        raise RuntimeError(f"Error creating {dest}. Exiting...")
    return 0
    # for file in dest_list_file:
         

def copy_dir(source, destination, logfile):
    f = open(logfile, "a")
    
    if not f:
        raise RuntimeError (f"Problem accessing {logfile}. Exiting...")
    if not path.exists(source):
        write_to_log(f, f"{source} does not exsist")
        f.close()
        raise FileNotFoundError (f"{source} does not exsist. Exiting..." )
    if not path.exists(destination):
        write_to_log(f, f"{source} {destination} does not exsist")
        f.close()
        raise FileNotFoundError(f"{destination} does not exsist. Exiting...")
    
    remove_files_at_dest(destination, logfile)

    return

copy_dir("./static", "./public", "copy_dir.log")