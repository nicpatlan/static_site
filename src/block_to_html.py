from block_markdown import (block_type_paragraph,
                            block_type_heading,
                            block_type_code,
                            block_type_quote,
                            block_type_unordered_list,
                            block_type_ordered_list,
                            markdown_to_blocks,
                            block_to_block_type)
from inline_markdown import text_to_textnodes
from textnode import text_node_to_html_node
from htmlnode import (ParentNode,
                      LeafNode)

def heading_block_to_htmlnode(block):
    hash_count = 0
    if len(block) > 0:
        for c in block[0]:
            if c == "#":
                hash_count += 1
            else:
                break
    tag = "h" + str(hash_count)

    text_nodes = text_to_textnodes(block[hash_count + 1:])

    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return ParentNode(tag, html_nodes)

def paragraph_block_to_htmlnode(block):
    text_nodes = text_to_textnodes(block)
    
    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return ParentNode("p", html_nodes)

def quote_block_to_htmlnode(block):
    split_block = block.split(">")
    
    text_nodes = []
    for text in split_block:
        if text == "":
            continue
        new_nodes = text_to_textnodes(text)
        for node in new_nodes:
            text_nodes.append(node)

    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return ParentNode("blockquote", html_nodes)


def code_block_to_htmlnode(block):
    text_nodes = text_to_textnodes(block[2:len(block) - 2])

    html_nodes = []
    for node in text_nodes:
        html_nodes.append(text_node_to_html_node(node))

    return ParentNode("pre", html_nodes)

def unordered_list_block_to_htmlnode(block):
    list_items = block.split("\n")

    item_nodes = []
    html_nodes = []
    for item in list_items:
        if item == "":
            continue
        children = []
        #html_nodes.append(LeafNode("li", ""))
        item_nodes = text_to_textnodes(item[2:])
        for node in item_nodes:
            children.append(text_node_to_html_node(node))
        #html_nodes.append(LeafNode("li", ""))
        html_nodes.append(ParentNode("li", children))

    return ParentNode("ul", html_nodes)

def ordered_list_block_to_htmlnode(block):
    list_items = block.split("\n")

    item_nodes = []
    html_nodes = []
    for item in list_items:
        if item == "":
            continue
        children = []
        #html_nodes.append(LeafNode("li", ""))
        item_nodes = text_to_textnodes(item[3:])
        for node in item_nodes:
            children.append(text_node_to_html_node(node))
        #html_nodes.append(LeafNode("li", ""))
        html_nodes.append(ParentNode("li", children))

    return ParentNode("ol", html_nodes)

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    
    all_blocks = []
    for block in blocks:
        block_type = block_to_block_type(block)
        block_htmlnodes = []
        if block_type == block_type_paragraph:
            block_htmlnodes = paragraph_block_to_htmlnode(block)
        elif block_type == block_type_heading:
            block_htmlnodes = heading_block_to_htmlnode(block)
        elif block_type == block_type_code:
            block_htmlnodes = code_block_to_htmlnode(block)
        elif block_type == block_type_quote:
            block_htmlnodes = quote_block_to_htmlnode(block)
        elif block_type == block_type_unordered_list:
            block_htmlnodes = unordered_list_block_to_htmlnode(block)
        elif block_type == block_type_ordered_list:
            block_htmlnodes = ordered_list_block_to_htmlnode(block)
        else:
            raise Exception("unknown block type")
        all_blocks.append(block_htmlnodes)
    return ParentNode("div", all_blocks)
