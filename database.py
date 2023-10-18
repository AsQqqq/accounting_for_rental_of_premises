import sqlite3
from listPRI import pri


class mainBase:
    def __init__(self) -> None:
        self.connection = sqlite3.connect("local.sqlite")
        self.cursor = self.connection.cursor()
        self.createTable()
        self.newDefaultUser()
        self.priDB()

    def createTable(self):
        """Создаем таблицу, если она не существует"""
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS account (login TEXT, password TEXT, status BOOL)''')
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS flat (location TEXT, busyness TEXT, price TEXT, category TEXT, paid_for TEXT)''')
        self.connection.commit()
    

    def priDB(self) -> None:
        self.cursor.execute('''SELECT * FROM flat''')
        if self.cursor.fetchall() == []:
            for i in pri:
                self.cursor.execute('''INSERT INTO flat(location, busyness, price, category, paid_for) VALUES (?, ?, ?, ?, ?)''',
                (
                    str(i[0]), str(i[1]), str(i[2]), str(i[3]), str(i[4])
                ))
                self.connection.commit()
    
    def selectFullPri(self) -> list:
        self.cursor.execute('''SELECT * FROM flat WHERE busyness == "True"''')
        return self.cursor.fetchall()
    

    def selectNonePri(self) -> list:
        self.cursor.execute('''SELECT * FROM flat WHERE busyness == "False"''')
        return self.cursor.fetchall()


    def newDefaultUser(self):
        self.cursor.execute('''SELECT * FROM account WHERE login = "root"''')
        if self.cursor.fetchall() == []:
            self.cursor.execute('''INSERT INTO account(login, password, status) VALUES ("root", "root", 0)''')
            self.connection.commit()
    
    def checkSignUp(self, login: str, password: str) -> bool:
        """Проверяем есть ли такой аккаунт в базе"""
        self.cursor.execute('''SELECT login, password FROM account WHERE login = ? AND password = ?''',
                             (login, password,))
        if self.cursor.fetchmany(1) != []:
            self.cursor.execute('''UPDATE account SET status = ? WHERE login = ?''', (1, login,))
            self.connection.commit()
            return True
        return False

    def join(self) -> bool:
        """Делаем статус входа 1"""
        self.cursor.execute('''SELECT login FROM account WHERE status = 1''')
        if self.cursor.fetchmany(1) != []:
            return True
        return False

    def exit(self) -> None:
        """Делаем статус входа 0"""
        self.cursor.execute('''SELECT login FROM account WHERE status = 1''')
        login = self.cursor.fetchone()
        self.cursor.execute('''UPDATE account SET status = ? WHERE login = ?''', (0, login[0],))
        self.connection.commit()
    

    def changeLine(self, location, val) -> None:
        print(val)
        if val:
            self.cursor.execute('''SELECT busyness FROM flat WHERE location = ?''', (location,))
            vv = self.cursor.fetchone()[0]
            if vv == "False":
                self.cursor.execute('''UPDATE flat SET busyness = ?, paid_for = ? WHERE location = ?''', ("True", str(val), location,))
                self.connection.commit()
        else:
            self.cursor.execute('''SELECT busyness FROM flat WHERE location = ?''', (location,))
            vv = self.cursor.fetchone()[0]
            if vv == "True":
                self.cursor.execute('''UPDATE flat SET busyness = ?, paid_for = ? WHERE location = ?''', ("False", "0", location,))
                self.connection.commit()
            
            
    