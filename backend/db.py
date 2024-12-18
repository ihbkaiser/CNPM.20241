import mysql.connector

class DBManager:
    def __init__(self, host,port, user, password, database):
        # create if not exists database
        self.create_database(host,port, user, password, database)
        self.conn = mysql.connector.connect(
            host=host,
            port=port,
            user=user,
            password=password,
            database=database
        )

        self.cursor = self.conn.cursor(dictionary=True)
        self.create_tables()
    def create_database(self, host,port, user, password, database):
        conn = mysql.connector.connect(
            host=host,
            port=port,
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
            username VARCHAR(255) NOT NULL,
            password VARCHAR(255) NOT NULL,
            account_type ENUM('root', 'admin', 'user') NOT NULL,
            full_name NVARCHAR(255) NOT NULL,
            phone_number VARCHAR(20) NOT NULL,
            apartment_code VARCHAR(50) PRIMARY KEY,
            email VARCHAR(255) DEFAULT NULL,
            dob DATE DEFAULT NULL,
            gender ENUM('male','female','undefined') DEFAULT NULL,
            id_card VARCHAR(20) DEFAULT NULL,
            hometown NVARCHAR(255) DEFAULT NULL
        );                
        """)
        self.conn.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS fees (
            fee_name VARCHAR(50) PRIMARY KEY,
            deadline datetime,
            total int DEFAULT 0,
            paid int DEFAULT 0,
            remain int DEFAULT 0,
            type ENUM('required', 'unrequired') NOT NULL
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
            FOREIGN KEY (apartment_code) REFERENCES users(apartment_code),
            FOREIGN KEY (fee_name) REFERENCES fees(fee_name)
        ); 
        """)
        self.conn.commit()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS noti (
            apartment_code VARCHAR(50) NOT NULL,
            apartment_code2 VARCHAR(50) NOT NULL,
            title VARCHAR(100) NOT NULL,
            content TEXT NOT NULL,
            time DATETIME DEFAULT CURRENT_TIMESTAMP,
            foreign key (apartment_code) references users(apartment_code),
            foreign key (apartment_code2) references users(apartment_code)
        ); 
        """)
        self.conn.commit()

        self.cursor.execute("DROP TRIGGER IF EXISTS update_fees_paid")
        self.conn.commit()
        
        trigger_sql = """
        CREATE TRIGGER update_fees_paid
        AFTER INSERT ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.paid = (
                SELECT COALESCE(SUM(uf.paid), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = NEW.fee_name;
        END
        """
        self.cursor.execute(trigger_sql)
        self.conn.commit()

        self.cursor.execute("""
        DROP TRIGGER IF EXISTS update_fees_paid2
        """)
        self.cursor.execute("""
        CREATE TRIGGER update_fees_paid2
        AFTER DELETE ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.paid = (
                SELECT COALESCE(SUM(uf.paid), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = OLD.fee_name;
        END
        """)
        self.conn.commit()

        self.cursor.execute("""
        DROP TRIGGER IF EXISTS update_fees_paid3
        """)
        self.cursor.execute("""
        CREATE TRIGGER update_fees_paid3
        AFTER UPDATE ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.paid = (
                SELECT COALESCE(SUM(uf.paid), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = NEW.fee_name;
        END
        """)
        self.conn.commit()

        self.cursor.execute("""
        DROP TRIGGER IF EXISTS update_fees_total
        """)
        self.cursor.execute("""
        CREATE TRIGGER update_fees_total
        AFTER INSERT ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.total = (
                SELECT COALESCE(SUM(uf.total), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = NEW.fee_name;
        END
        """)
        self.conn.commit()

        self.cursor.execute("""
        DROP TRIGGER IF EXISTS update_fees_total2
        """)
        self.cursor.execute("""
        CREATE TRIGGER update_fees_total2
        AFTER DELETE ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.total = (
                SELECT COALESCE(SUM(uf.total), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = OLD.fee_name;
        END
        """)
        self.conn.commit()

        self.cursor.execute("""
        DROP TRIGGER IF EXISTS update_fees_total3
        """)
        self.cursor.execute("""
        CREATE TRIGGER update_fees_total3
        AFTER UPDATE ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.total = (
                SELECT COALESCE(SUM(uf.total), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = NEW.fee_name;
        END
        """)
        self.conn.commit()

        self.cursor.execute("""
        DROP TRIGGER IF EXISTS update_fees_remain
        """)
        self.cursor.execute("""
        CREATE TRIGGER update_fees_remain
        AFTER INSERT ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.remain = (
                SELECT COALESCE(SUM(uf.remain), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = NEW.fee_name;
        END
        """)
        self.conn.commit()

        self.cursor.execute("""
        DROP TRIGGER IF EXISTS update_fees_remain2
        """)
        self.cursor.execute("""
        CREATE TRIGGER update_fees_remain2
        AFTER DELETE ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.remain = (
                SELECT COALESCE(SUM(uf.remain), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = OLD.fee_name;
        END
        """)
        self.conn.commit()

        self.cursor.execute("""
        DROP TRIGGER IF EXISTS update_fees_remain3
        """)
        self.cursor.execute("""
        CREATE TRIGGER update_fees_remain3
        AFTER UPDATE ON userfee
        FOR EACH ROW
        BEGIN
            UPDATE fees f
            SET f.remain = (
                SELECT COALESCE(SUM(uf.remain), 0)
                FROM userfee uf
                WHERE uf.fee_name = f.fee_name
            )
            WHERE f.fee_name = NEW.fee_name;
        END
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

    def update_user(self, username, password, account_type, full_name, phone_number,  apartment_code, email):
        self.cursor.execute("UPDATE users SET password = %s, account_type = %s, full_name = %s, phone_number = %s, apartment_code = %s, email = %s WHERE username = %s",
                            (password, account_type, full_name, phone_number, apartment_code, email, username))
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

    
    def add_userfee(self, apartment_code, fee_name, total, paid, remain):
        try:
            self.cursor.execute("""
            INSERT INTO userfee ( apartment_code, fee_name, total, paid, remain)
            VALUES (%s, %s, %s, %s, %s, %s)
            """, (apartment_code, fee_name, total, paid, remain))
            self.conn.commit() 
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi thêm căn hộ: {err}")
        
    def delete_userfee(self, apartment_code, fee_name):
        self.cursor.execute("DELETE FROM userfee WHERE apartment_code = %s AND fee_name = %s", (apartment_code, fee_name))
        self.conn.commit()
    
    def update_userfee(self, apartment_code, fee_name, total, paid, remain):
        self.cursor.execute("UPDATE userfee SET total = %s, paid = %s, remain = %s WHERE apartment_code = %s AND fee_name = %s",
                            (total, paid, remain, apartment_code, fee_name))
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
        total = row['total']
        money_paid = row['paid']
        money_remain = row['remain']
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
            'total': total,
            'money_paid': money_paid,
            'money_remain': money_remain,
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
        paid += pay_money
        remain = total - paid
        self.cursor.execute("UPDATE userfee SET paid = %s, remain = %s WHERE apartment_code = %s AND fee_name = %s",
                            (paid, remain, apartment_code, fee_name))
        self.conn.commit()

    def close(self):
        self.conn.close()

    def get_parking_fee_summary(self):
        """Lấy thống kê tổng hợp tiền gửi xe."""
        try:
            self.cursor.execute("""
            SELECT DATE_FORMAT(deadline, '%Y-%m') AS Month_Year, SUM(paid) AS 'Total_Paid', SUM(remain) AS 'Remaining_Fee'
            FROM fees
            WHERE fee_name LIKE 'Parking%'
            GROUP BY Month_Year
            order by Month_Year
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thống kê tiền gửi xe: {err}")
        
    def get_service_fee_summary(self):
        """Lấy thống kê tổng hợp tiền dịch vụ."""
        try:
            self.cursor.execute("""
            SELECT DATE_FORMAT(deadline, '%Y-%m') AS Month_Year, SUM(paid) AS 'Total_Paid', SUM(remain) AS 'Remaining_Fee'
            FROM fees
            WHERE fee_name LIKE 'Service%'
            GROUP BY Month_Year
            order by Month_Year
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thống kê tiền dịch vụ: {err}")
        
    def get_water_fee_summary(self):
        """Lấy thống kê tổng hợp tiền nước."""
        try:
            self.cursor.execute("""
            SELECT DATE_FORMAT(deadline, '%Y-%m') AS Month_Year, SUM(paid) AS 'Total_Paid', SUM(remain) AS 'Remaining_Fee'
            FROM fees
            WHERE fee_name LIKE 'Water%'
            GROUP BY Month_Year
            order by Month_Year
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thống kê tiền nước: {err}")
        
    def get_electricity_fee_summary(self):
        try:
            self.cursor.execute("""
            SELECT DATE_FORMAT(deadline, '%Y-%m') AS Month_Year, SUM(paid) AS Total_Paid, SUM(remain) AS Remaining_Fee
            FROM fees
            WHERE fee_name LIKE 'Electricity%'
            GROUP BY Month_Year
            ORDER BY Month_Year
            """)
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            print(f"Error fetching electricity fee summary: {err}")
            return []
        
    def get_userfee_by_apartment_code(self, apartment_code):
        """Lấy thông tin userfee theo mã căn hộ."""
        try:
            self.cursor.execute("""
            SELECT fee_name, paid, remain FROM userfee WHERE apartment_code = %s
            """, (apartment_code,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thông tin userfee: {err}")

    def view_fee_by_apartment_code(self, apartment_code):
        """Lấy thông tin userfee theo mã căn hộ."""
        try:
            self.cursor.execute("""
            SELECT userfee.fee_name,userfee.total,userfee.paid,userfee.remain,deadline FROM userfee 
            JOIN fees ON userfee.fee_name = fees.fee_name
            WHERE apartment_code = %s
            """, (apartment_code,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thông tin userfee: {err}")
        
    def send_noti(self, apartment_code, apartment_code2, title, content):
        try:
            self.cursor.execute("""
            INSERT INTO noti (apartment_code, apartment_code2, title, content)
            VALUES (%s, %s, %s, %s)
            """, (apartment_code, apartment_code2, title, content))
            self.conn.commit() 
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi gửi thông báo: {err}")
    
    def get_noti(self, apartment_code):
        try:
            self.cursor.execute("""
            SELECT * FROM noti WHERE apartment_code = %s
            """, (apartment_code,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thông báo: {err}")
        
    def get_user_by_apartment_code(self, apt_code):
        try:
            self.cursor.execute("""
            SELECT * FROM users WHERE apartment_code = %s
            """, (apt_code,))
            return self.cursor.fetchone()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thông tin người dùng: {err}")
        
    def get_noti_by_apartment_code(self, apt_code):
        try:
            self.cursor.execute("""
            SELECT full_name, title, content,time FROM noti 
            JOIN users ON users.apartment_code= noti.apartment_code WHERE apartment_code2 = %s or apartment_code = %s
            order by time desc
            """, (apt_code,))
            return self.cursor.fetchall()
        except mysql.connector.Error as err:
            raise Exception(f"Lỗi khi lấy thông tin thông báo: {err}")