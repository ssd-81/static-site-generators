from textnode import TextType, TextNode
from htmlnode import HTMLNode, ParentNode, LeafNode

def text_node_to_html_node(text_node):
    # convert a text_node to html_node (leaf node)
    match text_node.text_type:
        case TextType.TEXT:
            return LeafNode(None, text_node.text)
        case TextType.BOLD:
            return LeafNode('b', text_node.text)
        case TextType.ITALIC:
            return LeafNode('i', text_node.text)
        case TextType.CODE:
            return LeafNode('code', text_node.text)
        case TextType.LINK:
            # probably cause some issues
            return LeafNode('a', text_node.text, {"href":f"{text_node.url}"})
        case TextType.IMAGE:
            # what will be the alt text
            return LeafNode('img', "", {"src":f"{text_node.url}", "alt":f"{text_node.text}"})


def main():
    pass
