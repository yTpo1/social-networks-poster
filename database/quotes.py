import random
from database.library_models import QuotesModel
from database.query import query, sql_templates


class Quotes:

    def __init__(self, db_instance):
        self.db = db_instance
        self.model = QuotesModel()

    def sql_select_ids(self):
        return sql_templates["select"].format(self.model.col_quote_id,
                self.model.table_name)

    def sql_count(self):
        return sql_templates["select_count"].format(self.model.table_name)

    def sql_quote_by_id(self, id):
        return sql_templates["select_all_where_eq"].format(self.model.table_name,
            self.model.col_quote_id, id)

    def get_count(self):
        count = query(self.db.cursor, self.sql_count(), "one")
        return int(count[0])

    def get_all_ids(self):
        ids = query(self.db.cursor, self.sql_select_ids())
        return ids

    def get_random_quote(self):
        quote_ids = self.get_all_ids()
        rand_num = random.randint(0, len(quote_ids)-1)
        quote = query(self.db.cursor,
                self.sql_quote_by_id(quote_ids[rand_num][0]))
        return quote

