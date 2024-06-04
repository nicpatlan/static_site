import os
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
        os.mkdirs(dest_path)

    with open(dest_path, "w") as f:
        f.write(static_html)
