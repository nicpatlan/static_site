import re
from textnode import (TextNode,
                      text_type_text,
                      text_type_bold,
                      text_type_italic,
                      text_type_code,
                      text_type_link,
                      text_type_image)

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if type(node) is TextNode and node.text_type == text_type_text:
            split_list = node.text.split(delimiter, maxsplit=1)
            closing_delimiter_found = False
            while split_list:
                if closing_delimiter_found and len(split_list) > 1:
                    if split_list[0] != "":
                        new_nodes.extend([TextNode(split_list.pop(0), text_type)])
                    else:
                        split_list.pop(0)
                else:
                    if split_list[0] != "":
                        new_nodes.extend([TextNode(split_list.pop(0), text_type_text)])
                        if len(split_list) == 0:
                            closing_delimiter_found = True
                    else:
                        split_list.pop(0)
                if split_list:
                    split_list = split_list[0].split(delimiter, maxsplit=1)    
                if len(split_list) > 1:
                    closing_delimiter_found = not closing_delimiter_found
            if not closing_delimiter_found:
                raise Exception("could not find closing delimiter")
        else:
            new_nodes.append(node)
    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[(.*?)\]\((.*?)\)", text)

def extract_markdown_links(text):
    return re.findall(r"\[(.*?)\]\((.*?)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if type(node) is TextNode:
            image_tuples = extract_markdown_images(node.text)
            if not image_tuples:
                new_nodes.append(node)
                continue
            split_list = []
            for image in image_tuples:
                if not split_list:
                    split_list = node.text.split(f"![{image[0]}]({image[1]})", maxsplit=1)
                else:
                    split_list = split_list[0].split(f"![{image[0]}]({image[1]})", maxsplit=1)
                if split_list[0] != "":
                    new_nodes.extend([TextNode(split_list.pop(0), text_type_text), 
                                      TextNode(image[0], text_type_image, image[1])
                                     ])
                else:
                    split_list.pop(0)
                    new_nodes.append(TextNode(image[0], text_type_image, image[1]))
            if split_list and split_list[0] != "":
                new_nodes.append(TextNode(split_list.pop(0), text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if type(node) is TextNode:
            link_tuples = extract_markdown_links(node.text)
            if not link_tuples:
                new_nodes.append(node)
                continue
            split_list = []
            for link in link_tuples:
                if not split_list:
                    split_list = node.text.split(f"[{link[0]}]({link[1]})", maxsplit=1)
                else:
                    split_list = split_list[0].split(f"[{link[0]}]({link[1]})", maxsplit=1)
                if split_list[0] != "":
                    new_nodes.extend([TextNode(split_list.pop(0), text_type_text), 
                                      TextNode(link[0], text_type_link, link[1])
                                     ])
                else:
                    split_list.pop(0)
                    new_nodes.append(TextNode(link[0], text_type_link, link[1]))
            if split_list and split_list[0] != "":
                new_nodes.append(TextNode(split_list.pop(0), text_type_text))
        else:
            new_nodes.append(node)
    return new_nodes

def text_to_textnodes(text):
    node_list = split_nodes_delimiter(
            split_nodes_delimiter(
                split_nodes_delimiter(
                    [TextNode(text, text_type_text)],
                    "**", 
                    text_type_bold
                    ),
                "`",
                text_type_code
                ),
            "*",
            text_type_italic
            )
    return split_nodes_link(split_nodes_image(node_list))

