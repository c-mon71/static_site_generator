from os import(
    path,
    listdir,
    makedirs)
import shutil
from datetime import datetime
import time

"""Write a recursive function that copies all the contents from a source directory
   to a destination directory (in our case, static to public)
   It should first delete all the contents of the destination directory (public)
   to ensure that the copy is clean.
   It should copy all files and subdirectories, nested files, etc.
   I recommend logging the path of each file you copy, so you can see what's
   happening as you run and debug your code."""

def write_to_log(logfile, log_value):
    logfile.write(f"{datetime.now()} {log_value}\n")
    logfile.flush()

def remove_files_at_dest(dest, logfile):
    if path.exists(dest):
        try:
            shutil.rmtree(dest)
            # Give Windows a tiny moment to actually release the directory handle
            write_to_log(logfile, f"Deleted existing directory {dest} successfully.")
            time.sleep(0.1) 
        except Exception as e:
            write_to_log(logfile, f"Error deleting {dest}: {e}")
            raise RuntimeError(f"Could not remove existing directory {dest}")

    try:
        makedirs(dest, exist_ok=True)
        write_to_log(logfile, f"Created directory {dest} successfully.")
    except Exception as e:
        write_to_log(logfile, f"Error creating {dest}: {e}")
        # Make sure to close your logfile before crashing!
        raise RuntimeError(f"Error creating {dest}. Exiting...")
    
    return 0  

def copy_files_to_dest(src, dest, logfile):
    list_of_objects = listdir(src)
    for obj in list_of_objects:
        if path.isdir(f"{src}/{obj}"):
            makedirs(f"{dest}/{obj}")
            write_to_log(logfile, f"makedir {dest}/{obj}")
            copy_files_to_dest(f"{src}/{obj}",f"{dest}/{obj}", logfile )
        else:
            write_to_log(logfile, f"copy from {src}/{obj} to {dest}/{obj}")
            shutil.copy(f"{src}/{obj}",f"{dest}/{obj}")

def copy_dir(source, destination, logfile):
    with open("copy_dir.log", "a") as f:
    
        if not f:
            raise RuntimeError (f"Problem accessing {logfile}. Exiting...")
        if not path.exists(source):
            write_to_log(f, f"{source} does not exist")
            raise FileNotFoundError (f"{source} does not exist. Exiting..." )
        if not path.exists(destination):
            write_to_log(f, f"{source} {destination} does not exist")
            raise FileNotFoundError(f"{destination} does not exist. Exiting...")
        
        remove_files_at_dest(destination, f)
        copy_files_to_dest(source, destination, f)

    return
