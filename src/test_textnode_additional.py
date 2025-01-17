import unittest

from textnode_additional import split_nodes_delimiter
from textnode import TextNode, TextType


class TestTextNodeAdditional(unittest.TestCase):
    def test_plain_text_input(self):
        node = TextNode("Amongst the few, there are none", TextType.TEXT)
        node2 = TextNode("The dark makes a call", TextType.BOLD)
        alt_node = split_nodes_delimiter([node], "*", TextType.TEXT)
        alt_nodes2 = split_nodes_delimiter([node, node2], "*", TextType.TEXT)
        self.assertEqual(len(alt_node), 1)
        self.assertEqual(len(alt_nodes2), 2)
    
    def test_missing_pair(self):
        node = TextNode("There is a **hole in my heart", TextType.TEXT)
        self.assertRaises(Exception, split_nodes_delimiter, [node], "**", TextType.BOLD)

    def test_bold_text_input(self):
        node = TextNode("There is an enlightened being among us", TextType.TEXT)
        node2 = TextNode("The shadow is calling **me**", TextType.TEXT)
        alt_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(len(alt_nodes), 3)

    def test_italic_text_input(self):
        node = TextNode("what you desire, lies *ahead*", TextType.TEXT)
        alt_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        self.assertEqual(len(alt_nodes), 2)
    
    def test_code_text_input(self):
        node = TextNode("the python code: `x == (x+1) ` is very confusing", TextType.TEXT)
        node2 = TextNode("The underlying lie", TextType.TEXT)
        alt_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        alt_nodes2 = split_nodes_delimiter([node, node2],"`",  TextType.CODE)
        self.assertEqual(len(alt_nodes), 3)
        self.assertEqual(len(alt_nodes2), 4)
    
    def test_content_output_from_function(self):
        node = TextNode("The dark **knight** rises", TextType.TEXT)
        node2 = TextNode("Spiderman, spiderman, you know", TextType.TEXT)
        alt_nodes = split_nodes_delimiter([node, node2], "**", TextType.BOLD)
        self.assertEqual(alt_nodes[0].text, "The dark ")
        self.assertEqual(alt_nodes[1].text, "knight")
        self.assertEqual(alt_nodes[2].text, " rises")

    def test_output_text_type(self):
        node = TextNode("What is the *secret* behind your beauty?", TextType.TEXT)
        node2 = TextNode("The dimensity `processor`", TextType.TEXT)
        alt_nodes = split_nodes_delimiter([node], "*", TextType.ITALIC)
        alt_nodes2 = split_nodes_delimiter([node, node2],"`", TextType.CODE)
        self.assertEqual(alt_nodes[1].text_type, TextType.ITALIC)
        self.assertEqual(alt_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(alt_nodes2[0].text_type, TextType.TEXT)
        self.assertEqual(alt_nodes2[2].text_type, TextType.CODE)

    def test_multiple_delimiters_text_input(self):
        node = TextNode("What is the **meaning** of **life**?", TextType.TEXT)
        alt_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(alt_nodes), 5)
        self.assertEqual(alt_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(alt_nodes[3].text_type, TextType.BOLD)
        self.assertEqual(alt_nodes[1].text, "meaning")
        self.assertEqual(alt_nodes[3].text, "life")
    
    def test_empty_delimiters_text_input(self):
        node = TextNode("What is the core apple development ** **",TextType.TEXT)
        alt_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(alt_nodes), 2)
        self.assertEqual(alt_nodes[1].text_type, TextType.BOLD)
        self.assertEqual(alt_nodes[1].text, " ")


    def test_preserve_non_text_type(self):
        node = TextNode("Let us **break** dance", TextType.BOLD)
        alt_node = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(len(alt_node), 1)
        self.assertEqual(alt_node[0].text, "Let us **break** dance")
        self.assertEqual(alt_node[0].text_type, TextType.BOLD)

