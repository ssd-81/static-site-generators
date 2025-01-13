import unittest
from htmlnode import HTMLNode

from textnode import TextNode, TextType


class TestHTMLNode(unittest.TestCase):
    def test_object_initialization(self):
        node = HTMLNode('h', 'don chandu')
        self.assertIsInstance(node, HTMLNode)
    
    def test_repr(self):
        node = HTMLNode('h', 'don cola')
        self.assertEqual(repr(node), "HTMLNode(h, don cola, None, None)")
    
    def test_props_to_html(self):
        node = HTMLNode('h', 'master shifu', None, {
        "href": "www.google.com", 
        "target": "_blank",})
        self.assertEqual(node.props_to_html(), ' href="www.google.com" target="_blank"')

    def test_to_html(self):
        node = HTMLNode('p', 'tenma')
        self.assertRaises(NotImplementedError, node.to_html)




