block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_unordered_list = "unordered_list"
block_type_ordered_list = "ordered_list"

def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    valid_blocks = []
    for block in blocks:
        block = block.strip()
        if block == "":
            continue
        valid_blocks.append(block)

    return valid_blocks
