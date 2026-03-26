from markdown_blocks import markdown_to_html_node
from title import extract_title
from copy_dir import write_to_log
from os import(
    path,
    makedirs,
    listdir
)
def generate_page(prefix, from_path, template_path, dest_path):
    if not from_path.endswith(".md"):
        return
    from_path = f"{prefix}{from_path}"
    dest_path = f"{prefix}{dest_path}"
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as md_file:
        md_text = md_file.read()
    with open(template_path) as template_file:
        template = template_file.read()
    node = markdown_to_html_node(md_text)
    html = node.to_html()
    title = extract_title(md_text)
    template = template.replace("{{ Title }}", title)
    template = template.replace("{{ Content }}", html)
    template = template.replace("/href", f"{prefix}href")
    with open(dest_path, "w") as html_file:
        html_file.write(template)
    return

def generate_pages(prefix, from_path, template_path, dest_path):
    list_of_objects = listdir(f"{prefix}{from_path}")
    print(f"LOB: {list_of_objects}")
    for obj in list_of_objects:
        if path.isdir(f"{prefix}{from_path}/{obj}"):
            makedirs(f"{prefix}{dest_path}/{obj}")
            # write_to_log(logfile, f"makedir {dest_path}/{obj}")
            generate_pages(prefix,f"{from_path}/{obj}",f"{template_path}", f"{dest_path}/{obj}")
        else:
            # write_to_log(logfile, f"generate from {from_path}/{obj} to {from_path}/{obj}")
            out_obj=obj.replace(".md", ".html")
            generate_page(prefix, f"{from_path}/{obj}",f"{template_path}",f"{dest_path}/{out_obj}")
    return

#print(getcwd())
#prefix = "/Users/simonv/Documents/GitHub_c-mon71/static_site_generator"
#generate_pages(f"{prefix}/content", f"{prefix}/template.html", f"{prefix}/public")
