from enum import Enum
from src.htmlnode import HTMLNode

class BlockType(Enum):
    PARAGRAPH      = "paragraph"
    HEADING        = "heading"
    CODE           = "code"
    QUOTE          = "quote"
    UNORDERED_LIST = "unordered_list"
    ORDERED_LIST   = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    cleaned_blocks = [b.strip() for b in blocks if b.strip()]

    return cleaned_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    #RootNode = HTMLNode(None, None, None, None)
    return blocks

def block2heading(block):
    count = len(block) - len(block.lstrip("#"))
    return HTMLNode(f"h{count}", block[count:].strip(" "))

md = """
This is **bolded** paragraph
text in a p
tag here

This is another paragraph with _italic_ text and `code` here

"""
print(markdown_to_html_node(md))
