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
    # Use re.split to handle blank lines with spaces/tabs
    blocks = re.split(r'\n[ \t]*\n', markdown)
    new_blocks = []

    for block in blocks:
        # Strip whitespace from each block and check if it's non-empty
        temp = block.strip()
        if not temp:
            continue
        new_blocks.append(temp)

    return new_blocks




             