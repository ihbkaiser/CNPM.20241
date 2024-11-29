import customtkinter as ctk
from tkinter import ttk
from backend.auth import AuthManager
from frontend.root_gui import RootGUI  # Import RootGUI to extend it

class AdminGUI(RootGUI):
    def __init__(self, parent, user):
        # Initialize the parent class (RootGUI)
        super().__init__(parent, user)

    def show_home(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        ctk.CTkLabel(self, text=f"Welcome, {self.user['full_name']}").pack(pady=10)
        ctk.CTkButton(self, text="View Admins", command=self.view_admins, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self, text="View Users", command=self.view_users, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self, text="Manage Fees", command=self.manage_fees, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self, text="Edit Fees", command=self.edit_fees, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self, text="Payment", command=self.thu_fee_frame_gui, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self, text="Statistics", command=self.show_statistics_options, width=200, height=50).pack(pady=5)  # Nút thống kê khoản thu
        ctk.CTkButton(self, text="Logout", command=self.logout, width=200, height=50).pack(pady=5)

    def show_statistics_options(self):
        """Hiển thị các tùy chọn thống kê."""


        for widget in self.winfo_children():
            widget.pack_forget()
        self.statistic_frame = ctk.CTkFrame(self)
        self.statistic_frame.pack(fill='both', expand=True)
        ctk.CTkLabel(self.statistic_frame, text="Statistic", font=("Arial", 24)).pack(pady=10)

        ctk.CTkLabel(self.statistic_frame, text="Choose a statistics option:").pack(pady=10)

        ctk.CTkButton(self.statistic_frame, text="Electricity Fee", command=self.show_electricity_fee_summary, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self.statistic_frame, text="Water Fee", command=self.show_water_fee_summary, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self.statistic_frame, text="Service Fee", command=self.show_service_fee_summary, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self.statistic_frame, text="Parking Fee", command=self.show_parking_fee_summary, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self.statistic_frame, text="By Household", command=self.show_household_statistics, width=200, height=50).pack(pady=5)
        ctk.CTkButton(self.statistic_frame, text="Close", command=self.show_home, width=200, height=50).pack(pady=5)


    def show_household_statistics(self):
        """Hiển thị form nhập mã căn hộ để xem thống kê."""
        popup = ctk.CTkToplevel(self)
        popup.title("Household Statistics")
        popup.geometry("400x200")

        ctk.CTkLabel(popup, text="Enter Apartment Code:").pack(pady=10)
        apartment_code_entry = ctk.CTkEntry(popup)
        apartment_code_entry.pack(pady=10)

        def fetch_statistics():
            apartment_code = apartment_code_entry.get()
            print(apartment_code)
            if apartment_code:
                self.show_household_fee_summary(apartment_code)
                popup.destroy()
            else:
                self.show_popup("Error", "Apartment Code cannot be empty!")

        ctk.CTkButton(popup, text="Submit", command=fetch_statistics, width=200, height=50).pack(pady=10)
        ctk.CTkButton(popup, text="Close", command=popup.destroy, width=200, height=50).pack(pady=10)

    def show_household_fee_summary(self, apartment_code):
        """Hiển thị thống kê tổng hợp các loại phí cho một hộ gia đình."""
        summary = self.db_manager.get_userfee_by_apartment_code(apartment_code)  # Lấy thống kê tổng hợp từ db
        if summary:
            self.show_summary_table(f"Household Fee Summary for {apartment_code}", summary, ["fee_name", "paid", "remain"])
        else:
            self.show_popup("Error", f"No Fee Summary found for Apartment Code: {apartment_code}")


    def show_summary_table(self, title, data, columns):
        """Hiển thị bảng thống kê tổng hợp các loại phí."""
        popup = ctk.CTkToplevel(self)  # Tạo cửa sổ popup
        popup.title(title)
        popup.geometry("1000x600")  # Set larger size for the popup window

        # Tạo Treeview với các cột
        tree = ttk.Treeview(popup, columns=columns, show="headings", height=25)  # Set larger height for the Treeview

        # Đặt tiêu đề cho các cột và tăng kích thước cột
        column_widths = {col: 150 for col in columns}

        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=column_widths[col])

        # Chèn dữ liệu vào bảng
        for item in data:
            values = []
            for col in columns:
                value = item.get(col, 'N/A')
                values.append(value)
            tree.insert("", "end", values=tuple(values))

        tree.pack(pady=10, padx=10, expand=True, fill='both')

        # Thêm nút đóng
        ctk.CTkButton(popup, text="Close", command=popup.destroy).pack(pady=10)


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
        for widget in self.winfo_children():
            widget.pack_forget()
        """Hiển thị danh sách người dùng trong một bảng (popup)."""
        self.table_frame = ctk.CTkFrame(self)
        self.table_frame.pack(fill='both', expand=True)
        ctk.CTkLabel(self.table_frame, text=title, font=("Arial", 24)).pack(pady=10)
        # Tạo Treeview với các cột
        columns = ("Username", "Account Type", "Full Name", "Phone Number", "Apartment Code", "Email")
        tree = ttk.Treeview(self.table_frame, columns=columns, show="headings", height=25)  # Set larger height for the Treeview

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
        ctk.CTkButton(self.table_frame, text="Close", command=self.return_to_home).pack(pady=10)
    
    
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
        ctk.CTkButton(self.table_frame, text="Close", command=self.return_to_home).pack(pady=10)


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
    def thu_fee(self, apartment_code, fee_name, pay_money):
        self.db_manager.thu_fee(apartment_code, fee_name, pay_money)
    def thu_fee_frame_gui(self):
        for widget in self.winfo_children():
            widget.pack_forget()
        if hasattr(self, 'user_info_frame'):
            self.user_info_frame.destroy()
        self.thu_fee_frame = ctk.CTkFrame(self, width=450, height=350, corner_radius=15)
        self.thu_fee_frame.pack(padx=20, pady=20, fill="both", expand=True)
        header_font = ("Arial", 18, "bold")
        ctk.CTkLabel(self.thu_fee_frame, text="Fee Payment", font=header_font).grid(row=0, column=0, columnspan=2, pady=(20, 10))
        font_large = ("Arial", 14)
        ctk.CTkLabel(self.thu_fee_frame, text="Apartment Code:", font=font_large).grid(row=1, column=0, padx=(30, 10), pady=10, sticky="e")
        self.apartment_code_var = ctk.StringVar()
        self.apartment_code_entry = ctk.CTkEntry(self.thu_fee_frame, textvariable=self.apartment_code_var, width=220, font=font_large)
        self.apartment_code_entry.grid(row=1, column=1, padx=(10, 30), pady=10)
        ctk.CTkLabel(self.thu_fee_frame, text="Fee Name:", font=font_large).grid(row=2, column=0, padx=(30, 10), pady=10, sticky="e")
        self.fee_name_var = ctk.StringVar()
        fee_types = self.db_manager.get_fee_names()
        self.fee_type_dropdown = ctk.CTkOptionMenu(self.thu_fee_frame, variable=self.fee_name_var, values=fee_types, width=220)
        self.fee_type_dropdown.grid(row=2, column=1, padx=(10, 30), pady=10)
        submit_button = ctk.CTkButton(self.thu_fee_frame, text="Submit", command=self.display_user_info, width=120)
        submit_button.grid(row=3, column=0, columnspan=2, pady=(20, 20))
        back_button = ctk.CTkButton(self.thu_fee_frame, text="Back", command=self.show_home, width=120)
        back_button.grid(row=4, column=0, columnspan=2, pady=(0, 10))




    def display_user_info(self):
        if hasattr(self, 'user_info_frame'):
            self.user_info_frame.destroy()
        user_fee_info = self.db_manager.user_fee_info(self.apartment_code_var.get(), self.fee_name_var.get())
        try:
            username = user_fee_info['username']
        except:
            self.show_popup("Error", "No user found!")
            return
        fullname = user_fee_info['fullname']
        apt_code = user_fee_info['apt_code']
        feename = user_fee_info['feename']
        money_paid = user_fee_info['money_paid']
        money_remain = user_fee_info['money_remain']
        money_residual = user_fee_info['money_residual']
        status = user_fee_info['status']
        self.user_info_frame = ctk.CTkFrame(self, width=450, height=350, corner_radius=15)
        self.user_info_frame.pack(padx=20, pady=20, fill="both", expand=True)
        font_large = ("Arial", 14)
        ctk.CTkLabel(self.user_info_frame, text=f"Username: {username}", font=font_large).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.user_info_frame, text=f"Full Name: {fullname}", font=font_large).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.user_info_frame, text=f"Apt Code: {apt_code}", font=font_large).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.user_info_frame, text=f"Fee Name: {feename}", font=font_large).pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.user_info_frame, text=f"Money Paid: {money_paid}", font=font_large).pack(anchor="w", padx=10, pady=5)
        if status == 'Complete':
            ctk.CTkLabel(self.user_info_frame, text=f"Money Remain: {money_remain}", font=font_large, text_color="green").pack(anchor="w", padx=10, pady=5)
        else:
            ctk.CTkLabel(self.user_info_frame, text=f"Money Remain: {money_remain}", font=font_large, text_color="red").pack(anchor="w", padx=10, pady=5)
        ctk.CTkLabel(self.user_info_frame, text=f"Money Residual: {money_residual}", font=font_large).pack(anchor="w", padx=10, pady=5)
        payment_button = ctk.CTkButton(self.user_info_frame, text="Proceed to Payment", command=self.thu_fee_dialog)
        payment_button.pack(pady=(20, 10))

    def thu_fee_dialog(self):
        dialog = ctk.CTkToplevel(self)
        dialog.title("Payment")
        font_large = ("Arial", 16)
        ctk.CTkLabel(dialog, text="Amount:", font=font_large).grid(row=0, column=0, padx=10, pady=5, sticky="e")
        self.pay_money_var = ctk.StringVar()
        ctk.CTkEntry(dialog, textvariable=self.pay_money_var, width=200, font=font_large).grid(row=0, column=1, padx=10, pady=5)
        def pay_and_update():
            self.thu_fee(self.apartment_code_var.get(), self.fee_name_var.get(), int(self.pay_money_var.get()))
            self.display_user_info()
        ctk.CTkButton(dialog, text="Pay", command=pay_and_update, width=100).grid(row=1, column=0, pady=10)
        ctk.CTkButton(dialog, text="Cancel", command=dialog.destroy, width=100).grid(row=1, column=1, pady=10)





    def logout(self):
        """Đăng xuất và quay lại màn hình đăng nhập."""
        self.destroy()
        self.controller.show_login_frame()


    
    def show_electricity_fee_summary(self):
        """Hiển thị thống kê tổng hợp tiền điện."""
        summary = self.db_manager.get_electricity_fee_summary()  # Lấy thống kê tổng hợp từ db
        if summary:
            self.show_summary_table("Electricity Fee Summary", summary, ["Month_Year", "Total Electricity Paid", "Remaining Electricity Fee"])
        else:
            self.show_popup("Error", "No Electricity Fee Summary found!")

    def show_water_fee_summary(self):
        """Hiển thị thống kê tổng hợp tiền nước."""
        summary = self.db_manager.get_water_fee_summary()  # Lấy thống kê tổng hợp từ db
        if summary:
            self.show_summary_table("Water Fee Summary", summary, ["Month_Year", "Total Water Paid", "Remaining Water Fee"])
        else:
            self.show_popup("Error", "No Water Fee Summary found!")

    def show_service_fee_summary(self):
        """Hiển thị thống kê tổng hợp tiền dịch vụ."""
        summary = self.db_manager.get_service_fee_summary()  # Lấy thống kê tổng hợp từ db
        if summary:
            self.show_summary_table("Service Fee Summary", summary, ["Month_Year", "Total Service Paid", "Remaining Service Fee"])
        else:
            self.show_popup("Error", "No Service Fee Summary found!")

    def show_parking_fee_summary(self):
        """Hiển thị thống kê tổng hợp tiền gửi xe."""
        summary = self.db_manager.get_parking_fee_summary()  # Lấy thống kê tổng hợp từ db
        if summary:
            self.show_summary_table("Parking Fee Summary", summary, ["Month_Year", "Total Parking Paid", "Remaining Parking Fee"])
        else:
            self.show_popup("Error", "No Parking Fee Summary found!")

    def return_to_home(self):
        self.table_frame.destroy()
        self.show_home()