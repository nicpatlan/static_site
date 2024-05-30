import unittest

from block_markdown import markdown_to_blocks

class TestBlockMarkdown(unittest.TestCase):
    def test_markdown_to_blocks(self):
        markdown = ("This is **bolded** paragraph\n"
                    "\n"
                    "This is another paragraph with *italic* text and `code` here\n"
                    "This is the same paragraph on a new line\n"
                    "\n"
                    "* This is a list\n"
                    "* with items")
        block_list = markdown_to_blocks(markdown)
        self.assertEqual(block_list,
                         ["This is **bolded** paragraph",
                          "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                          "* This is a list\n* with items"
                         ]
        )
        
        markdown = ("This has *italic* stuff and excessive new lines beneath\n"
                    "\n\n\n"
                    "This is another block with excessive new lines below\n"
                    "\n\n"
                    "\n\n\n\n\n\n")
        block_list = markdown_to_blocks(markdown)
        self.assertEqual(block_list,
                         ["This has *italic* stuff and excessive new lines beneath",
                          "This is another block with excessive new lines below"
                         ]
        )


        markdown = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        block_list = markdown_to_blocks(markdown)
        self.assertEqual(block_list,
                         ["This is **bolded** paragraph",
                          "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                          "* This is a list\n* with items"
                         ]
        )

if __name__ == "__main__":
    unittest.main()
