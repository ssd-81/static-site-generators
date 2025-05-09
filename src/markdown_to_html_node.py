from htmlnode import HTMLNode, LeafNode, ParentNode
from markdown_extract import markdown_to_blocks, block_to_block_type
from text_to_textnode import text_to_textnodes
from textnode import TextNode

def markdown_to_html_node(markdown):
    # 1 split markdown into blocks 
    md_blocks = markdown_to_blocks(markdown)
    html_nodes = []
    for block in md_blocks:
        block_type = block_to_block_type(block)
        # create htmlnode based on block_type
        if block_type == "heading":
            # find the number '#' before the block
            hash_count = 0
            for i in block:
                if i != "#":
                    break
                else:
                    hash_count += 1
            content = block.lstrip("#").strip()
            html_node = LeafNode(f"h{hash_count}",content)
            html_nodes.append(html_node)
        elif block_type == "code":
            content_list = block.splitlines()
            del content_list[0]
            del content_list[len(content_list)-1]
            code_node = LeafNode("code",'\n'.join(content_list))
            html_node = ParentNode("pre", [code_node])
            html_nodes.append(html_node)
        elif block_type == "paragraph":
            text_nodes = text_to_textnodes(block)
            html_children = []
            for text_node in text_nodes:
                html_children.append(text_node.textnode_to_htmlnode())
            paragraph_parent_node = ParentNode("p", html_children)
            html_nodes.append(paragraph_parent_node)
        elif block_type == "quote":
            quote_list = block.splitlines()
            text_list = []
            for quote_part in quote_list:
                quote_part = quote_part.lstrip()
                if quote_part.startswith(">"):
                    quote_part = quote_part[1:]                
                    if quote_part.startswith(" "):
                        quote_part = quote_part[1:]
                text_list.append(quote_part)
            paragraph_lines = []
            paragraphs  = []
            for line in text_list:
                if not line:
                    if paragraph_lines:
                        paragraphs.append("\n".join(paragraph_lines))
                        paragraph_lines = []
                else:
                    paragraph_lines.append(line)
            if paragraph_lines:
                paragraphs.append("\n".join(paragraph_lines))
            
            for paragraph in paragraphs:
                

            text_nodes = text_to_textnodes("\n".join(text_list))
            html_children = []
            for text_node in text_nodes:
                html_children.append(text_node.textnode_to_htmlnode())
            quote_parent_node = ParentNode("blockquote", html_children)
            html_nodes.append(quote_parent_node)


        elif block_type == "unordered_list":
            pass
        elif block_type == "ordered_list":
            pass
        else:
            raise Exception("invalid block type")
    # create a parent node to store all the html_nodes in div
    return ParentNode("div", html_nodes)

