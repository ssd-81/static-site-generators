import unittest
from htmlnode import HTMLNode, LeafNode

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
    
    def test_leaf_node_instantiation(self):
        leaf_node = LeafNode('p', 'today is a git')
        self.assertIsInstance(leaf_node, LeafNode)
    
    def test_leaf_node_repr(self):
        leaf_node = LeafNode('a', 'google.com', {"href":"https://www.google.com"})
        self.assertEqual('HTMLNode(a, google.com, None, {\'href\': \'https://www.google.com\'})', repr(leaf_node))

    def test_leaf_node_to_html_edge_cases(self):
        err_node = LeafNode('h', None)
        raw_node = LeafNode(None, 'apple')
        full_node = LeafNode('a', 'google.com',{"href":"https://www.google.com"})
        self.assertEqual(full_node.to_html(), "<a href=\"https://www.google.com\">google.com</a>")
        self.assertRaises(ValueError, err_node.to_html)
        self.assertEqual(raw_node.to_html(), 'apple')



