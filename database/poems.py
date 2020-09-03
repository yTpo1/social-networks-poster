import random
from database.library_models import PoemModel, AuthorModel
from database.query import query, query_insert

class Poems:
    def __init__(self, db_instance):
        self.db = db_instance
        self.poem_model = PoemModel()
        self.author_model = AuthorModel()

    def get_poem_count(self):
        sql = "SELECT COUNT(*) FROM {};".format(self.poem_model.table_name)
        count = query(self.db.cursor, sql, "one")
        return int(count[0])

    def get_poem_ids(self):
        sql = "SELECT {} FROM {};".format(self.poem_model.col_poem_id,
                                          self.poem_model.table_name)
        poem_ids = query(self.db.cursor, sql)
        return poem_ids

    def get_all_poems(self):
        sql = "SELECT * FROM {};".format(self.poem_model.table_name)
        poem_ids = query(self.db.cursor, sql)
        return poem_ids

    def get_author_by_id(self, auth_id):
        sql = "SELECT * FROM {} WHERE {} = {};".format(
                                               self.author_model.table_name,
                                               self.author_model.col_author_id,
                                               auth_id)
        author_rec = query(self.db.cursor, sql, "one")
        return author_rec

    def get_random_poem(self):
        poems = self.get_all_poems()
        rand_num = random.randint(0, len(poems)-1)
        return poems[rand_num]

    def insert_poem(self, title, author_id, poem_text, book_id):
        sql = "INSERT INTO `{}` (`{}`, `{}`, `{}`, `{}`, `{}`) VALUES "\
                "({}, \"{}\", {}, \"{}\", {});".format(
                            self.poem_model.table_name,
                            self.poem_model.col_poem_id,
                            self.poem_model.col_title,
                            self.poem_model.col_author_id,
                            self.poem_model.col_poem_text,
                            self.poem_model.col_book_id,
                            "null", title, str(author_id),
                            poem_text, str(book_id))
        query_insert(self.db.connection, self.db.cursor, sql)



