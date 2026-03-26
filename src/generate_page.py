from markdown_blocks import markdown_to_html_node
from title import extract_title
from copy_dir import write_to_log
from os import(
    path,
    makedirs,
    listdir,
    getcwd
)
def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md_file:
        md_text = md_file.read()
    with open(template_path) as template_file:
        template = template_file.read()
    node = markdown_to_html_node(md_text)
    html = node.to_html()
    title = extract_title(md_text)
    html_page_title = template.replace("{{ Title }}", title)
    html_page = html_page_title.replace("{{ Content }}", html)
    with open(dest_path, "w") as html_file:
        html_file.write(html_page)
    return

def generate_pages(from_path, template_path, dest_path):
    list_of_objects = listdir(from_path)
    for obj in list_of_objects:
        if path.isdir(f"{from_path}/{obj}"):
            makedirs(f"{dest_path}/{obj}")
            # write_to_log(logfile, f"makedir {dest_path}/{obj}")
            generate_pages(f"{from_path}/{obj}",template_path, f"{dest_path}/{obj}")
        else:
            # write_to_log(logfile, f"generate from {from_path}/{obj} to {from_path}/{obj}")
            generate_page(f"{from_path}/{obj}",template_path,f"{dest_path}/{obj}")
    return

#print(getcwd())
prefix = "C:/Users/svidmar/Lokalni dokumenti/static_site_generator/"
generate_pages(f"{prefix}/content", f"{prefix}/template.html", f"{prefix}/public")
