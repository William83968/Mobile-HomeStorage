import mysql.connector

class Database():
    def __init__(self):
        # Connect to MySQL server
        self.db = mysql.connector.connect(
            host = "localhost",
            user = "root",
            passwd = "6678liam",
            database = "home_db"
        )

    def setup(self):
        # Create a cursor
        self.cursor = self.db.cursor(buffered=True) 

        # Create an actual database
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS home_db")

        # Create the table
        self.cursor.execute(
            """CREATE TABLE IF NOT EXISTS `home_db`.`users` (
                `user_id` INT NOT NULL AUTO_INCREMENT,
                `username` VARCHAR(200) NOT NULL,
                `password` VARCHAR(200) NOT NULL,
                `email` VARCHAR(200) NULL DEFAULT '',
                `address` VARCHAR(200) NULL DEFAULT '',
                `city` VARCHAR(100) NULL DEFAULT '',
                PRIMARY KEY (`user_id`));
            """
        )
    
    def user_submit(self, values):
        datas = values
        sql_command = f"INSERT INTO `home_db`.`users` (username, pswd, email, address, city) VALUES (%s, %s, %s, %s, %s);"
        self.cursor.execute(sql_command, datas)
        self.db.commit()

    def check_user(self, username, password):
        us_name, pswd = username, password
        sql_command = f"SELECT * FROM `home_db`.`users` WHERE username='{us_name}' AND pswd='{pswd}'"
        self.cursor.execute(sql_command)
        records = self.cursor.fetchone()
        if records:
            return True
        else:
            return False


db = Database()
db.setup()







    