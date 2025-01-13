from enum import Enum

class TextType(Enum):
    NORMAL = "normal text"
    BOLD = "bold text"
    ITALIC = "italic text"
    CODE = "code text"
    LINKS = "links"
    IMAGES = "images"


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



