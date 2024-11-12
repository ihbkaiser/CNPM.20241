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
        ctk.CTkButton(self, text="Manage Fees", command=self.manage_fees, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self, text="Edit Fees", command=self.edit_fees, width=200, height=50).pack(pady=5)
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
    
    def manage_fees(self):
        """Hiển thị giao diện quản lý phí."""
        fees = self.db_manager.get_all_fees()
        if fees:
            self.show_fees_table(fees)
        else:
            self.show_popup("Error", "No fees found!")

        # Hiển thị nút quay lại
        # ctk.CTkButton(self, text="Back", command=self.show_home).pack(pady=10)

    def edit_fees(self):
        """Hiển thị giao diện quản lý phí."""
        userfee = self.db_manager.get_all_userfee()
        if userfee:
            self.show_userfee_table(userfee)
        else:
            self.show_popup("Error", "No fees found!")

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
    
    def show_fees_table(self,fees):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill='both', expand=True)
        ctk.CTkLabel(self.table_frame, text="Fee", font=("Arial", 24)).pack(pady=10)

        # Lấy danh sách các cột từ dữ liệu đầu vào
        columns = list(fees[0].keys())

        # Tạo Treeview với các cột
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", height=25)  # Set larger height for the Treeview

        # Đặt tiêu đề cho các cột và tăng kích thước cột
        column_widths = {column: 150 for column in columns}
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=column_widths[column])

        # Thêm dữ liệu vào Treeview
        for item in fees:
            self.tree.insert("", "end", values=[item.get(column, 'N/A') for column in columns])
        self.tree.pack(pady=10, padx=10, expand=True, fill='both')

        # Thêm nút đóng
        ctk.CTkButton(self.table_frame, text="Close", command=self.show_home).pack(pady=10)

    def show_userfee_table(self,userfee):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill='both', expand=True)
        ctk.CTkLabel(self.table_frame, text="Fee", font=("Arial", 24)).pack(pady=10)

        # Lấy danh sách các cột từ dữ liệu đầu vào
        columns = list(userfee[0].keys())

        # Tạo Treeview với các cột
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", height=25)  # Set larger height for the Treeview

        # Đặt tiêu đề cho các cột và tăng kích thước cột
        column_widths = {column: 150 for column in columns}
        for column in columns:
            self.tree.heading(column, text=column)
            self.tree.column(column, width=column_widths[column])

        # Thêm dữ liệu vào Treeview
        for item in userfee:
            self.tree.insert("", "end", values=[item.get(column, 'N/A') for column in columns])
        # self.tree.bind("<Double-1>", self.on_fee_double_click)
        self.tree.pack(pady=10, padx=10, expand=True, fill='both')

        # Thêm nút đóng
        ctk.CTkButton(self.table_frame, text="Close", command=self.show_home).pack(pady=10)
        ctk.CTkButton(self.table_frame, text="Add Fee", command=self.add_userfee).pack(pady=10)
        ctk.CTkButton(self.table_frame, text="Delete Fee", command=self.delete_userfee).pack(pady=10)

    def show_popup(self, title, message):
        """Hiển thị thông báo lỗi hoặc thông tin."""
        popup = ctk.CTkToplevel(self)
        popup.title(title)
        ctk.CTkLabel(popup, text=message).pack(pady=10)
        ctk.CTkButton(popup, text="Close", command=popup.destroy).pack(pady=10)
    
    def add_userfee(self):
        self.add_window = ctk.CTkToplevel(self)
        self.add_window.title("Add Fee")
        font_large = ("Arial", 16)
        labels = ["Apartment_code", "Fee_name", "Total", "Paid", "Remain", "Residual"]
        entries = {}
        for idx, label in enumerate(labels):
            ctk.CTkLabel(self.add_window, text=label + ":", font=font_large).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(self.add_window, width=200, font=font_large)
            entries[label] = entry
            entry.grid(row=idx, column=1, padx=10, pady=5)
        ctk.CTkButton(self.add_window, text="Add", command=lambda: self.add_userfee2(entries), width=100).grid(row=len(labels), column=0, pady=10)
        ctk.CTkButton(self.add_window, text="Cancel", command=self.add_window.destroy, width=100).grid(row=len(labels), column=1, pady=10)
    
    def add_userfee2(self, entries):
        apartment_code = entries["Apartment_code"].get()
        fee_name = entries["Fee_name"].get()
        total = entries["Total"].get()
        paid = entries["Paid"].get()
        remain = entries["Remain"].get()
        residual = entries["Residual"].get()
        try:
            self.db_manager.add_userfee(apartment_code, fee_name, total, paid, remain, residual)
            self.add_window.destroy()
            data=self.db_manager.get_all_userfee()
            self.refresh_table(data)
        except Exception as e:
            self.show_popup("Error", str(e))

    def delete_userfee(self):
        self.delete_window = ctk.CTkToplevel(self)
        self.delete_window.title("Delete Fee")
        font_large = ("Arial", 16)
        labels = ["Apartment Code", "Fee Name"]
        entries = {}
        for idx, label in enumerate(labels):
            ctk.CTkLabel(self.delete_window, text=label + ":", font=font_large).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(self.delete_window, width=200, font=font_large)
            entries[label] = entry
            entry.grid(row=idx, column=1, padx=10, pady=5)
        ctk.CTkButton(self.delete_window, text="Delete", command=lambda: self.delete_userfee2(entries), width=100).grid(row=len(labels), column=0, pady=10)
        ctk.CTkButton(self.delete_window, text="Cancel", command=self.delete_window.destroy, width=100).grid(row=len(labels), column=1, pady=10)
        
    def delete_userfee2(self, entries):
        apartment_code = entries["Apartment_code"].get()
        fee_name = entries["Fee_name"].get()
        try:
            self.db_manager.delete_userfee(apartment_code, fee_name)
            self.delete_window.destroy()
            data=self.db_manager.get_all_userfee()
            self.refresh_table(data)
        except Exception as e:
            self.show_popup("Error", str(e))

    def refresh_table(self,data):
        if self.tree:
            for item in self.tree.get_children():
                self.tree.delete(item)
            columns = list(data[0].keys())
        
            # Cập nhật các cột trong Treeview
            self.tree["columns"] = columns
            for column in columns:
                self.tree.heading(column, text=column)
                self.tree.column(column, width=150)
            
            # Thêm dữ liệu mới vào Treeview
            for item in data:
                self.tree.insert("", "end", values=[item.get(column, 'N/A') for column in columns])
    
    def on_fee_double_click(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        self.edit_fee_dialog(values)

    def edit_fee_dialog(self, fee_data):
        self.edit_window = ctk.CTkToplevel(self)
        self.edit_window.title("Edit Fee")
        font_large = ("Arial", 16)
        labels = list(fee_data.keys())
        entries = {}
        for idx, label in enumerate(labels):
            ctk.CTkLabel(self.edit_window, text=label + ":", font=font_large).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(self.edit_window, width=200, font=font_large)
            entry.insert(0, fee_data[idx])
            if label == "apartment_code":
                entry.configure(state='disabled')
            entries[label] = entry
            entry.grid(row=idx, column=1, padx=10, pady=5)
        ctk.CTkButton(self.edit_window, text="Save", command=lambda: self.save_user(entries), width=100).grid(row=len(labels), column=0, pady=10)
        ctk.CTkButton(self.edit_window, text="Delete", command=lambda: self.delete_user(entries["apartment_code"].get()), width=100).grid(row=len(labels), column=1, pady=10)

    def logout(self):
        """Đăng xuất và quay lại màn hình đăng nhập."""
        self.destroy()
        self.controller.show_login_frame()