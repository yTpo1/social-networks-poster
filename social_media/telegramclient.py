from social_media.socialclient import SocialClient
from telethon import TelegramClient as TC
#from static_data.credentials import TELE_api_id, TELE_api_hash, TELE_session
from lib.ImageChooserDB import ImageChooserDB
from lib.dataparser import Parser
import getpass
# Moved, becuase this is sepparate logic


class TelegramClient(SocialClient):
    def __init__(self, credentials):
        parser = Parser()
        #tele_sess = parser.substr(TELE_session, getpass.getuser())
        #self.client = TC(tele_sess, TELE_api_id, TELE_api_hash)
        tele_sess = parser.substr(credentials["TELE_session"], getpass.getuser())
        self.client = TC(tele_sess,
                         credentials["TELE_api_id"],
                         credentials["TELE_api_hash"])
        self.client.start()

    def upload(self, content_type, blog_uname, content):
        if content_type == "text":
            self.upload_text(blog_uname, content[1])
        elif content_type == "image+text" or content_type == "image":
            self.upload_file(blog_uname, content[0], content[1])

    def upload_v1(self, content_type, blog_uname, content):
        if content_type == "text":
            if isinstance(content[0], dict):
                self.upload_text(blog_uname, content[0]["item"])
            else:
                self.upload_text(blog_uname, content)
        elif content_type == "image+text" or content_type == "image":
            texta = None
            for item in content:
                if item["content_type"] == "image":
                    filea = item["item"]
                if item["content_type"] == "text":
                    texta = item["item"]
            self.upload_file(blog_uname, filea, texta)
            # if filea is None:
            #     self.upload_text(blog_uname, texta)
            # else:
        # elif content_type == "image":
        #     self.upload_file(blog_uname, content)
        # elif content_type == "image+text":
        #     for item in content:
        #         if item["content_type"] == "image":
        #             filea = item["item"]
        #         if item["content_type"] == "text":
        #             texta = item["item"]
        #     self.upload_file(blog_uname, filea, texta)

    def upload_text(self, recipient, message):
        """Sends message to contant/chanel
        Example: recipient = '@test_chec' """

        self.client.send_message(recipient, message)
        print("Telegram Text Broadcast to: " + recipient +
              " completed successfully")

    def upload_file(self, recipient, pic_location, caption=None):
        if caption:
            self.client.send_file(recipient, pic_location,
                                  caption, parse_mode="html")
        else:
            self.client.send_file(recipient, pic_location)
        print("Telegram File Broadcast to: " + recipient +
              " completed successfully")

#    def upload_file_from_json(self, recepient_username, directory):
#        image_chooser = ImageChooserJSON(directory, "usedPhotosTelegram.json")
#
#        x = image_chooser.select_random_image(True)
#        directory = x[0]
#        pic_location = x[1]
#
#        general_info = InformationJson.get_photographers_info(directory)
#        caption = self.get_caption_travel(general_info)
#
#        self.upload_file_caption(recepient_username, pic_location, caption)
        # self.client.send_file(recepient_username, pic_location, caption+" |",
#                                parse_mode="html")

    def upload_file_from_db(self, recepient_username, directory):
        ImgC = ImageChooserDB()

        image_id = ImgC.choose_new_random_photo_id('Telegram')
        x = ImgC.data_for_posting(image_id)

        tags = []
        for item in x[1]:
            tags.append(item)

        caption = x[2]

        pic_location = directory + "\\" + x[0]

        # print(recepient_username + " " + pic_location + " " + caption)

        self.client.send_file(recepient_username, pic_location,
                              caption+" |", parse_mode="html")

        # Add image_id to used images
        ImgC.add_image_to_used(image_id, "Telegram")

    # def get_caption_travel(self, general_info):
    #     photographer_namesurname = general_info[0]

    #     caption = "Photo by: " + photographer_namesurname

    #     if general_info[3]:
    #         instagram = general_info[3]
    #         instagram = '<a href="' + instagram + '"> Instagram </a>'
    #         caption = caption + " | " + instagram

    #     return caption

# ImageChooser = ImageChooserJSON(r"C:\Users\Toshiba\Pictures\0 saved images")

# pic_location = ImageChooser.select_random_image()

# upload_file('@test_chec', pic_location)
