import unittest
from textnode import TextNode, TextType
from main import text_node_to_html_node

class TestConversionNodes(unittest.TestCase):
    def test_raw_text(self):
        text_node = TextNode('kahneman', TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual("kahneman", html_node.to_html())

    def test_bold_text(self):
        text_node = TextNode('mettle defender', TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual("<b>mettle defender</b>", html_node.to_html())
    
    def test_italics_text(self):
        text_node = TextNode('detection therapy', TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual("<i>detection therapy</i>", html_node.to_html())
    
    def test_code_text(self):
        text_node = TextNode('masters of doom', TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        self.assertEqual("<code>masters of doom</code>", html_node.to_html())

    def test_link_text(self):
        text_node = TextNode('Apple, inc', TextType.LINK, "https://www.google.com")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual('<a href="https://www.google.com">Apple, inc</a>', html_node.to_html())
    
    def test_image_text(self):
        text_node = TextNode("This would be alt text", TextType.IMAGE, "/link/to/some/image")
        html_node = text_node_to_html_node(text_node)
        self.assertEqual('<img src="/link/to/some/image" alt="This would be alt text"></img>',
        html_node.to_html())

