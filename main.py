import argparse
from social_media.socialclientfactory import SocialClientFactory
import filesystem.json_actions as json_actions

from contentparser import ContentParser
from contentchooser import ContentChooser


def main(json_pref_loc, opt, credentials_loc, printonly=None):
    contentparser = ContentParser()
    contentchooser = ContentChooser()

    bpref = json_actions.read_json_file(json_pref_loc)
    credentials = json_actions.read_json_file(credentials_loc)
    # 1. parse options and fill in data structure
    item = contentparser.get_content_requirements(bpref[opt])
    # 2. get the items specified by options
    item = contentchooser.create_item(item)
    # 3. broadcast the item
    if printonly:
        print("Image: " + item.item_image_path + " Text: " + item.item_text)
    else:
        broadcast(item, credentials)


def broadcast(item, credentials):
    socfact = SocialClientFactory()
    soc_netw_client = socfact.get_social_network_client(item.social_network,
                                                        credentials)

    if item.item_text != "" and item.item_image_path != "":
        content_type = "image+text"
    else:
        content_type = item.content_item[0].content_type

    content = [item.item_image_path, item.item_text, item.tags]
    soc_netw_client.upload(
        content_type,
        item.blog_username,
        content)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Broadcast Images to social networks of your choice"
        )

    parser.add_argument(
        "option_location",
        type=str,
        help="Location of the preferences json file")
    parser.add_argument(
        "optionid",
        type=int,
        help="Option from setup blogs in json file")
    parser.add_argument(
        "credentials",
        type=str,
        help="Location of the credentials for social networks json file")
    parser.add_argument(
        "-p",
        "--printonly",
        action='store_true',
        help="will only print out specified parameters and nothing else")

    # args
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    main(args.option_location, args.optionid, args.credentials, args.printonly)
