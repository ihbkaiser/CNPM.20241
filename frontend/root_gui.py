# frontend/root_gui.py

import customtkinter as ctk
from tkinter import ttk
from backend.auth import AuthManager

class RootGUI(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.controller = parent
        self.user = user  # Lưu thông tin người dùng đã đăng nhập
        self.db_manager = AuthManager().db  # Quản lý cơ sở dữ liệu

        # Giao diện chính của người dùng root
        ctk.CTkLabel(self, text=f"Welcome, {self.user['full_name']}").pack(pady=10)  # Hiển thị tên người dùng đăng nhập
        ctk.CTkButton(self, text="View Admins", command=self.view_admins).pack(pady=5)  # Nút xem danh sách Admins
        ctk.CTkButton(self, text="View Users", command=self.view_users).pack(pady=5)    # Nút xem danh sách Users
        ctk.CTkButton(self, text="Logout", command=self.logout).pack(pady=5)            # Nút đăng xuất

    def view_admins(self):
        """Lấy danh sách Admins từ cơ sở dữ liệu và hiển thị trong bảng."""
        admins = self.db_manager.get_all_users(account_type='root')  # Lấy danh sách admin từ db (cần kiểm tra lại account_type)
        if admins:
            self.show_table("Admins", admins)
        else:
            self.show_popup("Error", "No Admins found!")

    def view_users(self):
        """Lấy danh sách Users từ cơ sở dữ liệu và hiển thị trong bảng."""
        users = self.db_manager.get_all_users(account_type='user')  # Lấy danh sách user từ db
        if users:
            self.show_table("Users", users)
        else:
            self.show_popup("Error", "No Users found!")

    def show_table(self, title, data):
        """Hiển thị danh sách người dùng trong một bảng (popup)."""
        popup = ctk.CTkToplevel(self)  # Tạo cửa sổ popup
        popup.title(title)

        # Tạo Treeview với các cột
        columns = ("Username", "Account Type", "Full Name", "Apartment Code", "Email", "Phone")
        tree = ttk.Treeview(popup, columns=columns, show="headings")

        # Đặt tiêu đề cho các cột
        for col in columns:
            tree.heading(col, text=col)

        # Chèn dữ liệu vào bảng
        for item in data:
            tree.insert("", "end", values=(
                item.get('username', 'N/A'), 
                item.get('account_type', 'N/A'), 
                item.get('full_name', 'N/A'), 
                item.get('apartment_code', 'N/A'), 
                item.get('email', 'N/A'), 
                item.get('phone', 'N/A')
            ))

        tree.pack(pady=10, padx=10, expand=True, fill='both')

        # Thêm nút đóng
        ctk.CTkButton(popup, text="Close", command=popup.destroy).pack(pady=10)

    def show_popup(self, title, message):
        """Hiển thị thông báo lỗi hoặc thông tin."""
        popup = ctk.CTkToplevel(self)
        popup.title(title)
        ctk.CTkLabel(popup, text=message).pack(pady=10)
        ctk.CTkButton(popup, text="Close", command=popup.destroy).pack(pady=10)

    def logout(self):
        """Đăng xuất và quay lại màn hình đăng nhập."""
        self.controller.show_login_frame()
