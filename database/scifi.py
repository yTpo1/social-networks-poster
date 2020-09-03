from database.scifi_models import ImagesModel, GenreModel, ArtistModel
from database.query import query


class ScifiImages:

    def __init__(self, db_instance):
        self.db = db_instance
        self.image_model = ImagesModel()
        self.genre_model = GenreModel()
        self.artist_model = ArtistModel()

    def sql_image_id(self, image_filename):
        return "SELECT {} FROM {} WHERE {} = '{}';".format(
                self.image_model.col_img_id,
                self.image_model.table_name,
                self.image_model.col_img_filename,
                image_filename)

    def sql_get_artists_id(self, image_id):
        return "select artistid from photos_to_artists where photoid = {};".format(image_id)

    def sql_get_artist_info(self, artist_id):
        return "select * from artists where artistid = '{}';".format(artist_id)

    def get_image_id(self, image_filename):
        result = query(self.db.cursor, self.sql_image_id(image_filename), "one")
        return result[0]

    def get_artist_id(self, image_id):
        result = query(self.db.cursor, self.sql_get_artists_id(image_id), "one")
        return result[0]

    def get_artist_info(self, artist_id):
        result = query(self.db.cursor, self.sql_get_artist_info(artist_id), "one")
        return result

    def get_artist_of_image(self, image_filename):
        image_id = self.get_image_id(image_filename)
        artist_id = self.get_artist_id(image_id)
        if artist_id == None:
            return None
        artist_info = self.get_artist_info(artist_id)
        return artist_info

