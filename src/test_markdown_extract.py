import unittest
from markdown_extract import extract_markdown_images, extract_markdown_links, markdown_to_blocks


class TestMarkdownExtract(unittest.TestCase):
    def test_empty_alt_text_markdown_image_extract(self):
        text = "This is text with a ![](https://i.imgur.com/aKaOqIh.gif)"
        self.assertRaises(ValueError, extract_markdown_images, text) 
    
    def test_empty_image_url_markdown_image_extract(self):
        text = "This is text with a ![let's go]()"
        self.assertRaises(ValueError, extract_markdown_images, text)

    def test_single_markdown_image_extract(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif)"
        img_list = extract_markdown_images(text)
        self.assertEqual(len(img_list), 1)
        self.assertEqual(img_list[0][0],"rick roll")
        self.assertEqual(img_list[0][1],"https://i.imgur.com/aKaOqIh.gif")
    

    def test_multiple_markdown_image_extract(self):
        text = "This is text with a ![cat roll](https://i.imgur.comsllgif) This is text with a ![drum roll](https://i.imgur.drum/aKaOqIh.gif) This is text with a ![chicken roll](https://i.imgur.com/aKaOqIh.gif)"
        img_list = extract_markdown_images(text)
        self.assertEqual(len(img_list), 3)
        self.assertEqual(img_list[0][0], "cat roll")
        self.assertEqual(img_list[0][1], "https://i.imgur.comsllgif") 
        self.assertEqual(img_list[1][0], "drum roll")
        self.assertEqual(img_list[1][1], "https://i.imgur.drum/aKaOqIh.gif") 
        self.assertEqual(img_list[2][0], "chicken roll")
        self.assertEqual(img_list[2][1], "https://i.imgur.com/aKaOqIh.gif") 

    
    def test_empty_alt_text_markdown_link_extract(self):
        text = "This is text with a link [](https://www.boot.dev) woow"
        self.assertRaises(ValueError, extract_markdown_links, text)

    def test_empty_link_url_text_markdown_link_extract(self):
        text = "This is text with a link [heaven is not far, just a mile ahead]() woow"
        self.assertRaises(ValueError, extract_markdown_links, text)  

    def test_single_markdown_link_extract(self):
        # text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        text = "This is text with a link [to boot dev](https://www.boot.dev) woow"
        links_list = extract_markdown_links(text)
        self.assertEqual(len(links_list), 1)
        self.assertEqual(links_list[0][0], "to boot dev")
        self.assertEqual(links_list[0][1], "https://www.boot.dev")
    
    def test_multiple_markdown_link_extract(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev) and last but not least [to virtual space](https://www.boot.dev/space) oh, I forgot, one more [to outer space](https://www.outer.space)"
        links_list = extract_markdown_links(text)
        self.assertEqual(len(links_list), 4)
        self.assertEqual(links_list[0][0], "to boot dev")
        self.assertEqual(links_list[0][1], "https://www.boot.dev")
        self.assertEqual(links_list[1][0], "to youtube")
        self.assertEqual(links_list[1][1], "https://www.youtube.com/@bootdotdev")
        self.assertEqual(links_list[2][0], "to virtual space")
        self.assertEqual(links_list[2][1], "https://www.boot.dev/space")
        self.assertEqual(links_list[3][0], "to outer space")
        self.assertEqual(links_list[3][1], "https://www.outer.space")
    
    # test suite for markdown_to_blocks
    def test_simple_markdown_input_markdown_to_blocks(self):
        raw_markdown = text = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''

        expected_output = ["# This is a heading", "This is a paragraph of text. It has some **bold** and *italic* words inside of it.", '''* This is the first list item in a list block
* This is a list item
* This is another list item'''] 

        self.assertEqual(markdown_to_blocks(raw_markdown),expected_output )
    
    def test_