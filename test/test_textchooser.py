import unittest

from test.mock_info import Mockinfo
from textchooser import TextChooser


class TestTextChooser(unittest.TestCase):
    def setUp(self):
        self.mockinfo = Mockinfo()

    def test_get_text(self):
        textchooser = TextChooser()
        text = textchooser.get_text(
                                "description",
                                "infogeneral.json",
                                "json",
                                self.mockinfo.mockdir)
        self.assertEqual(self.mockinfo.travel_values, text)

        text = textchooser.get_text(
                                "description",
                                "infogeneral.json",
                                "json",
                                self.mockinfo.mockdir)
        self.assertEqual(self.mockinfo.travel_values, text)


    def test_get_scifi_description(self):
        textchooser = TextChooser()
        filename = "file3.jpg"
        expected_record = (1, 'Elijah McNeal', None,
                'https://www.artstation.com/el1j4h',
                None, None, None, None)
        img_info = textchooser.get_scifi_description("sqlite", self.mockinfo.mockdb,
                filename)
        self.assertEqual(img_info, expected_record)
        #def get_scifi_description(self, db_engine, data_file, file_name):
        #self.assertEqual(quote[1], self.mockinfo.expected_quotes_author)

    def test_get_quote(self):
        textchooser = TextChooser()
        quote = textchooser.get_quote("sqlite", self.mockinfo.mockdb)
        self.assertEqual(quote[0], self.mockinfo.expected_quote)
        self.assertEqual(quote[1], self.mockinfo.expected_quotes_author)


if __name__ == "__main__":
    unittest.main()
