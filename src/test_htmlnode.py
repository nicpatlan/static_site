import unittest

from htmlnode import HtmlNode, LeafNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

        node2 = HtmlNode()

        self.assertEqual(node2.props_to_html(), '')

    def test_leafnode_to_html(self):
        node = LeafNode("p", "This is a paragraph of text")
        self.assertEqual(node.to_html(), "<p>This is a paragraph of text</p>")

        node2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        self.assertEqual(node2.to_html(), '<a href="https://www.google.com">Click me!</a>')

        node3 = LeafNode("b", "I'm bold!")
        self.assertEqual(node3.to_html(), "<b>I'm bold!</b>")

        node4 = LeafNode("i", "Fancy Italy?")
        self.assertEqual(node4.to_html(), "<i>Fancy Italy?</i>")

        node7 = LeafNode(value="no tags means its a raw string")
        self.assertEqual(node7.to_html(), "no tags means its a raw string")

        self.assertRaises(ValueError, LeafNode().to_html)

if __name__ == "__main__":
    unittest.main()
