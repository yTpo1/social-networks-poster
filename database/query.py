

def query(curs, sql_query, how_many=None, parameters=None):
    if parameters:
        sql_query = sql_query.format(parameters)

    curs.execute(sql_query)

    if how_many is "one":
        return curs.fetchone()
    else: # how_many is "all"
        return curs.fetchall()

def query_insert(connection, cursor, sql):
    rows_affected = cursor.execute(sql)
    connection.commit()
    return rows_affected


sql_templates = {
        "select": "SELECT {} FROM {};",
        "select_all": "SELECT * FROM {};",
        "select_count": "SELECT COUNT(*) FROM {};",
        "select_all_where_like": "SELECT * FROM {} WHERE {} LIKE {};",
        "select_all_where_eq": "SELECT * FROM {} WHERE {} LIKE {};",
        "select_where_eq": "SELECT {} FROM {} WHERE {} = '{}';",
        "s":"SELECT {} FROM {} WHERE {} IN (SELECT {} FROM {} WHERE {} = {});",
        "insert": "INSERT INTO {}({}) VALUES ('{}');"
}
