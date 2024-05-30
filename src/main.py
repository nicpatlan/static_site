from textnode import TextNode
from inline_markdown import text_to_textnodes

def main():
    node = TextNode("This is a text node", "bold", "https://www.google.com")

    print(node)

    text = "This is **text** with an *italic* word and a `code block` and an ![image](https://storage.googleapis.com/qvault-webapp-dynamic-assets/course_assets/zjjcJKZ.png) and a [link](https://www.github.com)"

    print(text)
    print(text_to_textnodes(text))

main()
