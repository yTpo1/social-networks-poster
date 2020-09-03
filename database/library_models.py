

class PoemModel:
    table_name = "Poem"
    col_poem_id = "poem_id"
    col_title = "title"
    col_author_id = "author_id"
    col_poem_text = "poemtext"
    col_book_id = "Book_id"

class BookModel:
    table_name = "book"
    col_book_id = "Book_id"
    col_title = "Title"
    col_author_id = "Author_id"
    col_year = "Year"


class AuthorModel:
    table_name = "Author"
    col_author_id = "author_id"
    col_first_name = "firstname"
    col_last_name = "lastname"


class QuotesModel:
    table_name = "Quotes"
    col_quote_id = "id"
    col_quote_text = "quote_text"
    col_author = "author"
    col_genre = "genre"

