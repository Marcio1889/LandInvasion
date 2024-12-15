

import sqlite3


class DB:

    def __init__(self, name_db: str):
        self.name_db = name_db
        self.connection = sqlite3.connect(name_db)
        self.connection.execute(''' 
                                 CREATE TABLE IF NOT EXISTS dados(
                                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                                 name TEXT NOT NULL,
                                 score INTEGER NOT NULL,
                                 date TEXT NOT NULL)
                              '''
                                )
    def delete_all(self):
        print("Deleting all records...")
        self.connection.execute('DELETE FROM dados')
        self.connection.commit()

    def cleanup(self):
        print("Cleaning up the table to keep only the top 10 scores...")
        self.connection.execute('''
            DELETE FROM dados WHERE id NOT IN (
                SELECT id FROM dados ORDER BY score DESC LIMIT 10
            )
        ''')
        self.connection.commit()

    def save(self, score_dict: dict):
        print(f"Saving score: {score_dict}")
        self.connection.execute('INSERT INTO dados (name, score, date) VALUES (:name, :score, :date)', score_dict)
        self.connection.commit()
        self.cleanup()

    def retrieve_top(self) -> list:
        return self.connection.execute('SELECT * FROM dados ORDER BY score DESC LIMIT 10').fetchall()

    def close(self):
        self.connection.close()
