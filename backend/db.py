import mysql.connector

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
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS userfee (
            apartment_code VARCHAR(50) NOT NULL,
            fee_name VARCHAR(50) NOT NULL,
            total int,
            paid int,
            remain int,
            residual int
        );    
        """)
        self.conn.commit()
        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS fees (
            fee_name VARCHAR(50) NOT NULL,
            deadline datetime,
            total int,
            paid int,
            remain int
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
    
    def get_all_userfee(self):
        self.cursor.execute("SELECT * FROM userfee")
        return self.cursor.fetchall()

    
    def add_userfee(self, apartment_code, fee_name, total, paid, remain, residual):
        try:
            self.cursor.execute("""
            INSERT INTO userfee ( apartment_code, fee_name, total, paid, remain, residual)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (apartment_code, fee_name, total, paid, remain, residual))
            self.conn.commit() 
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi thêm căn hộ: {err}")
        
    def delete_userfee(self, apartment_code, fee_name):
        self.cursor.execute("DELETE FROM userfee WHERE apartment_code = %s AND fee_name = %s", (apartment_code, fee_name))
        self.conn.commit()
    
    def update_userfee(self, apartment_code, fee_name, total, paid, remain, residual):
        self.cursor.execute("UPDATE userfee SET total = %s, paid = %s, remain = %s, residual = %s WHERE apartment_code = %s AND fee_name = %s",
                            (total, paid, remain, residual, apartment_code, fee_name))
        self.conn.commit()
    
    def get_all_fees(self):
        self.cursor.execute("SELECT * FROM fees")
        return self.cursor.fetchall()
    def get_fee_names(self):
        self.cursor.execute("SELECT fee_name FROM fees")
        return [row['fee_name'] for row in self.cursor.fetchall()]

    def add_fee(self, fee_name, deadline, total, paid, remain):
        try:
            self.cursor.execute("""
            INSERT INTO fees (fee_name, deadline, total, paid, remain)
            VALUES (%s, %s, %s, %s, %s)
            """, (fee_name, deadline, total, paid, remain))
            self.conn.commit() 
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi thêm phí: {err}")
    
    def delete_fee(self, apartment_code, fee_name):
        self.cursor.execute("DELETE FROM fees WHERE apartment_code=%s and fee_name = %s ", (apartment_code,fee_name,))
        self.conn.commit()
    
    def update_fee(self, fee_name, deadline, total, paid, remain):
        self.cursor.execute("UPDATE fees SET deadline = %s, total = %s, paid = %s, remain = %s WHERE fee_name = %s",
                            (deadline, total, paid, remain, fee_name))
        self.conn.commit()
    def user_fee_info(self, apt_code, fee_name):
        self.cursor.execute("SELECT * FROM userfee WHERE apartment_code = %s AND fee_name = %s", (apt_code, fee_name))
        row = self.cursor.fetchone()
        if row is None:
            return None

        apt_code = row['apartment_code']
        feename = row['fee_name']
        money_paid = row['paid']
        money_remain = row['remain']
        money_residual = row['residual']
        self.cursor.execute("SELECT full_name, username FROM users WHERE apartment_code = %s", (apt_code,))
        info = self.cursor.fetchone()
        fullname = info['full_name']
        username = info['username']
        status = 'Complete' if money_remain == 0 else 'Incomplete'
        return {
            'username': username,
            'fullname': fullname,
            'apt_code': apt_code,
            'feename': feename,
            'money_paid': money_paid,
            'money_remain': money_remain,
            'money_residual': money_residual,
            'status' : status
        }
    def thu_fee(self, apartment_code, fee_name, pay_money):
        self.cursor.execute("SELECT * FROM userfee WHERE apartment_code = %s AND fee_name = %s", (apartment_code, fee_name))
        row = self.cursor.fetchone()
        if row is None:
            return None
        total = row['total']
        paid = row['paid']
        remain = row['remain']
        residual = row['residual']
        paid += pay_money
        remain = total - paid
        if remain < 0:
            residual = -remain
            remain = 0
        self.cursor.execute("UPDATE userfee SET paid = %s, remain = %s, residual = %s WHERE apartment_code = %s AND fee_name = %s",
                            (paid, remain, residual, apartment_code, fee_name))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def get_parking_fee_summary(self):
        """Lấy thống kê tổng hợp tiền gửi xe."""
        try:
            self.cursor.execute("""
            SELECT DATE_FORMAT(deadline, '%Y-%m') AS Month_Year, SUM(paid) AS 'Total Parking Paid', SUM(remain) AS 'Remaining Parking Fee'
            FROM fees
            WHERE fee_name LIKE 'parking%'
            GROUP BY Month_Year
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thống kê tiền gửi xe: {err}")
        
    def get_service_fee_summary(self):
        """Lấy thống kê tổng hợp tiền dịch vụ."""
        try:
            self.cursor.execute("""
            SELECT DATE_FORMAT(deadline, '%Y-%m') AS Month_Year, SUM(paid) AS 'Total Service Paid', SUM(remain) AS 'Remaining Service Fee'
            FROM fees
            WHERE fee_name LIKE 'service%'
            GROUP BY Month_Year
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thống kê tiền dịch vụ: {err}")
        
    def get_water_fee_summary(self):
        """Lấy thống kê tổng hợp tiền nước."""
        try:
            self.cursor.execute("""
            SELECT DATE_FORMAT(deadline, '%Y-%m') AS Month_Year, SUM(paid) AS 'Total Water Paid', SUM(remain) AS 'Remaining Water Fee'
            FROM fees
            WHERE fee_name LIKE 'water%'
            GROUP BY Month_Year
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thống kê tiền nước: {err}")
        
    def get_electricity_fee_summary(self):
        """Lấy thống kê tổng hợp tiền điện."""
        try:
            self.cursor.execute("""
            SELECT DATE_FORMAT(deadline, '%Y-%m') AS Month_Year, SUM(paid) AS 'Total Electricity Paid', SUM(remain) AS 'Remaining Electricity Fee'
            FROM fees
            WHERE fee_name LIKE 'electricity%'
            GROUP BY Month_Year
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thống kê tiền điện: {err}")
