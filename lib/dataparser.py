import filesystem.json_actions as json_actions
import getpass
import filesystem.dir_actions as dir_actions


class Parser:

    def __init__(self):
        pass

    def format_item_kv(self, content_type, content):
        item = {}
        item["content_type"] = content_type
        item["item"] = content
        return item

    def get_content_parameters(self, kv):
        if not isinstance(kv, str):
            content_parameters = kv
        else:
            # open file and parse first list of content
            location = kv % getpass.getuser()
            content_parameters = json_actions.pop_element_write_json(location, 0)
        return content_parameters

    def value_exists_in_kv(self, list_kv, entity, key):
        for item in list_kv:
            value = item[key]
            if entity == value:
                return True
        return False

    def substr(self, stra, strb):
        if "%s" in stra:
            return stra % strb
        else:
            return stra

    def substr_bool(self, bval, stra, strb):
        if bval:
            new_str = stra % strb
        else:
            new_str = stra
        return new_str

    def get_values_from_kv_pairs(self, data):
        values = []
        for item in data:
            for k in item:
                values.append(item[k])
        return values

    def get_values_json(self, directory, filename):
        directory = dir_actions.unite_dir_with_fname(directory, filename)

        data = json_actions.read_json_file(directory)

        return tuple(self.get_values_from_kv_pairs(data))

    # TODO: rename to format text
    def format_caption(self, format_rules, info):
        if len(format_rules) == 0:
            return info
        else:
            caption = ""
            for item in format_rules:
                for key in item:
                    if (info[item[key]] is not None
                       and info[item[key]] != ""):
                        caption = caption + key % info[item[key]]
            return caption

    def format_poem(self, poem_record, author_record):
        # title
        poem = poem_record[1] + "\n"
        # author
        poem += "by " + author_record[1] + " " + author_record[2] + "\n\n"
        # poem
        poem += poem_record[3]
        return poem

    @staticmethod
    def get_anime_info(directory):
        # directory = directory + "\infogeneral.json"
        directory = directory + "/infogeneral.json"
        anime_data = json_actions.read_json_file(directory)

        english_name = anime_data["English Name"]
        japanese_name = anime_data["Japanese Name"]
        year = anime_data["Year"]

        return english_name, japanese_name, year

    @staticmethod
    def get_artist_info(directory1, artist_name):
        directory = directory1 + r"\artists.json"
        artist_data = json_actions.read_json_file(directory)

        print("name: " + artist_name + " directory: " + directory)
        name = ""
        website = ""
        artstation = ""
        deviantart = ""

        # TODO: when found - quit loop
        # find info about artist in the json file
        for i in artist_data:

            name1 = i["Name"]
            # print(name1)
            if name1 == artist_name:
                name = i["Name"]
                if i["website"]:
                    website = i["website"]
                if i["artstation"]:
                    artstation = i["artstation"]
                if i["deviantart"]:
                    deviantart = i["deviantart"]
                return name, website, artstation, deviantart
            # else:
            #    return name, website, artstation, deviantart
                # TODO: return just empty is file has no artist name

        # name1 = artist_data[0]["Name"]
        # while name1 != artist_name:

        return name, website, artstation, deviantart

    # @staticmethod
    # def get_photographers_info(directory):
    #     if platform.system() == "Windows":
    #         directory = directory + "\infogeneral.json"
    #     elif platform.system() == "Linux":
    #         directory = directory + "/infogeneral.json"
    #     fileman = FileManager()
    #     photographer_data = fileman.read_json_file(directory)

    #     name_surname = photographer_data["NameSurname"]
    #     website = photographer_data["WebSite"]
    #     tumblr = photographer_data["Tumblr"]
    #     instragram = photographer_data["Instagram"]
    #     fivepx = photographer_data["500px"]
    #     flickr = photographer_data["flickr"]

    #     return name_surname, website, tumblr, instragram, fivepx, flickr
