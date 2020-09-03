

class Content:
    def __init__(self, social_network, blog_username, tags, application):
        self.social_network = social_network
        self.blog_username = blog_username
        self.tags = tags
        self.application = application

        self.item_image_path = ""
        self.item_text = ""

        # rename to content settings on how to get / process / rules
        self.content_item = []

    def add_content_item(self, content_item):
        self.content_item.append(content_item)


# TODO: rename to content requirements / parameters
class ContentText:
    def __init__(self, content_type, selection_alg, data_format, data_file,
                 format_rules, history_loc):
        self.content_type = content_type  # ": "text","image"
        self.selection_alg = selection_alg  # ": "random",
        self.data_format = data_format  # ": "database",
        self.data_file = data_file    # ": "/media/%s/ab961601-37b0-4743-ae69-3e7a0c12370c/Project_databases/quotes_base.db",
        self.format_rules = format_rules  # ": [
        self.history_loc = history_loc


# TODO: rename to content requirements / parameters
class ContentImage:
    def __init__(self, content_type, selection_alg, directory,
                 recursive_folders, history_ftype, history_loc):
        self.content_type = content_type  # ": "text","image"
        self.selection_alg = selection_alg  # ": "random",

        self.directory = directory
        self.recursive_folders = recursive_folders
        self.history_ftype = history_ftype
        self.history_loc = history_loc

