import re

from src.textnode import TextNode, TextType

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
        split_nodes = []
        sections = old_node.text.split(delimiter)
        if len(sections) % 2 == 0:
            raise ValueError("invalid markdown, formatted section not closed")
        for i in range(len(sections)):
            if sections[i] == "":
                continue
            if i % 2 == 0:
                split_nodes.append(TextNode(sections[i], TextType.TEXT))
            else:
                split_nodes.append(TextNode(sections[i], text_type))
        new_nodes.extend(split_nodes)
    return new_nodes

def extract_markdown_images(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for onode in old_nodes:
        #This is not a string
        if onode.text_type != TextType.TEXT:
            continue
        #extract links from nodes
        links = extract_markdown_images(onode)
        #no links present
        if len(links) == 0:
            new_nodes.append(onode)
        # links are present
        # spliting using links list
        for link in links:
            # create a loop for processing string with multiple links
            first, second = onode.text.split(f"{link[0]}{link[1]}",2)
            #append text
            new_nodes.append(TextNode(text=first, text_type=TextType.TEXT))
            #append link
            new_nodes.append(TextNode(text=link[0], text_type=TextType.LINK), url=link[1])





    return new_nodes

def split_nodes_link(old_nodes):
    return

node = TextNode(
    "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)",
    TextType.TEXT,
)
new_nodes = split_nodes_link([node])
# [
#     TextNode("This is text with a link ", TextType.TEXT),
#     TextNode("to boot dev", TextType.LINK, "https://www.boot.dev"),
#     TextNode(" and ", TextType.TEXT),
#     TextNode(
#         "to youtube", TextType.LINK, "https://www.youtube.com/@bootdotdev"
#     ),
# ]


print(new_nodes)