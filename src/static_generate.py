import os, pathlib
from block_to_html import markdown_to_html_node
from htmlnode import HtmlNode

def extract_title(markdown):
    lines = markdown.split("\n")
    for line in lines:
        if (line.startswith("#") and
            not line[1:].startswith("#")):
            return line[1:]
    raise Exception("could not find h1 header in markdown")

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    with open(from_path) as f:
        markdown_data = f.read()

    with open(template_path) as f:
        template_data = f.read()

    html_nodes = markdown_to_html_node(markdown_data)

    html_data = html_nodes.to_html()

    html_title = extract_title(markdown_data)

    with open(template_path) as f:
        static_html = f.read()

    static_html = static_html.replace("{{Title}}", html_title)
    static_html = static_html.replace("{{Content}}", html_data)

    dest_dir = os.path.dirname(dest_path)
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)

    with open(dest_path, "w") as f:
        f.write(static_html)

def generate_pages_recursively(dir_path_content, template_path, dest_dir_path):
    if os.path.exists(dir_path_content):
        #if not os.path.exists(dest_dir_path):
        #    print(f'Creating new directory at {dest_dir_path}')
        #    os.mkdir(dest_dir_path)
        print(f'Checking directory at {dir_path_content} for markdown files')
        list_dir = os.listdir(dir_path_content)

        for element in list_dir:
            new_path = pathlib.Path(dir_path_content, element)
            if os.path.isfile(new_path):
                if element.endswith(".md"):
                    new_ext_name = element[:len(element) - 2] + "html"
                    new_dest_path = pathlib.Path(dest_dir_path, new_ext_name)
                    print(f'Converting {element} to html at {new_dest_path}')
                    generate_page(new_path, template_path, new_dest_path)
            else:
                new_dest_path = pathlib.Path(dest_dir_path, element)
                print(f'Recursively checking for markdown files at {new_dest_path}')
                generate_pages_recursively(new_path, template_path, new_dest_path)
    else:
        raise Exception("invalid directory path")
