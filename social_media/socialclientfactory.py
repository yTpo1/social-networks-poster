from social_media.telegramclient import TelegramClient
from social_media.tumblrclient import TumblrClient
from social_media.twitterclient import TwitterClient
from social_media.vkclient import VkClient


class SocialClientFactory:
    def __init__(self):
        pass

    def get_social_network_client(self, soc_netw, credentials):
        for cred in credentials:
            if cred["social_network"] == soc_netw:
                keys = cred["keys"]
        if soc_netw == "telegram":
            return TelegramClient(keys)
        elif soc_netw == "tumblr":
            return TumblrClient(keys)
        elif soc_netw == "twitter":
            return TwitterClient(keys)
        elif soc_netw == "vk":
            return VkClient(keys)
        else:
            raise Exception("Unrecognisible client")
