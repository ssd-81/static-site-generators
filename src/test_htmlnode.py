import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
    
    def test_simple_leaf_node(self):
        node = LeafNode('p', 'The solitude of masters')
        self.assertEqual(node.to_html(), "<p>The solitude of masters</p>")

    def test_parent_node_to_html(self):
        node = ParentNode('p', [LeafNode('a', 'google.com', {"href":"https://www.google.com"}),
        LeafNode('p', 'apple')])
        self.assertEqual(node.to_html(), '<p><a href="https://www.google.com">google.com</a><p>apple</p></p>')

    def test_parent_node_to_html_edge_cases(self):
        parent_node_inside = ParentNode('p', [ParentNode('p', [LeafNode('p', 'wikipedia')])])
        absent_parent_tag = ParentNode(None, [LeafNode('p', 'americano')])
        multiple_child_parent_node = ParentNode('p', [LeafNode('h1', 'transition'), 
        LeafNode('h2', 'demarcation'), ParentNode('p', [LeafNode('a', 'nothing')])])
        self.assertEqual(multiple_child_parent_node.to_html(), '<p><h1>transition</h1><h2>demarcation</h2><p><a>nothing</a></p></p>')
        self.assertRaises(ValueError , absent_parent_tag.to_html)
        self.assertEqual(parent_node_inside.to_html(), '<p><p><p>wikipedia</p></p></p>')
    
    def test_parent_node_with_none_value_child(self):
        node = ParentNode('p', [LeafNode('h1', 'demarcation'), LeafNode('p', None)])
        self.assertRaises(ValueError, node.to_html)
    
    def test_parent_node_with_props(self):
        node = ParentNode('p', [LeafNode('div', 'content is the king'), LeafNode('a', 'gmail.com')], {"someprop":"idk"})
        self.assertEqual(node.to_html(), '<p someprop="idk"><div>content is the king</div><a>gmail.com</a></p>')

    



