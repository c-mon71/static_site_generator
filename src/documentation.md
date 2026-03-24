1. **textnode.py**
   1. class TextType
   2. class TextNode
   3. text_node_to_html_node(text_node) -> LeafNode
2. **htmlnode.py**
   1. class HtmlNode
   2. class LeafNode(HtmlNode)
   3. class ParentNode(htmlNode)
3. **inline.py**
   1. split_nodes_delimiter
   2. split_nodes_link
   3. split_nodes_image
   4. text_to_text_nodes
4. **block.py**
   1. class BlockType
   2. markdown_to_blocks
   3. block_to_block_type
   4. _markdown_to_html_node_