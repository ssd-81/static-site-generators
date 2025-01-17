import re

def extract_markdown_images(text):
    imgs_meta = re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for i in range(len(imgs_meta)):
        if not imgs_meta[i][0]:
            raise ValueError("alt text cannot be empty")
        if not imgs_meta[i][1]:
            raise ValueError("image links cannot be empty")
    return imgs_meta


def extract_markdown_links(text):
    # alt_text = re.findall(r"\[(.*?)\]", text)
    # link_text = re.findall(r"\((.*?)\)", text)

    links_meta = re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)
    for i in range(len(links_meta)):
        if not links_meta[i][0]:
            raise ValueError("alt text cannot be empty")
        if not links_meta[i][1]:
            raise ValueError("url links cannot be empty")
    return links_meta


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    print("Yo", blocks)
    for block in blocks:
        block = block.strip()
        if not block:
            blocks.remove(block)
            continue
    return blocks

sample_input = """# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item"""
print(markdown_to_blocks(sample_input))
             