import unittest
from lib.dataparser import Parser
from os.path import expanduser
from test.mock_info import Mockinfo


class TestParser(unittest.TestCase):

    def setUp(self):
        self.mockinfo = Mockinfo()
        self.parser = Parser()

        self.scifi_data = (11, 'Aedel Fakhrie', '',
                           'https://www.artstation.com/aedel',
                           '', None, None, None)
        self.expected_scifi = 'Artist: Aedel Fakhrie | ' \
                              '<a href="https://www.artstation.com/aedel">'\
                              ' Artstation </a> |'

    def test_substr(self):
        expected = "Photo by: Yours Truly "
        stra = "Photo by: %s "
        strb = "Yours Truly"

        result = self.parser.substr(stra, strb)
        self.assertEqual(expected, result)

        expected2 = "Yours Truly"
        result2 = self.parser.substr(strb, stra)
        self.assertEqual(expected2, result2)

    def test_format_caption_travel(self):
        expected = 'Photo by: Ales Krivec  | '\
                   '<a href="https://www.instagram.com/dreamypixels">'\
                   ' Instagram </a> |'
        format_caption = [
            {"Photo by: %s ": 0},
            {' | <a href="%s"> Instagram </a> |': 3}
            ]
        parser = Parser()
        caption_result = parser.format_caption(
                                               format_caption,
                                               self.mockinfo.travel_values
                                               )
        self.assertEqual(expected, caption_result)

    def test_format_caption_scifi(self):
        format_rules_scifi = [
            {"Artist: %s": 1},
            {' | <a href="%s"> Artstation </a> |': 3},
            {' | <a href="%s"> Instagram </a> |': 5},
            {' | <a href="%s"> Deviantart </a> |': 4},
            {' | <a href="%s"> Website </a> |': 2}
            ]
        result_text_scifi = parser.format_caption(format_rules_scifi,
                                                  self.scifi_data)
        self.assertEqual(self.expected_scifi, result_text_scifi)

    def test_substr_bool(self):
        parser = Parser()

        result_a = parser.substr_bool(True, "Hello %s", "Bye")
        self.assertEqual("Hello Bye", result_a)

        result_b = parser.substr_bool(False, "Hello", "Bye")
        self.assertEqual("Hello", result_b)

    def test_get_values_from_kv_pairs(self):
        parser = Parser()

        result = parser.get_values_from_kv_pairs(self.mockinfo.infogeneral)

        self.assertEqual(self.mockinfo.travel_values_list, result)

    def test_get_values_json(self):
        expected_info = "Ales Krivec", "", "",\
                        "https://www.instagram.com/dreamypixels", "",\
                        "https://www.facebook.com/aleskphotography",\
                        "https://500px.com/gljivec", "", ""

        parser = Parser()

        home = expanduser("~")
        test_dir = home + "/Projects/social-networks-poster/test/mock_data"

        info = parser.get_values_json(self.mockinfo.mockdir, "infogeneral.json")

        self.assertEqual(expected_info, info)


if __name__ == "__main__":
    unittest.main()
