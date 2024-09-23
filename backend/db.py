import mysql.connector

class DBManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor(dictionary=True)

        self.create_tables()

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL,
            account_type ENUM('root', 'admin', 'user') NOT NULL,
            full_name VARCHAR(255) NOT NULL,
            apartment_code VARCHAR(50) NOT NULL,
            email VARCHAR(255),
            phone VARCHAR(20)
        );
        """)
        self.conn.commit()


        self.cursor.execute("SELECT * FROM users WHERE username = 'root'")
        if self.cursor.fetchone() is None:
            self.add_user('root', 'rootpassword', 'Root User', 'N/A', 'root')

    def add_user(self, username, password, full_name, apartment_code, account_type='user', email=None, phone=None):
        try:
            self.cursor.execute("""
            INSERT INTO users (username, password, account_type, full_name, apartment_code, email, phone)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (username, password, account_type, full_name, apartment_code, email, phone))
            self.conn.commit()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi thêm tài khoản: {err}")

    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        return self.cursor.fetchone()

    def get_all_users(self, account_type=None):
        if account_type:
            self.cursor.execute("SELECT * FROM users WHERE account_type = %s", (account_type,))
        else:
            self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
