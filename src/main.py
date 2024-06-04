from copydir import copy_directory_to_directory
from static_generate import generate_pages_recursively

source_dir = "static"
destination_dir = "public"

from_path = "content"
template_path = "template.html"
dest_path = "public"


def main():
    copy_directory_to_directory(source_dir, destination_dir)
    generate_pages_recursively(from_path, template_path, dest_path)

main()
