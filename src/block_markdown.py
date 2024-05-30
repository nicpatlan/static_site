import re

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

def block_to_block_type(block):
    lines = block.split("\n")
    if not lines:
        raise Exception("block cannot be an empty string")

    if len(lines) == 1:
        if re.findall(r"^#{1,6} .*", lines[0]):
            return block_type_heading

    if re.findall(r"^``` *", lines[0]) != None:
        if re.findall(r"^``` *", lines[len(lines) - 1]):
            return block_type_code
    if lines[0][:1] == ">":
        for idx, line in enumerate(lines):
            if line[:1] != ">":
                break
            if idx == len(lines) - 1:
                return block_type_quote

    if len(lines[0]) > 1 and (lines[0][:2] == "* " or lines[0][:2] == "- "):
        for idx, line in enumerate(lines):
            if len(line) > 1 and (line[:2] == "* " or line[:2] == "- "):
                if idx == len(lines) - 1:
                    return block_type_unordered_list
                continue
            break
    if len(lines[0]) > 2 and lines[0][:3] == "1. ":
        ordered_value = 1
        for idx, line in enumerate(lines):
            if len(line) > 2 and int(line[:1]) == ordered_value and line[1:3] == ". ":
                ordered_value += 1
                if idx == len(lines) - 1:
                    return block_type_ordered_list
                continue
            break
    return block_type_paragraph
