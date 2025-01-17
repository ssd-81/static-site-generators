import unittest 
from textnode import TextNode, TextType
from text_to_textnode import text_to_textnodes

class TestTextToTextNodes(unittest.TestCase):
    def test_multiple_text_type_input(self):
        text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"

        expected_output = [
        TextNode("This is ", TextType.TEXT),
        TextNode("text", TextType.BOLD),
        TextNode(" with an ", TextType.TEXT),
        TextNode("italic", TextType.ITALIC),
        TextNode(" word and a ", TextType.TEXT),
        TextNode("code block", TextType.CODE),
        TextNode(" and an ", TextType.TEXT),
        TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
        TextNode(" and a ", TextType.TEXT),
        TextNode("link", TextType.LINK, "https://boot.dev"),]
        
        self.assertEqual(text_to_textnodes(text), expected_output)
    
    def test_simple_text_text_to_textnodes(self):
        text = "I am a shadow"
        expected_output = [TextNode("I am a shadow", TextType.TEXT)]
        self.assertEqual(text_to_textnodes(text), expected_output)
    
    def test_empty_text_text_to_textnodes(self):
        text = ""
        expected_output = []
        self.assertEqual(text_to_textnodes(text), expected_output)
    
    def test_multiple_same_type(self):
        text = "**bold** normal **bold again**"
        expected_output = [
            TextNode("bold", TextType.BOLD),
            TextNode(" normal ", TextType.TEXT),
            TextNode("bold again", TextType.BOLD)
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)
    
    def test_incomplete_markdown(self):
        text = "This has an *italic but no closing and a [link](with no closing"
        expected_output = [TextNode(text, TextType.TEXT)]
        self.assertRaises(Exception, text_to_textnodes, text)
    
    def test_multiple_images_and_links(self):
        text = "![img1](url1) and ![img2](url2) with [link1](url3) and [link2](url4)"
        expected_output = [TextNode("img1", TextType.IMAGE, "url1"), TextNode(" and ", TextType.TEXT), TextNode("img2", TextType.IMAGE, "url2"), TextNode(" with ", TextType.TEXT), TextNode("link1", TextType.LINK, "url3"), TextNode(" and ", TextType.TEXT), TextNode("link2", TextType.LINK, "url4")]
        self.assertEqual(text_to_textnodes(text), expected_output)
    
    def test_nested_delimiters(self):
        text = "This is **bold with *italic* inside**"
        expected_output = [
            TextNode("This is ", TextType.TEXT),
            TextNode("bold with *italic* inside", TextType.BOLD)
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)
    
    def test_leading_trailing_delimiters(self):
        text = "**bold start** plain text *italic end*"
        expected_output = [
            TextNode("bold start", TextType.BOLD),
            TextNode(" plain text ", TextType.TEXT),
            TextNode("italic end", TextType.ITALIC)
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)
    
    def test_consecutive_delimiters(self):
        text = "**bold**`code`*italic*"
        expected_output = [
            TextNode("bold", TextType.BOLD),
            TextNode("code", TextType.CODE),
            TextNode("italic", TextType.ITALIC)
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)
    
    def test_whitespace_handling(self):
        text = "  spaces  **  bold  **  "
        expected_output = [
            TextNode("  spaces  ", TextType.TEXT),
            TextNode("  bold  ", TextType.BOLD),
            TextNode("  ", TextType.TEXT)
        ]
        self.assertEqual(text_to_textnodes(text), expected_output)