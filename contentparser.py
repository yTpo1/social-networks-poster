import getpass
from content import Content, ContentText, ContentImage
from lib.dataparser import Parser as DataParser


class ContentParser:

    def get_content_requirements(self, json_options):
        social_network = json_options["social_network"]
        blog_username = json_options["blog_username"]
        tags = json_options["tags"]
        application = json_options["application"]

        content = Content(social_network, blog_username, tags, application)
        parser = DataParser()

        #content_item_format = json_options["content_type"]

        for item_param in json_options["content"]:
            if item_param["content_type"] == "text":
                data_file = parser.substr(stra=item_param["data_file"],
                                          strb=getpass.getuser())

                item_text = ContentText(item_param["content_type"],
                    item_param["selection_alg"], item_param["data_format"],
                    data_file, item_param["format_rules"],
                    None)
                content.add_content_item(item_text)
            elif item_param["content_type"] == "image":
                directory = parser.substr(stra=item_param["directory"],
                                          strb=getpass.getuser())
                br_history = parser.substr(stra=item_param['broadcast_history'],
                                           strb=getpass.getuser())

                item_image = ContentImage(item_param["content_type"],
                        item_param["selection_alg"],
                        directory,
                        item_param["recursive_folders"],
                        history_ftype=item_param["broadcast_history_ftype"],
                        history_loc=br_history)
                content.add_content_item(item_image)

        return content
