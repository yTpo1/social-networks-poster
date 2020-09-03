

class ImagesModel:
    table_name = "photos"
    col_img_id = "PhotoID"
    col_img_filename = "filename"
    col_file_extension = "file_extension"
    col_description = "description"


class ArtistModel:
    table_name = "artists"
    col_artist_id = "ArtistID"
    col_name = "NameSurname"
    col_website_url = "websiteURL"
    col_artstation_url = "artstationURL"
    col_deviantart_url = "deviantartURL"
    col_instagram_url = "InstagramURL"
    col_tumblr_url = "TumblrURL"


class GenreModel:
    table_name = "genres"
    col_genre_id = "GenreID"
    col_name = "Name"

