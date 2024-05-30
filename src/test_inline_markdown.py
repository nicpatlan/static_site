import unittest
from inline_markdown import (split_nodes_delimiter,
                             extract_markdown_images,
                             extract_markdown_links,
                             split_nodes_image,
                             split_nodes_link)

from textnode import (TextNode,
                      text_type_text,
                      text_type_bold,
                      text_type_italic,
                      text_type_code,
                      text_type_link,
                      text_type_image)

class TestInlineMarkdown(unittest.TestCase):
    def test_split_nodes_delimiter(self):
        node_list = [TextNode("text with `code block` in the middle", text_type_text), TextNode("some `code` here too", text_type_text)]
        new_nodes = split_nodes_delimiter(node_list, "`", text_type_code)
        self.assertEqual(new_nodes, 
                         [
                             TextNode("text with ", text_type_text), 
                             TextNode("code block", text_type_code), 
                             TextNode(" in the middle", text_type_text),
                             TextNode("some ", text_type_text),
                             TextNode("code", text_type_code),
                             TextNode(" here too", text_type_text)
                         ]
        )

        node_list = [TextNode("text with `code block` in the middle and another `code block` after", text_type_text)]
        new_nodes = split_nodes_delimiter(node_list, "`", text_type_code)
        self.assertEqual(new_nodes,
                         [
                             TextNode("text with ", text_type_text), 
                             TextNode("code block", text_type_code), 
                             TextNode(" in the middle and another ", text_type_text),
                             TextNode("code block", text_type_code),
                             TextNode(" after", text_type_text)
                         ]
        )

        node_list = [TextNode("text with **bold** in the middle", text_type_text), TextNode("some **bold** here too", text_type_text)]
        new_nodes = split_nodes_delimiter(node_list, "**", text_type_bold)
        self.assertEqual(new_nodes, 
                         [
                             TextNode("text with ", text_type_text), 
                             TextNode("bold", text_type_bold), 
                             TextNode(" in the middle", text_type_text),
                             TextNode("some ", text_type_text),
                             TextNode("bold", text_type_bold),
                             TextNode(" here too", text_type_text)
                         ]
        )

        node_list = [TextNode("text with **bold text** in the middle and another **bold text** after", text_type_text)]
        new_nodes = split_nodes_delimiter(node_list, "**", text_type_bold)
        self.assertEqual(new_nodes,
                         [
                             TextNode("text with ", text_type_text), 
                             TextNode("bold text", text_type_bold), 
                             TextNode(" in the middle and another ", text_type_text),
                             TextNode("bold text", text_type_bold),
                             TextNode(" after", text_type_text)
                         ]
        )

    def test_extract_markdown(self):
        image_string = "two images ![some alt text](https://www.google.com) and ![more alt text](https://www.github.com)"
        image_matches = extract_markdown_images(image_string)
        self.assertEqual(image_matches, [("some alt text", "https://www.google.com"), ("more alt text", "https://www.github.com")])

        link_string = "a link here [link](https://www.google.com) and another [github](https://www.github.com)"
        link_matches = extract_markdown_links(link_string)
        self.assertEqual(link_matches, [("link", "https://www.google.com"), ("github", "https://www.github.com")])

    def test_split_nodes_image(self):
        node_list = [TextNode("two images ![some alt text](https://www.google.com) and one ![more alt text](https://www.github.com) here", text_type_text)]
        new_nodes = split_nodes_image(node_list)
        self.assertEqual(new_nodes, [TextNode("two images ", text_type_text),
                                     TextNode("some alt text", text_type_image, "https://www.google.com"),
                                     TextNode(" and one ", text_type_text),
                                     TextNode("more alt text", text_type_image, "https://www.github.com"),
                                     TextNode(" here", text_type_text)
                                    ]
        )

        node_list = [TextNode("![alt here](https://www.google.com) this has a image to start", text_type_text),
                     TextNode("this has a image at the end ![another alt here](https://www.github.com)", text_type_text),
                     TextNode("this has no image", text_type_text)
                    ]
        new_nodes = split_nodes_image(node_list)
        self.assertEqual(new_nodes, [TextNode("alt here", text_type_image, "https://www.google.com"),
                                     TextNode(" this has a image to start", text_type_text),
                                     TextNode("this has a image at the end ", text_type_text),
                                     TextNode("another alt here", text_type_image, "https://www.github.com"),
                                     TextNode("this has no image", text_type_text)
                                    ]
        )

        image_only = [TextNode("![alt here](https://www.google.com)", text_type_text)]
        new_nodes = split_nodes_image(image_only)
        self.assertEqual(new_nodes, [TextNode("alt here", text_type_image, "https://www.google.com")])


    def test_split_nodes_links(self):
        single_node = [TextNode("two links [some link text](https://www.google.com) and one [more link text](https://www.github.com) here", text_type_text)]
        new_nodes = split_nodes_link(single_node)
        self.assertEqual(new_nodes, [TextNode("two links ", text_type_text),
                                     TextNode("some link text", text_type_link, "https://www.google.com"),
                                     TextNode(" and one ", text_type_text),
                                     TextNode("more link text", text_type_link, "https://www.github.com"),
                                     TextNode(" here", text_type_text)
                                    ]
        )

        node_list = [TextNode("[a link here](https://www.google.com) this has a link to start", text_type_text),
                     TextNode("this has a link at the end [another link here](https://www.github.com)", text_type_text),
                     TextNode("this has no links", text_type_text)
                    ]
        new_nodes = split_nodes_link(node_list)
        self.assertEqual(new_nodes, [TextNode("a link here", text_type_link, "https://www.google.com"),
                                     TextNode(" this has a link to start", text_type_text),
                                     TextNode("this has a link at the end ", text_type_text),
                                     TextNode("another link here", text_type_link, "https://www.github.com"),
                                     TextNode("this has no links", text_type_text)
                                    ]
        )

        link_only = [TextNode("[a link here](https://www.google.com)", text_type_text)]
        new_nodes = split_nodes_link(link_only)
        self.assertEqual(new_nodes, [TextNode("a link here", text_type_link, "https://www.google.com")])


if __name__ == "__main__":
    unittest.main()
