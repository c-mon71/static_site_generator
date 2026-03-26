#from src.textnode import TextNode
import sys
from os import getcwd

from copy_dir import copy_dir
from generate_page import generate_pages

def main():
    if len(sys.argv) > 1:
        prefix = "."+sys.argv[1]
    else:
        prefix = "./"
    print(f"prefix: {prefix}")
    #prefix = "/Users/simonv/Documents/GitHub_c-mon71/static_site_generator"
    copy_dir(f"{prefix}static", f"{prefix}docs", "copy_dir.log")
    generate_pages(prefix, "content", "template.html", "docs")

if __name__ == "__main__":
    main()

