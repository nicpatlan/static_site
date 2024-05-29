import unittest
from inline_markdown import split_nodes_delimiter
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

if __name__ == "__main__":
    unittest.main()
