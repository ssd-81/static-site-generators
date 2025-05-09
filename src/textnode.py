from enum import Enum
from htmlnode import HTMLNode, ParentNode, LeafNode

class TextType(Enum):
    TEXT = "normal text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINK = "links"
    IMAGE = "images"


class TextNode:
    def __init__(self, text, text_type: TextType, url=None):
        if text_type not in [member for member in TextType]:
            raise ValueError(f"{text_type} is not a valid TextType")
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return (self.text == other.text and self.text_type == other.text_type
        and self.url == other.url)
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url})"

    def textnode_to_htmlnode(self):
        # checks need to be made for this thoroughly , especially None in TEXT  
        if self.text_type == TEXT:
            return LeafNode(None, self.text)
        elif self.text_type == BOLD:
            return LeafNode("b", self.text)
        elif self.text_type == ITALIC:
            return LeafNode("i", self.text)
        elif self.text_type == CODE:
            return LeafNode("code", self.text)
        elif self.text_type == LINK:
            return LeafNode("a", self.text, {"href": self.url})
        elif self.text_type == IMAGE:
            return LeafNode("img", "", {"src" : self.url, "alt": self.text}) 
