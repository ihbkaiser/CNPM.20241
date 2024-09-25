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

<<<<<<< Updated upstream
    def show_table(self, title, data):
        """Hiển thị danh sách người dùng trong một bảng (popup)."""
        popup = ctk.CTkToplevel(self)  # Tạo cửa sổ popup
        popup.title(title)
        popup.geometry("800x600")  # Set larger size for the popup window

        # Tạo Treeview với các cột
        columns = ("Username", "Password", "Full Name", "Apartment Code", "Email", "Phone")
        tree = ttk.Treeview(popup, columns=columns, show="headings", height=25)  # Set larger height for the Treeview

        # Đặt tiêu đề cho các cột và tăng kích thước cột
=======
    def show_edit_table(self, title, data):
        for widget in self.winfo_children():
            widget.pack_forget()
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill='both', expand=True)
        ctk.CTkLabel(self.table_frame, text=title, font=("Arial", 24)).pack(pady=10)
        columns = ("Username", "Account Type", "Full Name", "Apartment Code", "Email", "Phone")
        self.tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", height=25)
>>>>>>> Stashed changes
        column_widths = {
            "Username": 150,
            "Password": 150,
            "Full Name": 200,
            "Apartment Code": 150,
            "Email": 200,
            "Phone": 150
        }
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=column_widths[col])
        for item in data:
<<<<<<< Updated upstream
            tree.insert("", "end", values=(
                item.get('username', 'N/A'), 
                item.get('password', 'N/A'), 
                item.get('full_name', 'N/A'), 
                item.get('apartment_code', 'N/A'), 
                item.get('email', 'N/A'), 
=======
            self.tree.insert("", "end", values=(
                item.get('username', 'N/A'),
                item.get('account_type', 'N/A'),
                item.get('full_name', 'N/A'),
                item.get('apartment_code', 'N/A'),
                item.get('email', 'N/A'),
>>>>>>> Stashed changes
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
        ctk.CTkButton(
            self.edit_window,
            text="Save",
            command=lambda: self.save_user(entries),
            width=100
        ).grid(row=len(labels), column=0, pady=10)
        ctk.CTkButton(
            self.edit_window,
            text="Delete",
            command=lambda: self.delete_user(entries["Username"].get()),
            width=100,
            fg_color="red"
        ).grid(row=len(labels), column=1, pady=10)

    def save_user(self, entries):
        username = entries["Username"].get()
        account_type = entries["Account Type"].get()
        full_name = entries["Full Name"].get()
        apartment_code = entries["Apartment Code"].get()
        email = entries["Email"].get()
        phone = entries["Phone"].get()
        self.db_manager.update_user(
            username,
            account_type=account_type,
            full_name=full_name,
            apartment_code=apartment_code,
            email=email,
            phone=phone
        )
        self.edit_window.destroy()
        self.refresh_table()

    def delete_user(self, username):
        confirm = ctk.CTkToplevel(self)
        confirm.title("Confirm Delete")
        ctk.CTkLabel(confirm, text=f"Are you sure you want to delete user '{username}'?").pack(pady=10)
        ctk.CTkButton(
            confirm,
            text="Yes",
            command=lambda: self.confirm_delete(username, confirm),
            fg_color="red"
        ).pack(side='left', padx=20, pady=10)
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
        ctk.CTkButton(
            self.edit_window,
            text="Create",
            command=lambda: self.create_user(entries),
            width=100
        ).grid(row=len(labels), column=0, pady=10)
        ctk.CTkButton(
            self.edit_window,
            text="Cancel",
            command=self.edit_window.destroy,
            width=100
        ).grid(row=len(labels), column=1, pady=10)

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
            self.db_manager.add_user(
                username,
                password,
                full_name,
                apartment_code,
                account_type=account_type,
                email=email,
                phone=phone
            )
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
<<<<<<< Updated upstream
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
        ctk.CTkLabel(self, text="Full name:", font=font_large).grid(row=6, column=0, padx=20, pady=10, sticky="w")
        self.fullname_entry = ctk.CTkEntry(self, placeholder_text="Full name", width=entry_width, height=entry_height, font=font_large)
        self.fullname_entry.grid(row=6, column=1, pady=10, padx=20, sticky="ew")
        self.fullname_label = ctk.CTkLabel(self, text="", text_color="red")
        self.fullname_label.grid(row=7, column=1)

        # Apartment code entry
        if self.is_user:
            code_name = "Apartment ID:"
        else:
            code_name = "Officer ID:"
        ctk.CTkLabel(self, text=code_name, font=font_large).grid(row=8, column=0, padx=20, pady=10, sticky="w")
        self.apartment_code_entry = ctk.CTkEntry(self, placeholder_text="Apartment ID", width=entry_width, height=entry_height, font=font_large)
        self.apartment_code_entry.grid(row=8, column=1, pady=10, padx=20, sticky="ew")
        self.apartment_code_label = ctk.CTkLabel(self, text="", text_color="red")
        self.apartment_code_label.grid(row=9, column=1)

        # Register button
        self.register_button = ctk.CTkButton(self, text="Sign up", width=button_width, height=60, font=font_large, command=self.register)
        self.register_button.grid(row=10, column=1, pady=20)

        # Switch to home frame with Return button
        self.switch_login_button = ctk.CTkButton(self, text="Return", width=button_width, height=60, font=font_large, command=self.return_to_home)
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
            ctk.CTkLabel(self, text="Admin register successfully!", font=("Arial", 18)).grid(row=12, column=1, pady=10)

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
=======
>>>>>>> Stashed changes
