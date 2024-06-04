from copydir import copy_directory_to_directory

source_dir = "static"
destination_dir = "public"


def main():
    copy_directory_to_directory(source_dir, destination_dir)

main()
