import unittest

from block_markdown import (markdown_to_blocks,
                            block_to_block_type,
                            block_type_paragraph,
                            block_type_heading,
                            block_type_code,
                            block_type_quote,
                            block_type_unordered_list,
                            block_type_ordered_list)

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

    def test_block_to_block_type(self):
        heading_block = "# Heading1"
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, block_type_heading)

        heading_block = "###### Heading6"
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, block_type_heading)

        heading_block = "####### not a heading"
        block_type = block_to_block_type(heading_block)
        self.assertEqual(block_type, block_type_paragraph)

        code_block = "```\ncode block\n```"
        block_type = block_to_block_type(code_block)
        self.assertEqual(block_type, block_type_code)

        code_block = "```\nnot a code block"
        block_type = block_to_block_type(code_block)
        self.assertEqual(block_type, block_type_paragraph)

        quote_block = "> short quotes\n> are the best"
        block_type = block_to_block_type(quote_block)
        self.assertEqual(block_type, block_type_quote)

        quote_block = "> short quotes\n> are the best\nendquote"
        block_type = block_to_block_type(quote_block)
        self.assertEqual(block_type, block_type_paragraph)

        unordered_block = "* an item\n* another item\n* last item"
        block_type = block_to_block_type(unordered_block)
        self.assertEqual(block_type, block_type_unordered_list)

        unordered_block = "* an item\n* another item\nnot an item\n* last item"
        block_type = block_to_block_type(unordered_block)
        self.assertEqual(block_type, block_type_paragraph)

        ordered_block = "1. first item\n2. second item\n3. third item"
        block_type = block_to_block_type(ordered_block)
        self.assertEqual(block_type, block_type_ordered_list)

        ordered_block = "1. first item\n3. woops third item\n4. fourth item"
        block_type = block_to_block_type(ordered_block)
        self.assertEqual(block_type, block_type_paragraph)

        paragraph_block = "just a normal paragraph block"
        block_type = block_to_block_type(paragraph_block)
        self.assertEqual(block_type, block_type_paragraph)

        paragraph_block = " # something that starts with stuff\n* has lines that do weird stuff"
        block_type = block_to_block_type(paragraph_block)
        self.assertEqual(block_type, block_type_paragraph)

if __name__ == "__main__":
    unittest.main()
