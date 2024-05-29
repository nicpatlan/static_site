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
        if type(node) is TextNode:
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
                    else:
                        split_list.pop(0)
                if split_list:
                    split_list = split_list[0].split(delimiter, maxsplit=1)    
                if len(split_list) > 1:
                    closing_delimiter_found = not closing_delimiter_found
            if not closing_delimiter_found:
                raise Exception("could not find closing delimiter")
        else:
            new_nodes.extend(node)
    return new_nodes

