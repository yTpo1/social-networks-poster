class DBSelectQueries:

    # This should be moved to a different class, but whatever right? ;)
    @staticmethod
    def sql_insert_used_photo(connection, photo_id, social_media):
        if social_media == "Tumblr":
            table_name = "used_photos"
        if social_media == "Telegram":
            table_name = "used_photos_tele"

        with connection.cursor() as cursor:
            sql = "INSERT INTO `"+table_name+"`(`PhotoID`, `what_ever`) VALUES ('" + str(photo_id) + "', null)"
            cursor.execute(sql)
        connection.commit()

    # @staticmethod
    # def sql_insert_used_photo_tele(connection, photo_id):
    #     table_name = "used_photos_tele"
    #     with connection.cursor() as cursor:
    #         sql = "INSERT INTO `"+table_name+"`(`PhotoID`, `what_ever`) VALUES ('" + str(photo_id) + "', null)"
    #         cursor.execute(sql)
    #     connection.commit()

    @staticmethod
    def sql_all_photo_ids(connection):
        """Get all image IDs"""
        with connection.cursor() as cursor:
            sql = "SELECT `PhotoID` FROM `photos`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    @staticmethod
    def sql_all_used_photo_ids_tele(connection):
        """Get all used image IDs in teleram blog"""
        with connection.cursor() as cursor:
            sql = "SELECT `PhotoID` FROM `used_photos_tele`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    @staticmethod
    def sql_all_used_photo_ids(connection):
        """Get all used image IDs"""
        with connection.cursor() as cursor:
            sql = "SELECT `PhotoID` FROM `used_photos`"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    @staticmethod
    def sql_get_photo_name(connection, photo_id):
        """get the ID of the photo, from photo name"""
        with connection.cursor() as cursor:
            sql = "SELECT `filename` FROM `photos` WHERE `PhotoID` = '" + photo_id + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_photo_file_extension(connection, photo_id):
        with connection.cursor() as cursor:
            sql = "SELECT `file extension` FROM `photos` WHERE `PhotoID` = '" + photo_id + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_artistID_from_photoID(connection, photo_id):
        with connection.cursor() as cursor:
            sql = "SELECT `ArtistID` FROM `photos_to_artists` WHERE `PhotoID` = '" + photo_id + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_artist_info(connection, artist_id):
        with connection.cursor() as cursor:
            sql = "SELECT * FROM `artists` WHERE `ArtistID` = '" + artist_id + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_genreIDs_from_photoID(connection, photo_id):
        with connection.cursor() as cursor:
            sql = "SELECT `GenreID` FROM `photos_to_genres` WHERE `PhotoID` = '" + photo_id + "'"
            cursor.execute(sql)
            result = cursor.fetchall()
            return result

    @staticmethod
    def sql_get_genre_name(connection, genre_id):
        with connection.cursor() as cursor:
            sql = "SELECT `Name` FROM `genres` WHERE `GenreID` = '" + genre_id + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_anime_name(connection, photo_id):
        with connection.cursor() as cursor:
            sql = "SELECT `AnimeID` FROM `photos_to_anime` WHERE `PhotoID` = '" + photo_id + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

    @staticmethod
    def sql_get_anime_info(connection, anime_id):
        with connection.cursor() as cursor:
            sql = "SELECT `Name`, `MyAnimeList` FROM `anime` WHERE `AnimeID` = '" + anime_id + "'"
            cursor.execute(sql)
            result = cursor.fetchone()
            return result

