import mysql.connector
from mysql.connector import Error


def connect_to_mysql_db():
    # TODO: when in Git --> change the real passwords to wildcards (******)
    connection_config_dict = {
        'user': 'your_username',
        'password': 'your_password',
        'host': 'your_host',
        'database': 'songs',
    }
    try:
        con = mysql.connector.connect(**connection_config_dict)
        if con.is_connected():
            db_Info = con.get_server_info()
            print("\t\t> Connected to MySQL Server version ", db_Info)
        return con
    except Error as e:
        print("\t\t> ***** Error while connection to MySQL", e)
        return None


def db_query(con, query):
    cursor = con.cursor()
    cursor.execute(query)
    records = cursor.fetchall()

    # return all records
    return records, cursor


def close_connection(c, con):
    c.close()
    con.close()
    print("\t\t> MySQL connection is closed")


def write_to_db(song):
    connection = connect_to_mysql_db()
    cursor = connection.cursor()

    sql_insert_query = "insert into song_info (song_name, song_artist, song_yt_link, song_full_title) " \
                       "VALUES (%s, %s, %s, %s)"
    val = (song.title, song.artist, song.yt_link, song.full_title)

    # Insertion query (add 1 row)
    cursor.execute(sql_insert_query, val)
    connection.commit()
    print("\t\t> ", cursor.rowcount, "was inserted.")
    close_connection(cursor, connection)

