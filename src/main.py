from textnode import TextNode
from inline_markdown import (extract_markdown_images,
                             extract_markdown_links)

def main():
    node = TextNode("This is a text node", "bold", "https://www.google.com")

    print(node)

    print(extract_markdown_images("two images ![some alt text](https://google.com) and ![more alt text](https://www.github.com)"))
    print(extract_markdown_links("a link here [link](https://www.google.com) and another [github](https://github.com)"))

main()
