import os
#from filemanager import FileManager
import filesystem.json_actions as json_actions


class Mockinfo:
    def __init__(self):
        self.home = os.path.expanduser("~")
        self.testdir = os.path.dirname(os.path.abspath(__file__))
        self.mockdir = self.testdir + "/mock_data"
        self.mockdb = self.mockdir+'/mock.db'
        self.mockdirwfiles = self.mockdir+"/Mockdirwithfiles"
        self.mockfilesindir = ["file1.jpg", "file2.jpg", "file3.jpg"]
        self.mockmultidir = self.mockdir+"/Mockmultidir"
        self.mockmultidircontents = [
            self.mockmultidir+"/Folder1",
            self.mockmultidir+"/Folder2",
            self.mockmultidir+"/Folder3"]
        self.testdir = os.path.dirname(os.path.abspath(__file__))
        self.historyfile = self.mockdir + "/used_files.json"
        self.historyfilerecdir = self.mockdir+"/used_files_rec_dir.json"
        self.usedfiles = [{'filename': ''},
                          {'filename': self.mockdirwfiles+'/file1.jpg'},
                          {'filename': self.mockdirwfiles+'/file2.jpg'}]
        self.usedfiles_rec_dir = [
                {'filename': ''},
                {'filename': self.mockmultidir+'/Folder1/file1.jpg'},
                {'filename': self.mockmultidir+'/Folder2/file2.jpg'},
                {'filename': self.mockmultidir+'/Folder1/infogeneral.json'},
                {'filename': self.mockmultidir+'/Folder2/infogeneral.json'},
                {'filename': self.mockmultidir+'/Folder3/infogeneral.json'}]

        self.infogeneral = [
            {"NameSurname": "Ales Krivec"},
            {"WebSite": ""},
            {"Tumblr": ""},
            {"Instagram": "https://www.instagram.com/dreamypixels"},
            {"Twitter": ""},
            {"Facebook": "https://www.facebook.com/aleskphotography"},
            {"500px": "https://500px.com/gljivec"},
            {"flickr": ""},
            {"vsco": ""}
        ]
        self.travel_values = (
                "Ales Krivec",
                "", "",
                "https://www.instagram.com/dreamypixels",
                "",
                "https://www.facebook.com/aleskphotography",
                "https://500px.com/gljivec",
                "", ""
                )
        self.travel_values_list = list(self.travel_values)
        self.expected_quote_formated = '"A friend is someone who knows all about' \
                            ' you and still loves you."\n\n- Elbert Hubbard '
        self.expected_quote = "A friend is someone who knows all about" \
                            " you and still loves you."
        self.expected_quotes_author = "Elbert Hubbard "

        # self.content_image_final = [
        # {'content_type': 'image', 'item': self.mockdirwfiles+'/file3.jpg'}]

        self.fill_hist_file()
        self.content_text()
        self.content_file()
        self.content_filetextdb_nonrec()
        self.content_imgtxt_rec()
        self.content_list()

    def content_list(self):
        """TODO: Docstring for content_list.
        """
        self.cnt_prms_list = [
            [
                {
                    "content_type": "image",
                    "directory": self.mockdirwfiles+'/file3.jpg',
                    "selection_alg": "direct"
                },
                {
                    "content_type": "text",
                    "selection_alg": "direct",
                    "data_format": "txt",
                    "data_file": self.mockdir+'/testtext.txt',
                    "format_rules": []
                },
                {
                    "content_type": "image",
                    "directory": self.mockdirwfiles+'/file3.jpg',
                    "selection_alg": "direct"
                }
            ],
            []
        ]
        self.content_list_final = [
                {'content_type': 'image',
                 'item': [
                    {'content_type': 'image',
                     'item': self.mockdirwfiles+'/file3.jpg'}
                    ]
                 },
                {'content_type': 'text',
                 'item': [
                    {
                        'content_type': 'text',
                        'item': 'Hello\nthis is line 2\nwell done!!\n'
                    }]
                 },
                {'content_type': 'image',
                 'item': [
                    {'content_type': 'image',
                     'item': self.mockdirwfiles+'/file3.jpg'}
                    ]
                 }
                ]
        """
         [{'content_type': 'image', 'item': [{'content_type': 'image', 'item': '/home/ghost/Downloads/T
mp/pic.jpg'}]}, {'content_type': 'text', 'item': [{'content_type': 'text', 'item': 'this is beauty\n'}]},
 {'content_type': 'image', 'item': [{'content_type': 'image', 'item': '/home/ghost/Downloads/Tmp/song.mp3
'}]}]
        """

    def content_imgtxt_rec(self):
        self.cont_params_img_text_rec_fold = [
                    {
                        "content_type": "image",
                        "directory": self.mockmultidir,
                        "recursive_folders": True,
                        "selection_alg": "random",
                        "broadcast_history_ftype": "json",
                        "broadcast_history": self.historyfilerecdir
                        },
                    {
                        "content_type": "text",
                        "selection_alg": "description",
                        "data_format": "json",
                        "data_file": "infogeneral.json",
                        "format_rules": [
                            {"Photo by: %s ": 0},
                            {" | <a href=\"%s\"\"> Instagram </a> |": 3}
                            ]
                    }
                ]

        self.content_image_text_final = [{
            'content_type': 'image+text',
            'item': [
                {'content_type': 'image',
                    'item': self.mockmultidir+'/Folder3/file3.jpg'},
                {'content_type': 'text',
                    'item': 'Photo by: Ales Krivec  ' +
                    '| <a href="https://www.instagram.com/dreamypixels"">' +
                    ' Instagram </a> |'}
                ]
                }]

    def content_filetextdb_nonrec(self):
        # image+text db non-rec
        self.cont_imgtxt_db_nonrec = [
            {
                "content_type": "image",
                "directory": self.mockdirwfiles,
                "recursive_folders": False,
                "selection_alg": "random",
                "broadcast_history_ftype": "json",
                "broadcast_history": self.historyfile
            },
            {
                "content_type": "text",
                "selection_alg": "description",
                "data_format": "database",
                "data_file": self.mockdb,
                "format_rules": [
                    {"Artist: %s": 1},
                    {" | <a href=\"%s\"> Artstation </a> |": 3},
                    {" | <a href=\"%s\"> Instagram </a> |": 5},
                    {" | <a href=\"%s\"> Deviantart </a> |": 4},
                    {" | <a href=\"%s\"> Website </a> |": 2}
                    ]
            }
        ]
        self.content_imgtxt_final_scifi = [{
            'content_type': 'image+text',
            'item': [
                {'content_type': 'image',
                    'item': self.mockdirwfiles+'/file3.jpg'},
                {'content_type': 'text',
                    'item': 'Artist: Elijah McNeal |' +
                            ' <a href="https://www.artstation.com/el1j4h">' +
                            ' Artstation </a> |'}
                ]
                }]

    def content_text(self):
        # text format template
        self.cont_params_text = [
                {
                    "content_type": "text",
                    "selection_alg": "random",
                    "data_format": "database",
                    "data_file": self.mockdb,
                    "format_rules": [
                        {"\"%s": 0},
                        {"\"\n\n- %s": 1}
                        ]
                }
            ]
        self.content_text_final = [{
            'content_type': 'text',
            'item': '"A friend is someone who knows all about' +
                    ' you and still loves you."\n\n- Elbert Hubbard '
                }]

    def content_file(self):
        self.cnt_prms_img_dir_nrec = [{
                    "content_type": "image",
                    "directory": self.mockdirwfiles,
                    "recursive_folders": False,
                    "selection_alg": "random",
                    "broadcast_history_ftype": "json",
                    "broadcast_history": self.historyfile
                }]
        self.params_file_nonrecurs_dir = {
                    "content_type": "image",
                    "directory": self.mockdirwfiles,
                    "recursive_folders": False,
                    "selection_alg": "random",
                    "broadcast_history_ftype": "json",
                    "broadcast_history": self.historyfile
                }
        self.content_image_final = [
                {'content_type': 'image',
                 'item': [
                    {'content_type': 'image',
                     'item': self.mockdirwfiles+'/file3.jpg'}
                    ]
                 }]

    def fill_hist_file(self):
        #fileman = FileManager()
        json_actions.write_json(self.historyfile, self.usedfiles)
        json_actions.write_json(self.historyfilerecdir, self.usedfiles_rec_dir)
