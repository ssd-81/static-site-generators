import unittest
from images_links_additional import split_nodes_image, split_nodes_link
from textnode import TextNode, TextType


class TestImagesLinksAdditional(unittest.TestCase):
    
    def test_single_image_text_node(self):
        node = TextNode("Start ![alt1](url1) middle", TextType.TEXT) 
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "Start ")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].url, "url1")
        self.assertEqual(new_nodes[1].text, "alt1")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " middle")
    
    def test_multiple_image_only_text_node(self):
        node = TextNode("![alt1](url1)![alt2](url2)![alt3](url3)", TextType.TEXT)
        new_nodes = split_nodes_image([node])
        self.assertEqual(len(new_nodes), 3)
        self.assertEqual(new_nodes[0].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].url, "url1")
        self.assertEqual(new_nodes[0].text, "alt1")
        self.assertEqual(new_nodes[1].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[1].url, "url2")
        self.assertEqual(new_nodes[1].text, "alt2")
        self.assertEqual(new_nodes[2].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[2].url, "url3")
        self.assertEqual(new_nodes[2].text, "alt3")
    

    def test_multiple_nodes_with_multiple_image(self):
        node = TextNode("![alt1](url1)![alt2](url2)![alt3](url3)", TextType.TEXT)
        node2 = TextNode("![alt4](url4)![alt5](url5)![alt6](url6)", TextType.TEXT)
        new_nodes = split_nodes_image([node, node2])
        self.assertEqual(len(new_nodes), 6)
        self.assertEqual(new_nodes[0].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[0].url, "url1")
        self.assertEqual(new_nodes[0].text, "alt1")
        self.assertEqual(new_nodes[4].text_type, TextType.IMAGE)
        self.assertEqual(new_nodes[4].url, "url5")
        self.assertEqual(new_nodes[4].text, "alt5")

    def test_single_link_only_text_node(self):
        # node = TextNode("Click [here](https://boot.dev) to start", TextType.TEXT)
        node = TextNode("[here](https://boot.dev)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 1)
        self.assertEqual(new_nodes[0].text_type, TextType.LINK)
        self.assertEqual(new_nodes[0].url, "https://boot.dev")
        self.assertEqual(new_nodes[0].text, "here")
    
    def test_multiple_link_only_text_node(self):
        node = TextNode("Click [here](https://boot.dev) to start [here to](https://boot.dev/shop)[there](https://boot.dev/farm)", TextType.TEXT)
        new_nodes = split_nodes_link([node])
        self.assertEqual(len(new_nodes), 5)
        self.assertEqual(new_nodes[0].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[0].text, "Click ")
        self.assertEqual(new_nodes[2].text_type, TextType.TEXT)
        self.assertEqual(new_nodes[2].text, " to start ")
        self.assertEqual(new_nodes[3].text_type, TextType.LINK)
        self.assertEqual(new_nodes[3].text, "here to")
        self.assertEqual(new_nodes[3].url, "https://boot.dev/shop")
    



