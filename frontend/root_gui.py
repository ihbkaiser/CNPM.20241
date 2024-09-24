import customtkinter as ctk
from tkinter import ttk
from backend.auth import AuthManager
import zxcvbn

class RootGUI(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.controller = parent
        self.user = user  # Lưu thông tin người dùng đã đăng nhập
        self.db_manager = AuthManager().db  # Quản lý cơ sở dữ liệu
        self.show_home()

    def show_home(self):
        """Giao diện chính của người dùng root."""
        # Clear previous widgets instead of destroying the frame
        for widget in self.winfo_children():
            widget.pack_forget()

        ctk.CTkLabel(self, text=f"Welcome, {self.user['full_name']}").pack(pady=10)  # Hiển thị tên người dùng đăng nhập
        ctk.CTkButton(self, text="View Admins", command=self.view_admins, width=200, height=50).pack(pady=5)  # Nút xem danh sách Admins
        ctk.CTkButton(self, text="View Users", command=self.view_users, width=200, height=50).pack(pady=5)    # Nút xem danh sách Users
        ctk.CTkButton(self, text="Create Admin", command=self.create_admin, width=200, height=50).pack(pady=5)  # Nút tạo Admin mới
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
        columns = ("Username", "Account Type", "Full Name", "Apartment Code", "Email", "Phone")
        tree = ttk.Treeview(popup, columns=columns, show="headings", height=25)  # Set larger height for the Treeview

        # Đặt tiêu đề cho các cột và tăng kích thước cột
        column_widths = {
            "Username": 150,
            "Account Type": 150,
            "Full Name": 200,
            "Apartment Code": 150,
            "Email": 200,
            "Phone": 150
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

    def create_admin(self):
        """Chuyển sang giao diện đăng ký admin mới."""
        for widget in self.winfo_children():
            widget.pack_forget()  # Hide RootGUI widgets without destroying the frame

        # Display the AdminRegisterFrame within the same root window
        admin_register_frame = AdminRegisterFrame(self)  # Set user_mode=False for admin
        admin_register_frame.pack(fill="both", expand=True)

    def logout(self):
        """Đăng xuất và quay lại màn hình đăng nhập."""
        self.destroy()
        self.controller.show_login_frame()
class AdminRegisterFrame(ctk.CTkFrame):
    def __init__(self, parent, user_mode=False):
        super().__init__(parent)
        self.controller = parent
        self.is_user = user_mode

        # Custom fonts and sizes
        font_large = ("Arial", 20)
        button_width = 250
        entry_width = 300
        entry_height = 50

        # Username entry
        ctk.CTkLabel(self, text="Username:", font=font_large).grid(row=0, column=0, padx=20, pady=10, sticky="w")
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=entry_width, height=entry_height, font=font_large)
        self.username_entry.grid(row=0, column=1, pady=10, padx=20, sticky="ew")
        self.username_label = ctk.CTkLabel(self, text="", text_color="red")
        self.username_label.grid(row=1, column=1)

        # Password entry
        ctk.CTkLabel(self, text="Password:", font=font_large).grid(row=2, column=0, padx=20, pady=10, sticky="w")
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=entry_width, height=entry_height, font=font_large)
        self.password_entry.grid(row=2, column=1, pady=10, padx=20, sticky="ew")
        self.password_label = ctk.CTkLabel(self, text="", text_color="red")
        self.password_label.grid(row=3, column=1)

        # Add a label to display password strength
        self.password_strength_label = ctk.CTkLabel(self, text="", font=("Arial", 16), text_color="gray")
        self.password_strength_label.grid(row=3, column=0, columnspan=2, padx=20, sticky="w")

        # Bind the password entry to update password strength dynamically
        self.password_entry.bind("<KeyRelease>", self.check_password_strength)

        # Add button for showing/hiding password
        self.password_visible = False
        self.eye_button = ctk.CTkButton(self, text="👁", width=50, command=self.toggle_password)
        self.eye_button.grid(row=2, column=2, padx=10)

        # Confirm password entry
        ctk.CTkLabel(self, text="Confirm Password:", font=font_large).grid(row=4, column=0, padx=20, pady=10, sticky="w")
        self.confirm_password_entry = ctk.CTkEntry(self, placeholder_text="Confirm Password", show="*", width=entry_width, height=entry_height, font=font_large)
        self.confirm_password_entry.grid(row=4, column=1, pady=10, padx=20, sticky="ew")
        self.confirm_password_label = ctk.CTkLabel(self, text="", text_color="red")
        self.confirm_password_label.grid(row=5, column=1)

        # Full name entry
        ctk.CTkLabel(self, text="Họ tên:", font=font_large).grid(row=6, column=0, padx=20, pady=10, sticky="w")
        self.fullname_entry = ctk.CTkEntry(self, placeholder_text="Họ tên", width=entry_width, height=entry_height, font=font_large)
        self.fullname_entry.grid(row=6, column=1, pady=10, padx=20, sticky="ew")
        self.fullname_label = ctk.CTkLabel(self, text="", text_color="red")
        self.fullname_label.grid(row=7, column=1)

        # Apartment code entry
        if self.is_user:
            code_name = "Mã căn hộ:"
        else:
            code_name = "Mã cán bộ:"
        ctk.CTkLabel(self, text=code_name, font=font_large).grid(row=8, column=0, padx=20, pady=10, sticky="w")
        self.apartment_code_entry = ctk.CTkEntry(self, placeholder_text="Mã căn hộ", width=entry_width, height=entry_height, font=font_large)
        self.apartment_code_entry.grid(row=8, column=1, pady=10, padx=20, sticky="ew")
        self.apartment_code_label = ctk.CTkLabel(self, text="", text_color="red")
        self.apartment_code_label.grid(row=9, column=1)

        # Register button
        self.register_button = ctk.CTkButton(self, text="Đăng ký tài khoản", width=button_width, height=60, font=font_large, command=self.register)
        self.register_button.grid(row=10, column=1, pady=20)

        # Switch to home frame with Return button
        self.switch_login_button = ctk.CTkButton(self, text="Quay lại", width=button_width, height=60, font=font_large, command=self.return_to_home)
        self.switch_login_button.grid(row=11, column=1, pady=20)

        # Center the grid elements
        self.grid_columnconfigure(0, weight=1)  # Left label column
        self.grid_columnconfigure(1, weight=1)  # Center input field column
        self.grid_columnconfigure(2, weight=1)  # Right for button (like eye button)

    def toggle_password(self):
        """Toggle password visibility."""
        if self.password_visible:
            self.password_entry.configure(show="*")
            self.eye_button.configure(text="👁")
        else:
            self.password_entry.configure(show="")
            self.eye_button.configure(text="🚫")
        self.password_visible = not self.password_visible

    def check_password_strength(self, event=None):
        """Check the password strength and update the label."""
        password = self.password_entry.get()
        result = zxcvbn.zxcvbn(password)

        strength_score = result['score']
        feedback = result['feedback']['suggestions']

        # Convert strength score to a user-friendly message
        strength_text = {0: "Very Weak", 1: "Weak", 2: "Medium", 3: "Strong", 4: "Very Strong"}
        strength_color = {0: "red", 1: "red", 2: "orange", 3: "green", 4: "green"}

        self.password_strength_label.configure(text=f"Strength: {strength_text[strength_score]}", text_color=strength_color[strength_score])

    def register(self):
        """Perform register action."""
        # Get input values
        username = self.username_entry.get()
        password = self.password_entry.get()
        confirm_password = self.confirm_password_entry.get()
        full_name = self.fullname_entry.get()
        apartment_code = self.apartment_code_entry.get()

        # Clear previous warnings
        self.clear_warnings()

        # Input validation
        valid = True
        if not username:
            self.username_label.configure(text="Username is required")
            valid = False
        if not password:
            self.password_label.configure(text="Password is required")
            valid = False
        elif password != confirm_password:
            self.confirm_password_label.configure(text="Passwords do not match")
            valid = False
        if not full_name:
            self.fullname_label.configure(text="Full name is required")
            valid = False
        if not apartment_code:
            self.apartment_code_label.configure(text="Apartment code is required")
            valid = False

        if not valid:
            return

        # Attempt to register the user
        try:
            if self.is_user:
                self.controller.db_manager.add_user(username, password, full_name, apartment_code)
            else:
                self.controller.db_manager.add_user(username, password, full_name, apartment_code, account_type='admin')

            # Show success message
            ctk.CTkLabel(self, text="Admin đăng ký thành công!", font=("Arial", 18)).grid(row=12, column=1, pady=10)

        except Exception as e:
            ctk.CTkLabel(self, text=str(e), font=("Arial", 18), text_color="red").grid(row=12, column=1, pady=10)

    def clear_warnings(self):
        """Clear all warning labels."""
        self.username_label.configure(text="")
        self.password_label.configure(text="")
        self.confirm_password_label.configure(text="")
        self.fullname_label.configure(text="")
        self.apartment_code_label.configure(text="")

    def return_to_home(self):
        """Return to the RootGUI home screen."""
        for widget in self.winfo_children():
            widget.pack_forget()  # Hide AdminRegisterFrame widgets

        # Show the home screen widgets of RootGUI
        self.controller.show_home()
