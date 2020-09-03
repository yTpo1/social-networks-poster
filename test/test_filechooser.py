import unittest

from test.mock_info import Mockinfo
from filechooser import FileChooser


class TestFileChooser(unittest.TestCase):

    def setUp(self):
        self.mockinfo = Mockinfo()

    def test_get_file(self):
        pass

    def test_get_files_from_list(self):
        pass

    def test_get_random_file(self):
        pass

    def test_record_using_file(self):
        pass

    def test_select_random_unused_file(self):
        filech = FileChooser()
        directory, fpath, fname = filech.select_random_unused_file(
                                False,
                                self.mockinfo.mockdirwfiles,
                                self.mockinfo.usedfiles)
        self.assertNotEqual(self.mockinfo.mockdirwfiles+"/infogeneral.json", fpath)
        self.assertEqual(self.mockinfo.mockdirwfiles+"/file3.jpg", fpath)

    #def test_select_random_unused_file_json(self):
    #    filech = FileChooser()
    #    directory, fpath, fname = filech.select_random_unused_file(
    #                            False,
    #                            self.mockinfo.mockdirwfiles,
    #                            self.mockinfo.usedfiles)
    #    self.assertEqual(self.mockinfo.mockdirwfiles+"/file3.jpg", fpath)

    def test_get_history(self):
        filechooser = FileChooser()
        result = filechooser.get_history(self.mockinfo.historyfile, "json")
        self.assertEqual(self.mockinfo.usedfiles, result)

    #def test_new_get_content(self):
    #    filech = FileChooser()

    #    # image
    #    file_loc, dir_only, file_name = filech.new_get_content(
    #                                self.mockinfo.params_file_nonrecurs_dir)
    #    self.assertEqual(self.mockinfo.mockdirwfiles+"/file3.jpg", file_loc)
    #    self.assertEqual(self.mockinfo.mockdirwfiles, dir_only)
    #    self.assertEqual("file3.jpg", file_name)
    #
    #def test_get_content_direct(self):
    #    # Example: Poetry
    #    filech = FileChooser()
    #    content = filech.get_content(
    #                            self.mockinfo.cnt_prms_list[0],
    #                            "list")
    #    self.assertEqual(self.mockinfo.content_list_final, content)
    #
    #def test_get_content(self):
    #    # Example: Cats
    #    filech = FileChooser()
    #    # image
    #    content = filech.get_content(
    #                            self.mockinfo.cnt_prms_img_dir_nrec,
    #                            "image")
    #    self.assertEqual(self.mockinfo.content_image_final, content)
    #
    #def test_get_content_imgtxt_json_nonrec(self):
    #    # Example: Travel
    #    filech = FileChooser()
    #    # image + text(description)
    #    result_content_image_text = filech.get_content(
    #            self.mockinfo.cont_params_img_text_rec_fold,
    #            "image+text")
    #    self.assertEqual(
    #                self.mockinfo.content_image_text_final,
    #                result_content_image_text)
    #
    #def test_get_content_text_db(self):
    #    # Example: Quotes
    #    filech = FileChooser()
    #    result_content_text = filech.get_content(
    #                    self.mockinfo.cont_params_text,
    #                    "text")
    #    self.assertEqual(self.mockinfo.content_text_final, result_content_text)
    #
    #def test_get_content_imgtxt_db_nonrec(self):
    #    # Example: SciFi
    #    filech = FileChooser()
    #    # image + text(description) db
    #    result_content_imgtxt_nonrec = filech.get_content(
    #                    self.mockinfo.cont_imgtxt_db_nonrec,
    #                    "image+text")
    #    self.assertEqual(self.mockinfo.content_imgtxt_final_scifi,
    #                     result_content_imgtxt_nonrec)


if __name__ == "__main__":
    unittest.main()
