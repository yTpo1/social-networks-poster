from M_Sqlite import M_Sqlite
import random

class TextChooser:

    def get_quote(self, db_location):
        db = M_Sqlite()
        conn, curs = db.create_connetion(db_location)
        # find out total quotes in the database
        total_quotes = db.get_count_quotes(curs)
        # get a random number for range in quotes
        random_number = random.randint(0, int(total_quotes[0]))
        query = db.get_quote_by_id(curs, str(random_number))
        db.close_connetion(conn)
        # print(query[0])

        # print(type(query[0]))

        quote = query[0][1]
        author = query[0][2]
        return quote, author
