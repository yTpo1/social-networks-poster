import unittest
# import mock
#from os.path import expanduser
from test.mock_info import Mockinfo

#from filemanager import FileManager
import filesystem.json_actions as json_actions
import filesystem.txt_actions as txt_actions


class TestFileManager(unittest.TestCase):

    def setUp(self):
        self.mockinfo = Mockinfo()
        #self.fileman = FileManager()

        # populate queue file for test_pop_first_record_json
        self.queue_original_file_loc = self.mockinfo.mockdir+"/posting_queue_original.json"
        self.queue_file_loc = self.mockinfo.mockdir+"/posting_queue.json"
        queue_data_original = json_actions.read_json_file(
                                                self.queue_original_file_loc)
        json_actions.write_json(self.queue_file_loc, queue_data_original)

    # @mock.patch('lib.FileManager')
    def test_read_json_file(self):
        pass

    def test_pop_first_record_json(self):
        expected = [[]]
        element = json_actions.pop_element_write_json(self.queue_file_loc, 0)
        self.assertEqual('direct', element[0]['selection_alg'])

        result = json_actions.read_json_file(self.queue_file_loc)
        self.assertEqual(expected, result)

    def test_read_txt(self):
        expected = "Hello\nthis is line 2\nwell done!!\n"
        location = self.mockinfo.mockdir + "/testtext.txt"
        result = txt_actions.read_txt(location)
        self.assertEqual(expected, result)

        # loc2 = self.test_dir + '/she_walks_in_beauty.txt'
        # result2 = self.fileman.read_txt(loc2)
        # self.assertEqual(expected, result2)


if __name__ == "__main__":
    unittest.main()
