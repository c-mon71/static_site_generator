#from src.textnode import TextNode
from copy_dir import copy_dir
from generate_page import generate_pages

def main():
    prefix = "/Users/simonv/Documents/GitHub_c-mon71/static_site_generator"
    copy_dir(f"{prefix}/static", f"{prefix}/public", "copy_dir.log")
    generate_pages("content", "template.html", "public")

if __name__ == "__main__":
    main()

