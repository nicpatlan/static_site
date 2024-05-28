import unittest

from htmlnode import HtmlNode

class TestHtmlNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HtmlNode(props={"href": "https://www.google.com", "target": "_blank"})

        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

        node2 = HtmlNode()

        self.assertEqual(node2.props_to_html(), '')

if __name__ == "__main__":
    unittest.main()
