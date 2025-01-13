from textnode import TextType, TextNode

def main():
    test_node = TextNode("nodeba", TextType.BOLD, "https:google.com")
    print(test_node)

main()