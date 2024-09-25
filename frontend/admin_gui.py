import customtkinter as ctk
from tkinter import ttk
from backend.auth import AuthManager
from frontend.root_gui import RootGUI  # Import RootGUI to extend it

class AdminGUI(RootGUI):
    def __init__(self, parent, user):
        # Initialize the parent class (RootGUI)
        super().__init__(parent, user)

    def show_home(self):
        """Giao diện chính của người dùng admin (không có nút Create Admin)."""
        # Clear previous widgets
        for widget in self.winfo_children():
            widget.pack_forget()

        # Show the remaining buttons and labels
        ctk.CTkLabel(self, text=f"Welcome, {self.user['full_name']}").pack(pady=10)  # Hiển thị tên người dùng đăng nhập
        ctk.CTkButton(self, text="View Admins", command=self.view_admins, width=200, height=50).pack(pady=5)  # Nút xem danh sách Admins
        ctk.CTkButton(self, text="View Users", command=self.view_users, width=200, height=50).pack(pady=5)    # Nút xem danh sách Users
        # Notice there's no "Create Admin" button here
        ctk.CTkButton(self, text="Logout", command=self.logout, width=200, height=50).pack(pady=5)            # Nút đăng xuất

    def view_admins(self):
        """Lấy danh sách Admins từ cơ sở dữ liệu và hiển thị trong bảng."""
        admins = self.db_manager.get_all_users(account_type='admin')  # Lấy danh sách admin từ db (account_type="admin")
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
        popup.geometry("800x600")  # Set larger size for the popup window

        # Tạo Treeview với các cột
        columns = ("Username", "Account Type", "Full Name", "Phone Number", "Apartment Code", "Email")
        tree = ttk.Treeview(popup, columns=columns, show="headings", height=25)  # Set larger height for the Treeview

        # Đặt tiêu đề cho các cột và tăng kích thước cột
        column_widths = {
            "Username": 150,
            "Account Type": 150,
            "Full Name": 200,
            "Phone Number": 150,
            "Apartment Code": 150,
            "Email": 200
        }

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=column_widths[col])

        # Chèn dữ liệu vào bảng
        for item in data:
            tree.insert("", "end", values=(
                item.get('username', 'N/A'), 
                item.get('account_type', 'N/A'), 
                item.get('full_name', 'N/A'), 
                item.get('phone_number', 'N/A'),
                item.get('apartment_code', 'N/A'), 
                item.get('email', 'N/A')
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
        self.destroy()
        self.controller.show_login_frame()
