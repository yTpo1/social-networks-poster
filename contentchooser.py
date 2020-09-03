from filechooser import FileChooser
from textchooser import TextChooser
from lib.dataparser import Parser


class ContentChooser:

    def create_item(self, content_item):
        parser = Parser()
        filechooser = FileChooser()
        textchooser = TextChooser()
        content_params = content_item.content_item[0]
        if content_params.content_type == "text":
            general_info = textchooser.get_text(
                content_params.selection_alg,
                content_params.data_file,
                content_params.data_format,
                None,
                None,
                application=content_item.application)
            if content_item.application == "poetry":
                content_item.item_text = parser.format_poem(
                                                        general_info[0],
                                                        general_info[1])
            else:
                content_item.item_text = parser.format_caption(
                    content_params.format_rules, general_info)
            return content_item
        elif content_params.content_type == "image":
            image_path = filechooser.get_file(content_params.selection_alg,
                                              content_params.recursive_folders,
                                              content_params.directory,
                                              content_params.history_loc,
                                              content_params.history_ftype)
            content_item.item_image_path = image_path[0]
            if len(content_item.content_item) > 1:
                general_info = textchooser.get_text(
                    content_item.content_item[1].selection_alg,
                    content_item.content_item[1].data_file,
                    content_item.content_item[1].data_format,
                    image_path[1],
                    image_path[2])
                content_item.item_text = parser.format_caption(
                    content_item.content_item[1].format_rules, general_info)
            return content_item
