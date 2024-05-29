import unittest
from textnode import (TextNode,
                      text_node_to_html_node,
                      text_type_text,
                      text_type_bold,
                      text_type_italic,
                      text_type_code,
                      text_type_link,
                      text_type_image)

from htmlnode import LeafNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", text_type_bold)
        node2 = TextNode("This is a test node", text_type_bold)

        self.assertEqual(node, node2)
        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)

        node3 = TextNode("a test node", text_type_italic, "https://www.google.com")
        node4 = TextNode("a test node", text_type_italic, "https://www.google.com")

        self.assertEqual(node3, node4)

    def test_not_eq(self):
        node = TextNode("something that doesn't match", text_type_bold)
        node2 = TextNode("something that doesnt match", text_type_bold)

        self.assertNotEqual(node, node2)

        node3 = TextNode("something that matches", text_type_bold)
        node4 = TextNode("something that matches", text_type_italic)

        self.assertNotEqual(node3, node4)

        node5 = TextNode("matches", "also matches")
        node6 = TextNode("matches", "also matches", "https://www.google.com")

        self.assertNotEqual(node5, node6)

    def test_text_node_to_html_node(self):
        node = TextNode("some text", text_type_text)
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node, LeafNode("some text"))

        node = TextNode("bold text", text_type_bold)
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node, LeafNode("b", "bold text"))

        node = TextNode("italic text", text_type_italic)
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node, LeafNode("i", "italic text"))

        node = TextNode("for i in range(5):", text_type_code)
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node, LeafNode("code", "for i in range(5):"))

        node = TextNode("a description", text_type_link, "https://www.google.com")
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node, LeafNode("a", "a description", {"href": "https://www.google.com"}))

        node = TextNode("alt text", text_type_image, "https://www.google.com")
        new_node = text_node_to_html_node(node)
        self.assertEqual(new_node, LeafNode("img", "", {"href": "https://www.google.com", "alt": "alt text"}))

if __name__ == "__main__":
    unittest.main()
