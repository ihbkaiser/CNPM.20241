import customtkinter as ctk
from tkinter import ttk
from backend.auth import AuthManager
import zxcvbn

class RootGUI(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.controller = parent
        self.user = user
        self.db_manager = AuthManager().db
        self.show_home()

    def show_home(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        ctk.CTkLabel(self, text=f"Welcome, {self.user['full_name']}").pack(pady=10)
        ctk.CTkButton(self, text="Edit Admins", command=self.edit_admins, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self, text="Edit Users", command=self.edit_users, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self, text="Logout", command=self.logout, width=200, height=50).pack(pady=5)

    def edit_admins(self):
        self.current_account_type = 'admin'
        admins = self.db_manager.get_all_users(account_type='admin')
        if admins:
            self.show_edit_table("Admins", admins)
        else:
            self.show_popup("Error", "No Admins found!")

    def edit_users(self):
        self.current_account_type = 'user'
        users = self.db_manager.get_all_users(account_type='user')
        if users:
            self.show_edit_table("Users", users)
        else:
            self.show_popup("Error", "No Users found!")

    def show_edit_table(self, title, data):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill='both', expand=True)
        ctk.CTkLabel(self.table_frame, text=title, font=("Arial", 24)).pack(pady=10)
        columns = ("Username", "Account Type", "Full Name", "Apartment Code", "Email", "Phone")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", height=25)
        column_widths = {
            "Username": 150,
            "Account Type": 150,
            "Full Name": 200,
            "Apartment Code": 150,
            "Email": 200,
            "Phone": 150
        }
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[col])
        for item in data:
            self.tree.insert("", "end", values=(
                item.get('username', 'N/A'),
                item.get('account_type', 'N/A'),
                item.get('full_name', 'N/A'),
                item.get('apartment_code', 'N/A'),
                item.get('email', 'N/A'),
                item.get('phone', 'N/A')
            ))
        self.tree.bind("<Double-1>", self.on_item_double_click)
        self.tree.pack(pady=10, padx=10, expand=True, fill='both')
        ctk.CTkButton(self.table_frame, text="Add New", command=self.add_new_user, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self.table_frame, text="Return", command=self.return_to_home, width=200, height=50).pack(pady=10)

    def on_item_double_click(self, event):
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        self.edit_user_dialog(values)

    def edit_user_dialog(self, user_data):
        self.edit_window = ctk.CTkToplevel(self)
        self.edit_window.title("Edit User")
        font_large = ("Arial", 16)
        labels = ["Username", "Account Type", "Full Name", "Apartment Code", "Email", "Phone"]
        entries = {}
        for idx, label in enumerate(labels):
            ctk.CTkLabel(self.edit_window, text=label + ":", font=font_large).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(self.edit_window, width=200, font=font_large)
            entry.insert(0, user_data[idx])
            if label == "Username":
                entry.configure(state='disabled')
            entries[label] = entry
            entry.grid(row=idx, column=1, padx=10, pady=5)
        ctk.CTkButton(self.edit_window, text="Save", command=lambda: self.save_user(entries), width=100).grid(row=len(labels), column=0, pady=10)
        ctk.CTkButton(self.edit_window, text="Delete", command=lambda: self.delete_user(entries["Username"].get()), width=100).grid(row=len(labels), column=1, pady=10)

    def save_user(self, entries):
        username = entries["Username"].get()
        account_type = entries["Account Type"].get()
        full_name = entries["Full Name"].get()
        apartment_code = entries["Apartment Code"].get()
        email = entries["Email"].get()
        phone = entries["Phone"].get()
        self.db_manager.update_user(username, account_type=account_type, full_name=full_name,
                                    apartment_code=apartment_code, email=email, phone=phone)
        self.edit_window.destroy()
        self.refresh_table()

    def delete_user(self, username):
        confirm = ctk.CTkToplevel(self)
        confirm.title("Confirm Delete")
        ctk.CTkLabel(confirm, text=f"Are you sure you want to delete user '{username}'?").pack(pady=10)
        ctk.CTkButton(confirm, text="Yes", command=lambda: self.confirm_delete(username, confirm)).pack(side='left', padx=20, pady=10)
        ctk.CTkButton(confirm, text="No", command=confirm.destroy).pack(side='right', padx=20, pady=10)

    def confirm_delete(self, username, confirm_window):
        self.db_manager.delete_user(username)
        confirm_window.destroy()
        self.edit_window.destroy()
        self.refresh_table()

    def add_new_user(self):
        self.edit_window = ctk.CTkToplevel(self)
        self.edit_window.title("Add New User")
        font_large = ("Arial", 16)
        labels = ["Username", "Password", "Confirm Password", "Account Type", "Full Name", "Apartment Code", "Email", "Phone"]
        entries = {}
        for idx, label in enumerate(labels):
            ctk.CTkLabel(self.edit_window, text=label + ":", font=font_large).grid(row=idx, column=0, padx=10, pady=5, sticky="e")
            entry = ctk.CTkEntry(self.edit_window, width=200, font=font_large)
            if label == "Password" or label == "Confirm Password":
                entry.configure(show='*')
            entries[label] = entry
            entry.grid(row=idx, column=1, padx=10, pady=5)
        entries["Account Type"].insert(0, self.current_account_type)
        ctk.CTkButton(self.edit_window, text="Create", command=lambda: self.create_user(entries), width=100).grid(row=len(labels), column=0, pady=10)
        ctk.CTkButton(self.edit_window, text="Cancel", command=self.edit_window.destroy, width=100).grid(row=len(labels), column=1, pady=10)

    def create_user(self, entries):
        username = entries["Username"].get()
        password = entries["Password"].get()
        confirm_password = entries["Confirm Password"].get()
        account_type = entries["Account Type"].get()
        full_name = entries["Full Name"].get()
        apartment_code = entries["Apartment Code"].get()
        email = entries["Email"].get()
        phone = entries["Phone"].get()
        if password != confirm_password:
            self.show_popup("Error", "Passwords do not match!")
            return
        try:
            self.db_manager.add_user(username, password, full_name, apartment_code, account_type=account_type, email=email, phone=phone)
            self.edit_window.destroy()
            self.refresh_table()
        except Exception as e:
            self.show_popup("Error", str(e))

    def refresh_table(self):
        if self.tree:
            for item in self.tree.get_children():
                self.tree.delete(item)
            account_type = self.current_account_type
            data = self.db_manager.get_all_users(account_type=account_type)
            for item in data:
                self.tree.insert("", "end", values=(
                    item.get('username', 'N/A'),
                    item.get('account_type', 'N/A'),
                    item.get('full_name', 'N/A'),
                    item.get('apartment_code', 'N/A'),
                    item.get('email', 'N/A'),
                    item.get('phone', 'N/A')
                ))

    def return_to_home(self):
        self.table_frame.destroy()
        self.show_home()

    def show_popup(self, title, message):
        popup = ctk.CTkToplevel(self)
        popup.title(title)
        ctk.CTkLabel(popup, text=message).pack(pady=10)
        ctk.CTkButton(popup, text="Close", command=popup.destroy).pack(pady=10)

    def logout(self):
        self.destroy()
        self.controller.show_login_frame()
