import unittest
from test.mock_info import Mockinfo
import filesystem.dir_actions as dir_actions


class TestDirectoryScanner(unittest.TestCase):

    def setUp(self):
        self.mock = Mockinfo()

    def test_unite_dir_with_fname(self):
        pass

    def test_get_files_in_dir(self):
        result = dir_actions.get_files_in_dir(self.mock.mockdirwfiles)

        result.sort()

        self.assertEqual(self.mock.mockfilesindir, result)


    def test_get_list_of_dirs(self):
        folders = dir_actions.get_list_of_dirs(self.mock.mockmultidir)

        self.assertTrue(all(elem in self.mock.mockmultidircontents for elem in folders))

    def test_select_rand_file(self):
        rand_file = dir_actions.select_rand_file(self.mock.mockdirwfiles)

        self.assertTrue(rand_file in self.mock.mockfilesindir)

    def test_select_random_folder(self):
        rand_folder_dir = dir_actions.select_random_folder(self.mock.mockmultidir)

        self.assertTrue(rand_folder_dir in self.mock.mockmultidircontents)


if __name__ == "__main__":
    unittest.main()
