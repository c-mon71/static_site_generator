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
    matches = re.findall(r"!\[(.*?)\]\((.*?)\)", text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return matches

def split_nodes_link(old_nodes):
    new_nodes = []
    for onode in old_nodes:
        #This is not a string
        if onode.text_type != TextType.TEXT:
            new_nodes.append(onode)
            continue
        #extract links from nodes
        links = extract_markdown_links(onode.text)
        #no links present
        if len(links) == 0:
            new_nodes.append(onode)
            continue
        # links are present
        # spliting using links list
        text_to_process = onode.text
        for link in links:
            pattern = f"[{link[0]}]({link[1]})"
            splitted = text_to_process.split(pattern,1)
            if splitted[0] != "":
                new_nodes.append(TextNode(text=splitted[0], text_type=TextType.TEXT))
            new_nodes.append(TextNode(text=link[0], text_type=TextType.LINK, url=link[1]))
            if len(splitted) == 2:
                text_to_process = splitted[1]
            else:
                text_to_process = ""
        if text_to_process != "":
            new_nodes.append(TextNode(text_to_process, TextType.TEXT))
    return new_nodes

def split_nodes_image(old_nodes):
    new_nodes = []
    for onode in old_nodes:
        #This is not a string
        if onode.text_type != TextType.TEXT:
            new_nodes.append(onode)
            continue
        images = extract_markdown_images(onode.text)
        if len(images) == 0:
            new_nodes.append(onode)
            continue
        text_to_process = onode.text
        for image in images:
            pattern = f"![{image[0]}]({image[1]})"
            splitted = text_to_process.split(pattern,1)
            if splitted[0] != "":
                new_nodes.append(TextNode(text=splitted[0], text_type=TextType.TEXT))
            new_nodes.append(TextNode(text=image[0], text_type=TextType.IMAGE, url=image[1]))
            if len(splitted) == 2:
                text_to_process = splitted[1]
            else:
                text_to_process = ""
        if text_to_process != "":
            new_nodes.append(TextNode(text_to_process, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    node = [TextNode(text, TextType.TEXT)]
    #print("node:", node)
    nodes = split_nodes_delimiter(node, "**", TextType.BOLD)
    #print("nodes bold:", nodes)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    #print("nodes italic:", nodes)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    #print("nodes code:", nodes)
    nodes = split_nodes_image(nodes)
    #print("nodes img:", nodes)
    nodes = split_nodes_link(nodes)
    #print("nodes link:", nodes)

    return nodes