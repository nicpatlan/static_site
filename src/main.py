from copydir import copy_directory_to_directory
from static_generate import generate_page

source_dir = "static"
destination_dir = "public"

from_path = "content/index.md"
template_path = "template.html"
dest_path = "public/index.html"


def main():
    copy_directory_to_directory(source_dir, destination_dir)
    generate_page(from_path, template_path, dest_path)

main()
