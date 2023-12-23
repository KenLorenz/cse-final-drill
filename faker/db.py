import mysql.connector

class mysqli:

    def __init__(self):
        self.host = "127.0.0.1"
        self.port = 3306
        self.user = "ren"
        self.password = '122846'
        self.database="cseCars"
        self.sql = None
        
    def connect(self):
        try:
            self.sql = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
        except mysql.connector.Error as err:
            print(err)
        return self.sql
    