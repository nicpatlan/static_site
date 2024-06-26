import unittest

from htmlnode import HtmlNode, LeafNode, ParentNode

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

    def test_parentnode_to_html(self):
        node = ParentNode(
                "p",
                [
                    LeafNode("b", "This text is bold!"),
                    LeafNode("i", "This text is fancy!"),
                    LeafNode(value="No tags for this text!")
                ],
        )
        self.assertEqual(node.to_html(), "<p><b>This text is bold!</b><i>This text is fancy!</i>No tags for this text!</p>")

        node2 = ParentNode(
                "p",
                [
                    ParentNode(
                        "p",
                        [
                            LeafNode("i", "fancy text"),
                            LeafNode("b", "bold text")
                        ]
                    ),
                    LeafNode("b", "more bold text")
                ]
        )
        self.assertEqual(node2.to_html(), "<p><p><i>fancy text</i><b>bold text</b></p><b>more bold text</b></p>")



        self.assertRaises(ValueError, ParentNode().to_html)
        self.assertRaises(ValueError, ParentNode(children=[LeafNode("b", "Bold text")]).to_html)

if __name__ == "__main__":
    unittest.main()
