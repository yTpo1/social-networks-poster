# Social Networks (Blogs) Media Broadcaster

Was a final year project at uni. I guess you could say that this is a data driven application.

# Usage
```
$ py main.py [-h] [-p] blog_settings_file option_id credentials_file
```

## With Docker
```
$ docker-compose up
```

Note. Currently Docker is set up to run cron to regularly call the script/app, broadcasting images to different blogs.

An example of a a cron job in the crontab file:
```
0 */9 * * * /usr/local/bin/python3.6 /usr/src/app/main.py /media/root/ssd_name/settings/blog_settings.json 0 /media/root/ssd_name/settings/credentials_keys.json > /dev/null 2>&1
```

# Screenshots
|||
|--|--|
|Examples of posts to Twitter|![Twitter example](readme_images/example_post_twitter.jpg)|
|Examples of posts to Tumblr|![Tumblr example](readme_images/example_post_tumblr.jpg)![Tumblr example](readme_images/example_post_tumblr_2.jpg)![Tumblr example](readme_images/example_post_tumblr_3.jpg)|
|Examples of posts to Telegram|![Telegram example](readme_images/example_post_telegram.jpg)|
|Examples of posts to VK||

# Blog options json file
|Parameter|Available Options|
|--|--|
|social_network|"telegram", "tumblr", "twitter", "vk"|
|blog_username|The username of your blog|
|content_type|"text","image","image+text"|
|tags|List of hash tags that will be attached to the post. Example: ["yolo","greatday"]|
|content|Is a list of items to post that have parameters of ther own|

### Content parameters
|Parameter|Available Options|
|--|--|
|content_type|"text", "image"|
|directory (only used with "image" content_type)|"/path/to/images"|
|recursive_folders (only used with "image" content_type)|true, false|
|selection_alg|"random", "description"|
|broadcast_history_ftype (used with "image" content_type)|"json"|
|broadcast_history (used with "image" content_type)|"/path/to/history_log_file.json"|
|data_format (only used with "text" content_type)|"json", "database"|
|data_file (only used with "text" content_type)|"nameoffile.json", "/path/to/sqlite.db"|
|format_rules (only used with "text" content_type)|Takes values from "data_file" and inserts them into the %s position|



### Blog settings/parameters json file example
```
[
    {
        "social_network": "telegram",
        "blog_username": "@literature_blog",
        "content_type": "text",
        "application": "note_to_self_literature_blog",
        "content":[
            {
                "content_type": "text",
                "selection_alg": "random",
                "data_format": "database",
                "data_file": "/path/to/sqlite/database/mydata.db",
                "format_rules": [
                    {"\"%s":0},
                    {"\"\n\n- %s":1}
                    ]
            }
        ],
        "tags":""
    },
        {
        "social_network": "tumblr",
        "blog_username": "world_wide_art_images",
        "content_type": "image+text",
        "application": "note_to_self_art_blog",
        "content" : [
            {
                "content_type": "image",
                "directory": "/path/to/dir/with/images/",
                "recursive_folders": true,
                "selection_alg": "random",
                "broadcast_history_ftype": "json",
                "broadcast_history": "/path/to/history_log_file.json"
            },
            {
                "content_type": "text",
                "selection_alg": "description",
                "data_format": "json",
                "data_file": "infogeneral.json",
                "format_rules": [
                    {"Photo by: %s ":0},
                    {" | <a href=\"%s\"\"> Instagram </a> |":3}
                    ]
            }
        ],
        "tags":["art", "explore", "inspiration"]
    }
]
```


### Credentials and keys json file example
```
[
{
	"social_network": "telegram",
	"keys": {
		"TELE_api_id": ,
		"TELE_api_hash": "",
		"TELE_session":  "",
		"TELE_session_test": ""
	}
},
{
	"social_network": "twitter",
	"keys": {
		"CONSUMER_KEY_TW": "",
		"CONSUMER_SECRET_TW": "",
		"ACCESS_KEY_TW": "",
		"ACCESS_SECRET_TW": ""
	}
},
{
	"social_network": "tumblr",
	"note": "",
	"keys": {
		"CONSUMER_KEY": "",
		"CONSUMER_SECRET": "",
		"OAUTH_TOKEN": "",
		"OAUTH_TOKEN_SECRET": ""
	}
},
{
	"social_network": "vk",
	"note": "",
	"keys": {
		"vk_user_id": "",
		"vk_album_id": "",
		"vk_version": "5.103",
		"vk_token_loc": "",
		"vk_token_loc_test": ""
	}
}
]
```
### Other
VK  
blog_username is group_id
