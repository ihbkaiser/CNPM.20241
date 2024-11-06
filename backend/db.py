import mysql.connector
import yaml
class DBManager:
    def __init__(self, host, user, password, database):
        # create if not exists database
        self.create_database(host, user, password, database)
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.create_tables()
    def create_database(self, host, user, password, database):
        conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password
        )
        cursor = conn.cursor()
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database}")
        conn.close()


    def clear_tables(self):
        self.cursor.execute("DELETE FROM users")

    def create_tables(self):
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            username VARCHAR(255) PRIMARY KEY,
            password VARCHAR(255) NOT NULL,
            account_type ENUM('root', 'admin', 'user') NOT NULL,
            full_name VARCHAR(255) NOT NULL,
            phone_number VARCHAR(20) NOT NULL,
            apartment_code VARCHAR(50) NOT NULL,
            email VARCHAR(255)
        );
        """)
        self.conn.commit()


        self.cursor.execute("SELECT * FROM users WHERE username = 'root'")
        if self.cursor.fetchone() is None:
            self.add_user('root', 'rootpassword', 'Root User', '09111111111', 'N/A', 'root')

    def add_user(self, username, password, full_name, phone_number, apartment_code, account_type='user', email=None):
        try:
            self.cursor.execute("""
            INSERT INTO users (username, password, account_type, full_name, phone_number, apartment_code, email)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
            """, (username, password, account_type, full_name, phone_number, apartment_code, email))
            self.conn.commit() 
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi thêm tài khoản: {err}")

    def get_user(self, username):
        self.cursor.execute("SELECT * FROM users WHERE username = %s", (username,))
        return self.cursor.fetchone()
    
    def delete_user(self, username):
        self.cursor.execute("DELETE FROM users WHERE username = %s", (username,))
        self.conn.commit()

    def update_user(self, username, account_type, full_name, phone_number,  apartment_code, email):
        self.cursor.execute("UPDATE users SET account_type = %s, full_name = %s, phone_number = %s, apartment_code = %s, email = %s WHERE username = %s",
                            (account_type, full_name, phone_number, apartment_code, email, username))
        self.conn.commit()

    def get_all_users(self, account_type=None):
        if account_type:
            self.cursor.execute("SELECT * FROM users WHERE account_type = %s", (account_type,))
        else:
            self.cursor.execute("SELECT * FROM users")
        return self.cursor.fetchall()
    def update_user_password(self, username, new_password):
        """Cập nhật mật khẩu của người dùng."""
        try:
            self.cursor.execute("UPDATE users SET password = %s WHERE username = %s", (new_password, username))
            self.conn.commit()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi cập nhật mật khẩu: {err}")
        
    def close(self):
        self.conn.close()
