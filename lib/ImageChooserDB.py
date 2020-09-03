from lib.DBConnection import DBConnection as DB_Con #create_connection, close_connection
from lib.DBSelectQueries import DBSelectQueries as DBS
import random


class ImageChooserDB:
    """Choose image from the database"""

    def choose_new_random_photo_id(self, social_media):
        connection = DB_Con.create_connection()
        photo_ids_list = DBS.sql_all_photo_ids(connection)
        DB_Con.close_connection(connection)

        check_bool = False
        while check_bool is False:
            photo_id_random = random.choice(photo_ids_list)['PhotoID']
            if social_media == "Tumblr":
                check_bool = self.check_if_img_was_posted(photo_id_random)
            elif social_media == "Telegram":
                check_bool = self.check_if_img_was_posted_tele(photo_id_random)
        return str(photo_id_random)

    def add_image_to_used(self, photo_id, social_media):
        connection = DB_Con.create_connection()
        DBS.sql_insert_used_photo(connection, photo_id, social_media)
        DB_Con.close_connection(connection)

    # def add_image_to_used_tele(self, photo_id, social_media):
    #     connection = DB_Con.create_connection()
    #     DBS.sql_insert_used_photo(connection, photo_id, social_media)
    #     DB_Con.close_connection(connection)

    def check_if_img_was_posted_tele(self, photo_id):
        connection = DB_Con.create_connection()
        used_photos_list = DBS.sql_all_used_photo_ids(connection)
        DB_Con.close_connection(connection)

        for item in used_photos_list:
            if photo_id == item['PhotoID']:
                return False
        return True

    def check_if_img_was_posted(self, photo_id):
        connection = DB_Con.create_connection()
        used_photos_list = DBS.sql_all_used_photo_ids(connection)
        DB_Con.close_connection(connection)

        for item in used_photos_list:
            if photo_id == item['PhotoID']:
                return False
        return True

    def data_for_posting(self, photo_id):
        """For PhotoID get filename, genres, artist, check if gif, if anime get anime name"""
        """ caption - text under the post | hashtags = genres """
        connection = DB_Con.create_connection()
        file_name = DBS.sql_get_photo_name(connection, photo_id)['filename']
        file_extension = DBS.sql_get_photo_file_extension(connection, photo_id)['file extension']
        genre_ids = DBS.sql_get_genreIDs_from_photoID(connection, photo_id)

        genre_names = []
        for item in genre_ids:
            genre_name_tmp = DBS.sql_get_genre_name(connection, str(item['GenreID']))['Name']
            genre_names.append(genre_name_tmp)

        if {'GenreID': 1} in genre_ids:
            anime_id = str(DBS.sql_get_anime_name(connection, photo_id)['AnimeID'])
            anime_info = DBS.sql_get_anime_info(connection, anime_id)

            anime_name = anime_info['Name']
            myanimelistURL = anime_info['MyAnimeList']

            myanimelist = '<a href="' + myanimelistURL + '"> MyAnimeList </a>'
            caption = "Anime: " + anime_name + " | " + myanimelist
        else:
            artist_id = str(DBS.sql_get_artistID_from_photoID(connection, photo_id)['ArtistID'])
            artist_info = DBS.sql_get_artist_info(connection, artist_id)

            name_surname = artist_info['NameSurname']
            caption = "Artist: " + name_surname

            if artist_info['websiteURL']:
                websiteURL = artist_info['websiteURL']

                website = '<a href="' + websiteURL + '"> Website </a>'
                caption = caption + " | " + website
            elif artist_info['deviantartURL']:
                deviantartURL = artist_info['deviantartURL']

                deviantart = '<a href="' + deviantartURL + '"> Deviantart </a>'
                caption = caption + " | " + deviantart
            elif artist_info['artstationURL']:
                artstationURL = artist_info['artstationURL']

                artstation = '<a href="' + artstationURL + '"> Artstation </a>'
                caption = caption + " | " + artstation
            elif artist_info['InstagramURL']:
                instagramURL = artist_info['InstagramURL']

                instagram = '<a href="' + instagramURL + '"> Instagram </a>'
                caption = caption + " | " + instagram
            elif artist_info['FlickrURL']:
                flickrURL = artist_info['FlickrURL']

                flickr = '<a href="' + flickrURL + '"> Flickr </a>'
                caption = caption + " | " + flickr

        DB_Con.close_connection(connection)

        # hashtags = # genre names , if gif , if anime = anime name
        # hashtags = genre_names
        if file_extension == ".gif":
            genre_names.append("gif")
        if {'GenreID': 1} in genre_ids:
            genre_names.append(anime_name)

        return file_name, genre_names, caption

"""
To get:
1) filename - to indicate location to the file
2) genres - hashtags
3) artist - info below photo

4) anime - if genre anime, then look for anime

5) jpg/gif - hashtag for gifs

To do: 
change methods for quing json photos into simpler ones

Add used image to used_photos
"""