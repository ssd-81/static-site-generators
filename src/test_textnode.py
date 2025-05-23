import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_repr(self):
        node = TextNode("doing some work", TextType.ITALIC, "NONE")
        self.assertEqual(f"TextNode(doing some work, italic text, NONE)", repr(node))
    
    def test_node_with_none(self):
        node = TextNode("testing none", TextType.BOLD)
        self.assertEqual(node.url, None)
    
    def test_node_none_repr(self):
        node = TextNode("node", TextType.BOLD)
        self.assertEqual(repr(node), f"TextNode(node, bold text, None)")
    
    def test_different(self):
        node = TextNode("we are similar", TextType.ITALIC)
        node2 = TextNode("we are similar", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_explicit_none(self):
        node = TextNode("explicit none", TextType.BOLD, None)
        self.assertEqual(node.url, None)

    def test_invalid_text_type_enum(self):
        with self.assertRaises(ValueError):
            TextNode("Invalid type test", "RANDOM_TYPE")

if __name__ =="__main__":
    unittest.main()