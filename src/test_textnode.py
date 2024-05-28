import unittest

from textnode import TextNode

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a test node", "bold")
        node2 = TextNode("This is a test node", "bold")

        self.assertEqual(node, node2)
        self.assertIsNone(node.url)
        self.assertIsNone(node2.url)

        node3 = TextNode("a test node", "italic", "something")
        node4 = TextNode("a test node", "italic", "something")

        self.assertEqual(node3, node4)

    def test_not_eq(self):
        node = TextNode("something that doesn't match", "bold")
        node2 = TextNode("something that doesnt match", "bold")

        self.assertNotEqual(node, node2)

        node3 = TextNode("something that matches", "dont match")
        node4 = TextNode("something that matches", "don't match")

        self.assertNotEqual(node3, node4)

        node5 = TextNode("matches", "also matches", None)
        node6 = TextNode("matches", "also matches", "not None")

        self.assertNotEqual(node5, node6)

if __name__ == "__main__":
    unittest.main()
