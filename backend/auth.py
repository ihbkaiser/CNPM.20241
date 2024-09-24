from backend.db import DBManager

class AuthManager:
    def __init__(self):
        self.db = DBManager(host="localhost",user="root", password="IHBKaiser@04", database="CNPMdb")
        

    def register_user(self, username, password, full_name, apartment_code, account_type='user', email=None, phone=None):
        self.db.add_user(username, password, full_name, apartment_code, email=email, phone=phone, account_type=account_type) 

    def login(self, username, password):
        user = self.db.get_user(username)
        if user and user['password'] == password:
            return user
        raise Exception("Thông tin đăng nhập không chính xác")

    def get_users(self, account_type, logged_in_user):
        if logged_in_user['account_type'] == 'root':
            return self.db.get_all_users(account_type)
        raise Exception("Không có quyền truy cập")
