from social_media.socialclient import SocialClient
import tweepy
#from static_data.credentials import CONSUMER_KEY_TW, CONSUMER_SECRET_TW
#from static_data.credentials import ACCESS_KEY_TW, ACCESS_SECRET_TW


class TwitterClient(SocialClient):

    def __init__(self, keys):
        #auth = tweepy.OAuthHandler(CONSUMER_KEY_TW, CONSUMER_SECRET_TW)
        #auth.set_access_token(ACCESS_KEY_TW, ACCESS_SECRET_TW)
        auth = tweepy.OAuthHandler(keys["CONSUMER_KEY_TW"],
                                   keys["CONSUMER_SECRET_TW"])
        auth.set_access_token(keys["ACCESS_KEY_TW"], keys["ACCESS_SECRET_TW"])
        self.api = tweepy.API(auth)

    def upload(self, content_type, blog_username, content):
        for tag in content[2]:
            content[1] = content[1] + "#"+tag+" "
        self.upload_image(content[0], content[1])

    def upload_v1(self, content_type, blog_username, content):
        if content_type == "image":
            self.upload_image(content[0], content[1])
        elif content_type == "image+text":
            texta = ""
            for item in content:
                if 'content_type' in item:
                    if item["content_type"] == "image":
                        filea = item["item"]
                    if item["content_type"] == "text":
                        texta = item["item"]
                if "tags" in item:
                    tags = item["tags"]

            for tag in tags:
                texta = texta + "#"+tag+" "
            self.upload_image(filea, texta)

    def upload_image(self, file_loc, caption):
        self.api.update_with_media(file_loc, status=caption)
        print("Twitter File Broadcast, completed successfully")
