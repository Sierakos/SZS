import sqlite3

class Sqlite():
    def __init__(self):
        pass

    try: 
        def connect(self):
            self.conn = sqlite3.connect('C:\\Users\\Sebastian\\Desktop\\studia\\ZPO\\test\\SZS\\SZS_console\\Student_system_managment.db')
            self.c = self.conn.cursor()
            self.c.execute("PRAGMA foreign_keys = ON")
            return self.conn
    except:
        print("Nie udało połączyć się do bazy danych.")


    def commit(self, connection):
        connection.commit()

    def close(self, connection):
        connection.close()
