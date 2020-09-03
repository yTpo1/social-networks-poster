"""Utils for getting items names from directories"""
import os
import shutil
import random
import platform

def copy_file(file_loc, dest_dir):
    shutil.copy(file_loc, dest_dir)

def move_file(source, dest, filename):
    os.rename(source + filename, dest + filename)

def delete_file(file_path_name):
    os.remove(file_path_name)

def get_file_extension(path):
    path_split = os.path.splitext(path)
    return path_split[1]

def check_file_exists(file_path_name):
    return os.path.exists(file_path_name)

def unite_dir_with_fname(directory, fname):
    if platform.system() == "Windows":
        directory = directory + "\\" + fname
    elif platform.system() == "Linux":
        directory = directory + "/" + fname
    return directory

def get_files_in_dir(directory):
    return os.listdir(directory)

def select_random_folder(directory):
    dir_list = get_list_of_dirs(directory)
    random_dir = random.choice(dir_list)
    return random_dir

def select_rand_file(directory):
    """Select a random file name from path
    example: filename.jpg, filename.mp3"""
    random_filename = random.choice([
        x for x in os.listdir(directory)
        if os.path.isfile(os.path.join(directory, x))
    ])
    return random_filename

def get_list_of_dirs(directory):
    """ get all the folder (directories) in the selected path and store them in
    a list """
    list_of_directories_with_folder_names = [os.path.join(directory, f)
                         for f in os.listdir(directory)
                         if os.path.isdir(os.path.join(directory, f))]

    return list_of_directories_with_folder_names
