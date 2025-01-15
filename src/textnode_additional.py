from textnode import TextNode, TextType


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    # old_nodes is a list of nodes
    # we need to return a set of new nodes based on the delimiter 
    new_nodes = []
    for old_node in old_nodes:
        # do make checks wherever necessary
        if old_node.text_type == TextType.TEXT: # are you sure that this was the condition
            temp = old_node.text.split(delimiter)
            if len(temp) % 2 == 0:
                raise Exception("invalid markdown syntax")
            for sub in range(len(temp)):
                if sub % 2 != 0:
                    new_nodes.append(convertTextNode(temp[sub], delimiter, text_type))
                else:
                    new_nodes.append(TextNode(temp[sub], TextType.TEXT))
        else:
            new_nodes.append(old_node)
    return new_nodes

def convertTextNode(text, delimiter, text_type):
    # you might need to rework on this due to fine details
    # what is the point of parameter text_type ???
    if delimiter == "**":
        return TextNode(text, text_type)
    elif delimiter == "*":
        return TextNode(text, text_type)
    elif delimiter == "`":
        return TextNode(text, text_type)