from lib.dataparser import Parser
import filesystem.txt_actions as txt_actions

from database.database_connection import DatabaseInit
from database.quotes import Quotes
from database.poems import Poems
from database.scifi import ScifiImages
#from M_Sqlite import M_Sqlite
#from static_data.sql_queries_dict import sql_queries


class TextChooser:
    def get_text(self, selection_alg, data_file, data_format, directory=None,
                 file_name=None, application=None, db_engine="sqlite"):
        if selection_alg == "random":
            if data_format == "database":
                if application == "quotes":
                    # (quote, author) =
                    general_info = self.get_quote(db_engine, data_file)
                if application == "poetry":
                    general_info = self.get_poem_data(db_engine, data_file)
        elif selection_alg == "direct":
            if data_format == "txt":
                general_info = txt_actions.read_txt(data_file)
        elif selection_alg == "description":
            if data_format == "json":
                parser = Parser()
                general_info = parser.get_values_json(directory,
                                                      data_file)
            elif data_format == "database":
                general_info = self.get_scifi_description(db_engine, data_file, file_name)

        return general_info

    def get_scifi_description(self, db_engine, data_file, file_name):
        db = DatabaseInit(db_engine, data_file)
        scifi = ScifiImages(db.database)
        record = scifi.get_artist_of_image(file_name)
        db.close_connection()
        return record

    def parse_quote_and_author(self, quote_record):
        quote_text = quote_record[0][1]
        quote_author = quote_record[0][2]
        return quote_text, quote_author


    def get_quote(self, db_engine, db_location):
        db = DatabaseInit(db_engine, db_location)
        quotes = Quotes(db.database)
        quote_record = quotes.get_random_quote()
        quote_text, quote_author = self.parse_quote_and_author(quote_record)
        db.close_connection()
        return quote_text, quote_author


    def get_poem_data(self, db_engine, database_name):
        db = DatabaseInit(db_engine, database_name)

        poetry_actions = Poems(db.database)
        poem_record = poetry_actions.get_random_poem()
        author_record = poetry_actions.get_author_by_id(poem_record[2])

        db.close_connection()

        return (poem_record, author_record)

        #poem = format_poem(poem_record, author_record)

    #def old_get_scifi_description(self, data_file, file_name):
    #    conn, curs = M_Sqlite.create_connetion(data_file)

    #    image_id = M_Sqlite.query(curs,
    #                              sql_queries['scifi_get_image_id'],
    #                              'one', parameter=file_name)
    #    artist_id = M_Sqlite.query(
    #                        curs,
    #                        sql_queries['scifi_get_artist_id_from_image_id'],
    #                        'one',
    #                        parameter=image_id[0])

    #    if artist_id is None:
    #        M_Sqlite.close_connetion(conn)

    #    general_info = M_Sqlite.query(
    #                        curs,
    #                        sql_queries['scifi_get_artist_info'],
    #                        'one',
    #                        parameter=artist_id[0])
    #    M_Sqlite.close_connetion(conn)

    #    return general_info


    #def get_quote(self, db_location):
    #    db = M_Sqlite()
    #    conn, curs = db.create_connetion(db_location)

    #    # find out total quotes in the database
    #    total_quotes = db.query(curs, sql_queries['select_count'], 'one')

    #    # get a random number for range in quotes
    #    random_number = random.randint(1, int(total_quotes[0]))

    #    query = db.query(
    #                    curs,
    #                    sql_queries['get_quote_by_id'],
    #                    'one',
    #                    parameter=str(random_number))
    #    db.close_connetion(conn)

    #    # quote, author
    #    return query[1], query[2]
