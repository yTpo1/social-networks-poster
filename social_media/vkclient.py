import requests
from social_media.socialclient import SocialClient
#from static_data.credentials import vk_user_id, vk_album_id
#from static_data.credentials import vk_version, vk_token_loc
from lib.dataparser import Parser
import getpass
#from filemanager import FileManager
import filesystem.txt_actions as txt_actions


class VkClient(SocialClient):
    def __init__(self, keys):
        parser = Parser()
        #vk_token = parser.substr(vk_token_loc, getpass.getuser())
        vk_token = parser.substr(keys["vk_token_loc"], getpass.getuser())
        self.token = txt_actions.read_txt(vk_token)
        #self.user_id = vk_user_id
        #self.album_id = vk_album_id
        #self.version = vk_version
        self.user_id = keys["vk_user_id"]
        self.album_id = keys["vk_album_id"]
        self.version = keys["vk_version"]

    def upload(self, content_type, blog_username, content):
        if content_type == "text":
            self.upload_text(
                    self.token,
                    group_id=blog_username,
                    version=self.version,
                    message=content[1])
        elif content_type == "image+text" or content_type == "image":
            for tag in content[2]:
                content[1] = content[1] + "#"+tag+" "
            self.upload_photo(
                    self.token,
                    group_id=blog_username,
                    version=self.version,
                    message=content[1],
                    fileloc=content[0],
                    user_id=self.user_id,
                    album_id=self.album_id)

    def upload_v1(self, content_type, blog_username, content):
        if content_type == "text":
            self.upload_text(
                    self.token,
                    group_id=blog_username,
                    version=self.version,
                    message=content)
        elif content_type == "image+text" or content_type == "image":
            texta = None
            for item in content:
                if item["content_type"] == "image":
                    filea = item["item"]
                if item["content_type"] == "text":
                    texta = item["item"]
            # self.upload_file(blog_uname, filea, texta)
            self.upload_photo(
                    self.token,
                    group_id=blog_username,
                    version=self.version,
                    message=texta,
                    fileloc=filea,
                    user_id=self.user_id,
                    album_id=self.album_id)

    def upload_text(self, token, group_id, version, message):
        r = self.post_group_v2(token, group_id=group_id, v=version,
                               message=message)
        return r

    def upload_photo(self, token, group_id, version, message,
                     fileloc, user_id, album_id):
        ph_alb_r = self.upload_photo_to_album(token,
                                              album_id,
                                              fileloc,
                                              version)
        # attachments: <type><owner_id>_<media_id>,<type><owner_id>_<media_id>
        # attachments = 'photo'+'-'+group_id+'_'+ str(ph_alb_r['response'][0]['id'])
        attachments = 'photo'+user_id+'_'+ str(ph_alb_r['response'][0]['id'])

        r = self.post_group_v2(token, group_id=group_id, v=version, message=message, attachments=attachments)
        print("Upload Photo to VK successfull")
        return r

    def upload_photo_to_album(self, token,  album_id, fileloc, version,
                              group_id=None):
        if group_id:
            upload_url = self.get_upload_server_group(token, group_id,
                                                      album_id, version)
        else:
            upload_url = self.get_upload_server_user(token, album_id, version)
        bfile = {'file1': open(fileloc, 'rb')}
        req_post = self.post_query_upload_photo(upload_url, bfile)
        if group_id:
            r = self.save_photo_on_server_group(token, req_post, version)
        else:
            r = self.save_photo_on_server_user(token, req_post, version)
        return r

    def post_group_v2(self, token, group_id, v, message=None, attachments=None):
        parameters = {'owner_id':'-'+group_id,
                            'from_group':'1',
                            'v':v,
                            'access_token':token}
        if message:
            parameters.update({'message':message})
        if attachments:
            parameters.update({'attachments':attachments})
        if message == None and attachments == None:
            parameters.update({'message':'.'})

        r = requests.post('https://api.vk.com/method/wall.post',
                    params=parameters).json()
        return r

    def get_upload_server_group(self, token, group_id, album_id, v):
        r = requests.get('https://api.vk.com/method/photos.getUploadServer',
                    params={
                        'access_token': token,
                        'album_id': album_id,
                        'group_id': group_id,
                        'v':v
                        }).json()
        return r['response']['upload_url']

    def get_upload_server_user(self, token, album_id, v):
        r = requests.get('https://api.vk.com/method/photos.getUploadServer',
                    params={
                        'access_token': token,
                        'album_id': album_id,
                        'v':v
                        }).json()
        return r['response']['upload_url']

    def post_query_upload_photo(self, upload_url, bfile):
        ur = requests.post(upload_url, files=bfile).json()
        return ur

    def save_photo_on_server_group(self, token, upload_url, v):
        r = requests.get('https://api.vk.com/method/photos.save',
                    params={
                        'access_token': token,
                        'album_id': upload_url['aid'],
                        'group_id': upload_url['gid'],
                        'server': upload_url['server'],
                        'photos_list': upload_url['photos_list'],
                        'hash': upload_url['hash'],
                        'v':v
                        }).json()
        return r

    def save_photo_on_server_user(self, token, upload_url, v):
        r = requests.get('https://api.vk.com/method/photos.save',
                    params={
                        'access_token': token,
                        'album_id': upload_url['aid'],
                        'server': upload_url['server'],
                        'photos_list': upload_url['photos_list'],
                        'hash': upload_url['hash'],
                        'v':v
                        }).json()
        return r


#    def get_user_info(token, user_id, v):
#        r = requests.get('https://api.vk.com/method/users.get',
#                        params={'user_id':user_id,
#                            'v':v,
#                            'access_token':token}).json()
#        return r
#
#    def get_group_members(token, group_id, v):
#        r = requests.get('https://api.vk.com/method/groups.getMembers',
#                        params={'group_id':group_id,
#                            'count':'5',
#                            'v':v,
#                            'access_token':token}).json()
#        return r

#def post_group(token, group_id, message, v):
#    r = requests.get('https://api.vk.com/method/wall.post',
#                params={'owner_id':'-'+group_id,
#                        'from_group':'1',
#                        'message':message,
#                        'v':v,
#                        'access_token':token}).json()
#    return r


#def post_user(token, user_id, message, v):
#    r = requests.get('https://api.vk.com/method/wall.post',
#                params={'owner_id':user_id,
#                        'message':message,
#                        'v':v,
#                        'access_token':token}).json()
#    return r
#
#def wall_user(token, user_id, v):
#    r = requests.get('https://api.vk.com/method/wall.get',
#                params={'owner_id':user_id,
#                        'count':'3',
#                        'v':v,
#                        'access_token':token}).json()
#    return r
#
#def get_vk_session(email, password):
#    self.session = requests.Session()
#
#def create_token(client_id, permissions, v):
#    r = requests.get('https://oauth.vk.com/authorize',
#                params={
#                    'client_id':client_id,
#                    'redirect_uri':'https://oauth.vk.com/blank.html',
#                    'scope':permissions,
#                    'response_type':'token',
#                    'v':v
#                    }).json()
#    return r
