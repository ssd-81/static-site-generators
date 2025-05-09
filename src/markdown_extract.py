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
    blocks = re.split(r"\n[ \t]*\n", markdown)
    new_blocks = []

    for block in blocks:
        # Strip whitespace from each block and check if it's non-empty
        temp = block.strip()
        if not temp:
            continue
        new_blocks.append(temp)

    return new_blocks


def block_to_block_type(block):
    line_block_list = block.split("\n")
    heading_pattern = r'^#{1,6} '
    quote_block = r'^>.*'
    ul_block = r'^[*-] '
    
    # Check for heading first
    if re.match(heading_pattern, block):
        return "heading"
    # Check for code blocks
    elif (len(line_block_list) >= 3 and 
          line_block_list[0].strip().startswith('```') and 
          line_block_list[-1].strip() == '```'):
        return "code"
    # Check for quote blocks
    elif all(re.match(quote_block, line) for line in line_block_list):
        return "quote"
    # Check for unordered lists
    elif all(re.match(ul_block, line) for line in line_block_list):
        return "unordered_list"
    # Check for ordered lists
    elif all(re.match(r'^\d+\. ', line) for line in line_block_list):
        count = 1
        for line in line_block_list:
            match = re.match(r'^(\d+)\. ', line)
            if match:
                number = int(match.group(1))
                if number == count:
                    count += 1
                else:
                    return "paragraph"
        return "ordered_list"
    else:
        return "paragraph"  
