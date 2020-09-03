import unittest
import getpass
from contentparser import ContentParser


class TestContentParser(unittest.TestCase):

    def setUp(self):
        self.json_quote = {'social_network': 'telegram',
                           'blog_username': '@username', 'content_type': 'text',
                           'content':
                [{'content_type': 'text', 'selection_alg': 'random', 'data_format':
                    'database', 'data_file':
                    '/media/%s/ae69/db/data.db',
                    'format_rules': [{'"%s': 0}, {'"\n\n- %s': 1}]}], 'tags': ''}
        self.json_travel = {'social_network': 'telegram',
                            'blog_username': '@travel_and_nature',
                            'content_type': 'image+text',
                            'content': [
                                {'content_type': 'image',
                                 'directory': '/media/%s/ab961601-37b0-4743-ae69-3e7a0c12370c/bloom/',
                                 'recursive_folders': True,
                                 'selection_alg': 'random',
                                 'broadcast_history_ftype': 'json',
                                 'broadcast_history': '/media/%s/ab961601-37b0-4743-ae69-3e7a0c12370c/Project_databases/used_tg_travel.json'},
                                {'content_type': 'text',
                                 'selection_alg': 'description',
                                 'data_format': 'json',
                                 'data_file': 'infogeneral.json', 'format_rules': [{'Photo by: %s ': 0}, {' | <a href="%s""> Instagram </a> |': 3}]}
                                ],
                            'tags': ''}
        self.json_scifi = {'social_network': 'telegram',
                           'blog_username': '@scifi_cyberpunk',
                           'content_type': 'image+text',
                           'content': [{'content_type': 'image',
'directory': '/media/%s/ab961601-37b0-4743-ae69-3e7a0c12370c/Cyberpunk all/',
'recursive_folders': False, 'selection_alg': 'random',
'broadcast_history_ftype': 'json', 'broadcast_history':
'/media/%s/ab961601-37b0-4743-ae69-3e7a0c12370c/Project_databases/used_tg_scifi.json'},
{'content_type': 'text', 'selection_alg': 'description', 'data_format':
    'database', 'data_file': '/media/%s/cyberpunk_images.db', 'format_rules':
    [{'Artist: %s': 1}, {' | <a href="%s"> Artstation </a> |': 3}, {'| <a href="%s"> Instagram </a> |': 5}, {' | <a href="%s"> Deviantart </a> |': 4}, {' | <a href="%s"> Website </a> |': 2}]}], 'tags': ''}

        self.json_cat = {'social_network': 'telegram', 'blog_username': '@cat', 'content_type': 'image', 'content': [{'content_type': 'image', 'directory': '/media/%s/cat/', 'recursive_folders': False, 'selection_alg': 'random', 'broadcast_history_ftype': 'json', 'broadcast_history': '/media/%s/ab961601-37b0-4743-ae69-3e7a0c12370c/Project_databases/used_tg_cats.json'}], 'tags': ''}

    def test_parser_cat(self):
        content_parser = ContentParser()
        content = content_parser.get_content_requirements(self.json_cat)

        self.assertEqual(content.social_network, "telegram")
        self.assertEqual(content.blog_username, "@cat")
        self.assertEqual(content.tags, "")

        self.assertEqual(len(content.content_item), 1)

        self.assertEqual(content.content_item[0].content_type, "image")
        self.assertEqual(content.content_item[0].selection_alg, "random")
        self.assertEqual(content.content_item[0].history_ftype, "json")
        self.assertEqual(content.content_item[0].directory,
                         "/media/%s/cat/" % getpass.getuser())
        self.assertEqual(content.content_item[0].recursive_folders, False)

    def test_parser_scifi(self):
        content_parser = ContentParser()
        content = content_parser.get_content_requirements(self.json_scifi)

        self.assertEqual(content.social_network, "telegram")
        self.assertEqual(content.blog_username, "@scifi_cyberpunk")
        self.assertEqual(content.tags, "")

        self.assertEqual(len(content.content_item), 2)

        self.assertEqual(content.content_item[0].content_type, "image")
        self.assertEqual(content.content_item[0].selection_alg, "random")
        self.assertEqual(content.content_item[0].history_ftype, "json")

        self.assertEqual(content.content_item[1].content_type, "text")
        self.assertEqual(content.content_item[1].selection_alg, "description")
        self.assertEqual(content.content_item[1].data_format, "database")
        self.assertEqual(content.content_item[1].data_file,
                         "/media/%s/cyberpunk_images.db" % getpass.getuser())

    def test_parser_travel(self):
        content_parser = ContentParser()
        content = content_parser.get_content_requirements(self.json_travel)

        self.assertEqual(content.social_network, "telegram")
        self.assertEqual(content.blog_username, "@travel_and_nature")
        self.assertEqual(content.tags, "")

        self.assertEqual(len(content.content_item), 2)

        self.assertEqual(content.content_item[0].content_type, "image")
        self.assertEqual(content.content_item[0].selection_alg, "random")
        self.assertEqual(content.content_item[0].history_ftype, "json")

        self.assertEqual(content.content_item[1].content_type, "text")
        self.assertEqual(content.content_item[1].selection_alg, "description")
        self.assertEqual(content.content_item[1].data_format, "json")
        self.assertEqual(content.content_item[1].data_file, "infogeneral.json")

    def test_parser_quotes(self):
        content_parser = ContentParser()
        content = content_parser.get_content_requirements(self.json_quote)

        self.assertEqual(content.social_network, "telegram")
        self.assertEqual(content.blog_username, "@username")
        self.assertEqual(content.tags, "")

        self.assertEqual(content.content_item[0].content_type, "text")
        self.assertEqual(content.content_item[0].selection_alg, "random")
        self.assertEqual(content.content_item[0].data_file,
                         "/media/%s/ae69/db/data.db" % getpass.getuser())


if __name__ == "__main__":
    unittest.main()
