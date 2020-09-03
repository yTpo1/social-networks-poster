import unittest
from test.mock_info import Mockinfo
from contentchooser import ContentChooser
from content import Content, ContentText, ContentImage


class TestContentChooser(unittest.TestCase):

    def setUp(self):
        self.mockinfo = Mockinfo()
        self.expected_cats_image = self.mockinfo.mockdirwfiles+'/file3.jpg'
        self.expected_travel_image = self.mockinfo.mockmultidir+'/Folder3/file3.jpg'
        self.expected_travel_text = 'Photo by: Ales Krivec  ' \
                            '| <a href="https://www.instagram.com/dreamypixels"">' \
                                    ' Instagram </a> |'
        self.expected_scifi_image = self.mockinfo.mockdirwfiles+'/file3.jpg'
        self.expected_scifi_text = 'Artist: Elijah McNeal |' \
                            ' <a href="https://www.artstation.com/el1j4h">' \
                            ' Artstation </a> |'


    def setup_content_item_text(self):
        content = Content("telegram", "@quotes_literature", "",
                application="quotes")
        format_rules = [{"\"%s":0},{"\"\n\n- %s":1}]
        text = ContentText("text", "random", "database",
                           self.mockinfo.mockdb, format_rules, "")
        content.add_content_item(text)
        return content

    def setup_content_item_image_cat(self):
        tags = ["kitty", "kitten", "cat", "cute", "pet", "cutie", "animals"]
        content = Content("telegram", "@image_cat", tags, application="cats")
        image = ContentImage("image", "random", self.mockinfo.mockdirwfiles,
                             False, "json", self.mockinfo.historyfile)
        content.add_content_item(image)
        return content

    def setup_content_item_image_travel(self):
        tags = ""
        format_rules = [{"Photo by: %s ": 0},
            {" | <a href=\"%s\"\"> Instagram </a> |": 3}]
        content = Content("telegram", "@travel", tags, application="travel")
        image = ContentImage("image", "random", self.mockinfo.mockmultidir,
                             True, "json", self.mockinfo.historyfilerecdir)
        text = ContentText("text", "description", "json",
                           "infogeneral.json", format_rules, "")
        content.add_content_item(image)
        content.add_content_item(text)
        return content

    def setup_content_item_image_scifi(self):
        tags = ""
        format_rules = [
                    {"Artist: %s":1},
                    {" | <a href=\"%s\"> Artstation </a> |":3},
                    {" | <a href=\"%s\"> Instagram </a> |":5},
                    {" | <a href=\"%s\"> Deviantart </a> |":4},
                    {" | <a href=\"%s\"> Website </a> |":2}
                    ]
        content = Content("telegram", "@scifi", tags, application="scifi")
        image = ContentImage("image", "random", self.mockinfo.mockdirwfiles,
                             False, "json", self.mockinfo.historyfile)
        text = ContentText("text", "description", "database",
                           self.mockinfo.mockdb, format_rules, "")
        content.add_content_item(image)
        content.add_content_item(text)
        return content

    def test_create_item_image_scifi(self):
        content_params = self.setup_content_item_image_scifi()
        cont_chooser = ContentChooser()
        item = cont_chooser.create_item(content_params)
        self.assertEqual(item.item_image_path, self.expected_scifi_image)
        self.assertEqual(item.item_text, self.expected_scifi_text)

    def test_create_item_image_travel(self):
        content_params = self.setup_content_item_image_travel()
        cont_chooser = ContentChooser()
        item = cont_chooser.create_item(content_params)
        self.assertEqual(item.item_image_path, self.expected_travel_image)
        self.assertEqual(item.item_text, self.expected_travel_text)

    def test_create_item_image_cat(self):
        content_params = self.setup_content_item_image_cat()
        cont_chooser = ContentChooser()
        item = cont_chooser.create_item(content_params)
        self.assertEqual(item.item_image_path, self.expected_cats_image)

    def test_create_item_text(self):
        content_params = self.setup_content_item_text()
        cont_chooser = ContentChooser()
        item = cont_chooser.create_item(content_params)
        self.assertEqual(item.item_text, self.mockinfo.expected_quote_formated)
        self.assertEqual(len(item.item_text),
                len(self.mockinfo.expected_quote_formated))


if __name__ == "__main__":
    unittest.main()
