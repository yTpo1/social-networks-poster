import filesystem.json_actions as json_actions
import filesystem.dir_actions as dir_actions
from lib.dataparser import Parser as DataParser
#import random
#import getpass


class FileChooser:
    def get_file(self, selection_alg, recursive_folders,
                 directory, history_file, hist_file_type):
        """
        Get file(image) by specified algorithm, and folder structure
        return: file_loc, dir_only, file_name
        """

        if selection_alg == "random":
            return self.get_random_file(recursive_folders, directory,
                                        history_file, hist_file_type)
        elif selection_alg == "list":
            return self.get_files_from_list(directory)
        elif selection_alg == "direct":
            return directory
        else:
            raise Exception("Unsupported selection algorithm")

    def get_files_from_list(self, directory):
        # parse list / get first item from list
        broadcast_queue = json_actions.read_json_file(directory)

        # detele the first item from the list

        # return directories to files
        return broadcast_queue[0]

    def get_random_file(self, many_folders, content_dir, history_file,
                        hist_file_type):
        used_history = self.get_history(history_file, hist_file_type)

        directory, dir_fname, random_filename = self.select_random_unused_file(
                                                    many_folders,
                                                    content_dir, used_history)

        # record using - write the selected image name to the json file
        self.record_using_file(hist_file_type, history_file, used_history,
                               dir_fname)

        return dir_fname, directory, random_filename

    def get_history(self, history_file, file_type):
        if file_type == "json":
            return json_actions.read_json_file(history_file)
        elif file_type == "database":
            return None

    def record_using_file(self, file_type, history_file, used_history_data,
                          used_file):
        if file_type == "json":
            entity = {'filename': used_file}
            used_history_data.append(entity)
            json_actions.write_json(history_file, used_history_data)
        elif file_type == "database":
            pass

    def select_random_unused_file(self, bool_many_folders, cdir,
                                  used_photos_data):
        if bool_many_folders:
            # select random folder in currect directory
            directory = dir_actions.select_random_folder(cdir)
        else:
            directory = cdir

        dataparser = DataParser()
        same_photo = True
        while same_photo:
            # select a random file name from path
            random_filename = dir_actions.select_rand_file(directory)

            # random_filename_path = directory + "\\" + random_filename
            random_filename_path = directory + "/" + random_filename

            # check if filename was used before
            same_photo = dataparser.value_exists_in_kv(
                                                       used_photos_data,
                                                       random_filename_path,
                                                       "filename")
            # check if its not infogeneral.json
            if same_photo == False and random_filename == "infogeneral.json":
                same_photo = True

            # try a different folder
            if same_photo and bool_many_folders:
                directory = dir_actions.select_random_folder(cdir)

        return directory, random_filename_path, random_filename

    def select_random_unused_file_v3(self):
        # TODO: implement
        # get list of dir files

        # random num from range

        # check if file used before, else choose new random

        # return random file
        pass

    def select_random_unused_file_v2(self, bool_many_folders, cdir,
                                     used_photos_data):
        if bool_many_folders:
            # select random folder in currect directory
            directory = dir_actions.select_random_folder(cdir)
        else:
            directory = cdir

        dataparser = DataParser()
        same_photo = True
        while same_photo:
            # select a random file name from path
            random_filename = dir_actions.select_rand_file(directory)

            # random_filename_path = directory + "\\" + random_filename
            random_filename_path = directory + "/" + random_filename

            # check if filename was used before
            same_photo = dataparser.value_exists_in_kv(
                                        used_photos_data,
                                        random_filename_path,
                                        "filename")
            # try a different folder
            if same_photo and bool_many_folders:
                directory = dir_actions.select_random_folder(cdir)

        return directory, random_filename_path, random_filename

