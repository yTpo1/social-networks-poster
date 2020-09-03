from social_media.socialclient import SocialClient
#from static_data.credentials import CONSUMER_KEY, CONSUMER_SECRET
#from static_data.credentials import OAUTH_TOKEN, OAUTH_TOKEN_SECRET
import pytumblr


class TumblrClient(SocialClient):

    def __init__(self, credentials):
        # Authenticate via OAuth
        #self.client = pytumblr.TumblrRestClient(CONSUMER_KEY, CONSUMER_SECRET,
        #                                        OAUTH_TOKEN,
        #                                        OAUTH_TOKEN_SECRET)
        self.client = pytumblr.TumblrRestClient(credentials["CONSUMER_KEY"],
                                                credentials["CONSUMER_SECRET"],
                                                credentials["OAUTH_TOKEN"],
                                                credentials["OAUTH_TOKEN_SECRET"])

    def upload(self, content_type, blog_username, content):
        # state = "queue"
        state = "published"
        # self.upload_file(blog_username, filea, texta, tags, state)
        self.upload_file(blog_username,
                         content[0],
                         content[1],
                         content[2],
                         state)

    def upload_v1(self, content_type, blog_username, content):
        # state = "queue"
        state = "published"

        texta = None
        for item in content:
            if 'content_type' in item:
                if item["content_type"] == "image":
                    filea = item["item"]
                if item["content_type"] == "text":
                    texta = item["item"]
            if "tags" in item:
                tags = item["tags"]
        self.upload_file(blog_username, filea, texta, tags, state)

        # if content_type == "image":
        #     self.upload_file(blog_username, content[0], caption="",
        #                       tags=content[1],
        #             state="published")
        # elif content_type == "image+text":
        #     for item in content:
        #         if 'content_type' in item:
        #             if item["content_type"] == "image":
        #                 filea = item["item"]
        #             if item["content_type"] == "text":
        #                 texta = item["item"]
        #         if "tags" in item:
        #             tags = item["tags"]
        #     self.upload_file(blog_username, filea, texta, tags,
        #             state="published")
        # else:
        #     print("Function for this filetype is not implemented")

    def upload_file(self, blog_username, file_location, caption, tags, state):
        self.client.create_photo(blog_username,
                                 state=state,
                                 data=file_location,
                                 tags=tags,
                                 caption=caption)
        print("Tumblr File Broadcast to: " + blog_username +
              " completed successfully")
