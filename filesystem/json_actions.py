import json
import os
import platform

def pop_element_write_json(location, element_index):
    data_list = read_json_file(location)

    if isinstance(data_list, list):
        element = data_list.pop(element_index)
    else:
        raise Exception("cannot pop if not list")

    write_json(location, data_list)
    return element

def get_first_item_json(directory):
    # parse list / get first item from list
    data_list = read_json_file(directory)
    return data_list[0]

def read_json_file(file_loc):
    with open(file_loc) as json_file:
        return json.load(json_file)
    # return data

def write_json(file_loc, data):
    with open(file_loc, mode='w') as json_file:
        json.dump(data, json_file, indent=4)

def append_json(file_name, base_data, entity):
    base_data.append(entity)
    with open(file_name, mode='w') as json_file:
        json.dump(base_data, json_file, indent=4)

def check_file_exists(directory=None, file_name=None, dir_file_name=None):
    file_exists = False
    if dir_file_name:
        if os.path.exists(dir_file_name):
            file_exists = True
    else:
        if platform.system() == "Windows":
            file_path = directory + "\\" + file_name
        elif platform.system() == "Linux":
            file_path = directory + "/" + file_name

        if os.path.exists(file_path):
            file_exists = True
    return file_exists

def create_json(directory=None, file_name=None, dir_fname=None):
    if dir_fname:
        file_path = dir_fname
    else:
        file_path = directory + "\\" + file_name
    newfile = open(file_path, 'w+')
    newfile.write("[{\"filename\":\"\"}]")
    newfile.close()
