import sqlite3

class Database:
    def __init__(self, database_name: str) -> None:
        self.database = sqlite3.connect(database_name)
        self.database.row_factory = sqlite3.Row
        self.database.execute('CREATE TABLE IF NOT EXISTS goods (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, content TEXT NOT NULL, price TEXT NOT NULL, image TEXT NOT NULL )')
        self.database.execute('CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, cardId TEXT NOT NULL)')
    def __del__(self) -> None:
        self.database.close()

    def createTestPost(self) -> None:
        self.database.execute('INSERT INTO goods (name, content, price, image) VALUES ("Random Title", "Lorem ipsum dolor sit amet consectetur adipiscing elit", "2000", "toy1.jpg")')