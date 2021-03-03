import sqlite3 

class Database():
    def __init__(self, fileName):
        self.file_name = fileName
        self.create_tables()

    def create_tables(self):
        connection = sqlite3.connect(self.file_name)
        cursor = connection.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS urls (long_url TEXT, short_url_id TEXT)")
        connection.commit()
        connection.close()

    def insert_url(self, long_url, short_url_id):
        connection = sqlite3.connect(self.file_name)
        cursor = connection.cursor()
        cursor.execute("INSERT INTO urls VALUES (?, ?)", (long_url, short_url_id))
        connection.commit()
        connection.close()
