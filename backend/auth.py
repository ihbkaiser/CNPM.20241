from backend.db import DBManager
import yaml
import re

class AuthManager:
    def __init__(self):
        try:
            with open("config.yml", 'r') as ymlfile:
                cfg = yaml.safe_load(ymlfile)
        except:
            raise Exception("Cannot open config.yml")
        self.db = DBManager(host=cfg['db']['host'], port = cfg['db']['port'],user=cfg['db']['user'], password=cfg['db']['password'], database=cfg['db']['database'])

        

    def register_user(self, username, password, full_name, phone_number, apartment_code, confirm_password, account_type='user', email=None):
        """Đăng ký người dùng mới."""
        if password != confirm_password:
            raise Exception("Password and confirm password do not match. Please enter the same password in both fields.")
        if not username:
            raise Exception("Username is required. Please enter a valid username.")
        if not password:
            raise Exception("Password is required. Please enter a valid password.")
        if not full_name:
            raise Exception("Full name is required. Please enter your full name.")
        if not phone_number:
            raise Exception("Phone number is required. Please enter a valid phone number.")
        if not re.match(r'^\d{10}$', phone_number):
            raise Exception("Invalid phone number. Phone number must be 10 digits.")
        if not apartment_code:
            raise Exception("Apartment code is required. Please enter a valid apartment code.")
        
        self.db.add_user(username, password, full_name, phone_number, apartment_code, email=email, account_type=account_type)

    def login(self, username, password):
        user = self.db.get_user(username)
        if user and user['password'] == password:
            return user
        raise Exception("Thông tin đăng nhập không chính xác")
    
    def get_users(self, account_type, logged_in_user):
        if logged_in_user['account_type'] == 'root':
            return self.db.get_all_users(account_type)
        raise Exception("Không có quyền truy cập")

    def change_password(self, username, phone_number , new_password):
        """Thay đổi mật khẩu của người dùng."""
        user = self.db.get_user(username)
        if phone_number==user['phone_number']:
            self.db.update_user_password(username, new_password)
        else:
            raise Exception("Số điện thoại không chính xác")
