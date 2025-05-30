from textnode import TextNode, TextType
from markdown_extract import extract_markdown_images, extract_markdown_links


def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        while True:
            imgs = extract_markdown_images(text)
            if not imgs:
                if text.strip():
                    new_nodes.append(TextNode(text, TextType.TEXT))
                break
            
            # Process first image only
            img = imgs[0]  # (alt, url)
            # sections will essentially return a list of substrings split on img arg
            sections = text.split(f"![{img[0]}]({img[1]})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(img[0], TextType.IMAGE, img[1]))
            text = "".join(sections[1:])
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        text = node.text
        while True:
            links = extract_markdown_links(text)
            if not links:
                if text.strip():
                    new_nodes.append(TextNode(text, TextType.TEXT))
                break
            
            link = links[0]  # (alt, url)
            sections = text.split(f"[{link[0]}]({link[1]})", 1)
            if sections[0]:
                new_nodes.append(TextNode(sections[0], TextType.TEXT))
            new_nodes.append(TextNode(link[0], TextType.LINK, link[1]))
            text = "".join(sections[1:])
    return new_nodes
