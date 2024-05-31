import unittest
from block_to_html import (heading_block_to_htmlnode,
                           paragraph_block_to_htmlnode,
                           quote_block_to_htmlnode,
                           code_block_to_htmlnode,
                           unordered_list_block_to_htmlnode,
                           ordered_list_block_to_htmlnode,
                           markdown_to_html_node)
from textnode import (text_type_text,
                      text_type_bold,
                      text_type_italic,
                      text_type_code,
                      text_type_link,
                      text_type_image)
from htmlnode import (HtmlNode,
                      ParentNode,
                      LeafNode)

from block_to_html import heading_block_to_htmlnode

class TestBlockToHtml(unittest.TestCase):
    def test_heading_block_to_htmlnode(self):
        block = "# Heading 1"
        parent_node = heading_block_to_htmlnode(block)
        self.assertEqual(parent_node,
                         ParentNode("h1", 
                                    [LeafNode(None, "Heading 1")]
                                   )
                        )

    def test_paragraph_block_to_htmlnode(self):
        block = "a simple paragraph"
        parent_node = paragraph_block_to_htmlnode(block)
        self.assertEqual(parent_node,
                         ParentNode("p", 
                                    [LeafNode(value="a simple paragraph")]
                                   )
                        )

    def test_quote_block_to_htmlnode(self):
        block = "> a simple quote"
        parent_node = quote_block_to_htmlnode(block)
        self.assertEqual(parent_node,
                         ParentNode("blockquote",
                                    [LeafNode(value=" a simple quote")]
                                   )
                        )

    def test_code_block_to_htmlnode(self):
        block = "```\na code block\n```"
        parent_node = code_block_to_htmlnode(block)
        self.assertEqual(parent_node,
                         ParentNode("pre",
                                    [LeafNode(text_type_code, "\na code block\n")]
                                   )
                        )

    def test_unordered_list_block_to_htmlnode(self):
        block = "* a **bold** item\n* another item\n* and one more"
        parent_node = unordered_list_block_to_htmlnode(block)
        self.assertEqual(parent_node,
                         ParentNode("ul",
                                     [LeafNode("li", ""),
                                      LeafNode(value="a "),
                                      LeafNode("b", "bold"),
                                      LeafNode(value=" item"),
                                      LeafNode("li", ""),
                                      LeafNode("li", ""),
                                      LeafNode(value="another item"),
                                      LeafNode("li", ""),
                                      LeafNode("li", ""),
                                      LeafNode(value="and one more"),
                                      LeafNode("li", "")
                                     ]
                                   )
                        )

    def test_ordered_list_block_to_htmlnode(self):
        block = "1. first item\n2. second item\n3. third *italic* item"
        parent_node = ordered_list_block_to_htmlnode(block)
        self.assertEqual(parent_node,
                         ParentNode("ol",
                                    [LeafNode("li", ""),
                                      LeafNode(value="first item"),
                                      LeafNode("li", ""),
                                      LeafNode("li", ""),
                                      LeafNode(value="second item"),
                                      LeafNode("li", ""),
                                      LeafNode("li", ""),
                                      LeafNode(value="third "),
                                      LeafNode("i", "italic"),
                                      LeafNode(value=" item"),
                                      LeafNode("li", "")
                                     ]
                                   )
                        )

    def test_markdown_to_html_node(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        parent_node = markdown_to_html_node(markdown)
        self.assertEqual(parent_node,
                         ParentNode("div", 
                                    [ParentNode("p", 
                                                [
                                                    LeafNode(None, "This is "), 
                                                    LeafNode("b", "bolded"), 
                                                    LeafNode(None, " paragraph")
                                                ], 
                                                None
                                               ), 
                                     ParentNode("p", 
                                                [
                                                    LeafNode(None, "This is another paragraph with "), 
                                                    LeafNode("i", "italic"), 
                                                    LeafNode(None, " text and "), 
                                                    LeafNode("code", "code"), 
                                                    LeafNode(None, " here\nThis is the same paragraph on a new line")
                                                ], 
                                                None
                                               ), 
                                     ParentNode("ul", 
                                                [
                                                    LeafNode("li", ""), 
                                                    LeafNode(None, "This is a list"), 
                                                    LeafNode("li", "", None), 
                                                    LeafNode("li", "", None), 
                                                    LeafNode(None, "with items"), 
                                                    LeafNode("li", "")
                                                ], 
                                                None
                                               )], 
                                    None
                                   )
                        )

    def test_markdown_to_html(self):
        markdown = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line
"""
        parent_node = markdown_to_html_node(markdown)
        self.assertEqual(parent_node,
                         ParentNode("div", 
                                    [ParentNode("p", 
                                                [
                                                    LeafNode(None, "This is "), 
                                                    LeafNode("b", "bolded", None), 
                                                    LeafNode(None, " paragraph")
                                                ], 
                                                None
                                               ), 
                                     ParentNode("p", 
                                                [
                                                    LeafNode(None, "This is another paragraph with "), 
                                                    LeafNode("i", "italic"), 
                                                    LeafNode(None, " text and "), 
                                                    LeafNode("code", "code"), 
                                                    LeafNode(None, " here\nThis is the same paragraph on a new line")
                                                ], 
                                                None
                                               ), 
                                    ], 
                                    None
                                   )
                        )

        #print(parent_node)

if __name__ == "__main__":
    unittest.main()
