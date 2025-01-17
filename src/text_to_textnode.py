from textnode import TextNode, TextType
from textnode_additional import split_nodes_delimiter
from images_links_additional import split_nodes_image, split_nodes_link


def text_to_textnodes(text):
    DELIMITERS = [
    ("**", TextType.BOLD),
    ("*", TextType.ITALIC),
    ("`", TextType.CODE)
    ]
    node = TextNode(text, TextType.TEXT)
    nodes = split_nodes_image([node])
    nodes = split_nodes_link(nodes)
    for delimiter, text_type in DELIMITERS:
        nodes = split_nodes_delimiter(nodes, delimiter, text_type)
    return nodes
