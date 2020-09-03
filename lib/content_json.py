import getpass
from lib.dataparser import Parser as DataParser
from filechooser import FileChooser


class ContentJson:
    def __init__(self):
        self.filechooser = FileChooser()

    def get_content(self, content_parameters, content_type):
        parser = DataParser()
        content = []
        info = None
        # print(content_parameters)
        for content_params in content_parameters:
            # print(content_params)
            if content_params["selection_alg"] == "description":
                description = self.filechooser.get_content_description(
                    content.pop(),
                    content_params,
                    info,
                    content_type)
                content.append(description)
            else:
                # returns: file_dir, dir_only, file_only
                info = self.new_get_content(content_params)
                if isinstance(info, str):
                    item = parser.format_item_kv(
                                        content_params["content_type"],
                                        info)
                else:
                    item = parser.format_item_kv(
                                    content_params["content_type"],
                                    info[0])
                    if len(content_parameters) == 1:
                        tmp_list = []
                        tmp_list.append(item)
                        item = parser.format_item_kv(
                                        content_params["content_type"],
                                        tmp_list)

                if content_type == 'list':
                    tmp_list = []
                    tmp_list.append(item)
                    item = parser.format_item_kv(
                                    content_params["content_type"],
                                    tmp_list)

                content.append(item)
        return content

    def new_get_content(self, params, dir_only=None, file_only=None):
        directory = None
        br_history = None
        parser = DataParser()
        file_chooser = FileChooser()
        if (params["content_type"] == "image" or
                params["content_type"] == "audio"):
            if 'directory' in params:
                directory = parser.substr(stra=params['directory'],
                                          strb=getpass.getuser())
            if 'broadcast_history' in params:
                br_history = parser.substr(stra=params['broadcast_history'],
                                           strb=getpass.getuser())
            rec_fold = None
            if 'recursive_folders' in params:
                rec_fold = params['recursive_folders']
            br_hist_ftype = None
            if 'broadcast_history_ftype' in params:
                br_hist_ftype = params['broadcast_history_ftype']

            # file_loc, dir_only, file_name
            return file_chooser.get_file(
                    params['selection_alg'],
                    rec_fold,
                    directory,
                    br_history,
                    br_hist_ftype)
        elif params["content_type"] == "text":
            data_file = parser.substr(stra=params['data_file'],
                                      strb=getpass.getuser())

            general_info = file_chooser.get_text(
                    directory=dir_only,
                    selection_alg=params['selection_alg'],
                    data_file=data_file,
                    data_format=params['data_format'],
                    file_name=file_only)
            text = parser.format_caption(params['format_rules'], general_info)
            return text

    def get_content_description(self, content_item, content_params, info,
                                content_type):
        united_content = []
        united_content.append(content_item)

        # not supposed to be here
        dataparser = DataParser()

        item_text = dataparser.format_item_kv(
                "text",
                self.new_get_content(content_params, info[1], info[2]))
        united_content.append(item_text)

        item = dataparser.format_item_kv(content_type, united_content)
        return item
