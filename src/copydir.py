import os, shutil

def copy_directory_to_directory(path, base_dir):
    print(f'Deleting {base_dir} directory')
    if os.path.exists(path):
        if os.path.exists(base_dir):
            shutil.rmtree(base_dir)
        os.mkdir(base_dir)
        file_dir_list = os.listdir(path)
        print(f'Copying directory at {path} to directory at {base_dir}')
        for element in file_dir_list:
            element_path = os.path.join(path, element)
            if os.path.isfile(element_path):
                base_dir_path = os.path.join(base_dir, element)
                shutil.copy(element_path, base_dir_path)
            else:
                new_base_dir = os.path.join(base_dir, element)
                copy_directory_to_directory(element_path, new_base_dir)
    else:
        raise Exception("invalid directory path")

