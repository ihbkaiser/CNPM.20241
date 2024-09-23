# frontend/normal_gui.py

import customtkinter as ctk

class NormalGUI(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.controller = parent
        self.user = user

        # Normal User's GUI Layout
        ctk.CTkLabel(self, text=f"Welcome,{self.user['full_name']} ").pack(pady=10)
        ctk.CTkLabel(self, text=f"Mã căn hộ: {self.user['apartment_code']}").pack(pady=5)
        ctk.CTkButton(self, text="View Profile", command=self.view_profile).pack(pady=5)
        ctk.CTkButton(self, text="View Fees", command=self.view_fees).pack(pady=5)
        ctk.CTkButton(self, text="Logout", command=self.logout).pack(pady=5)

    def view_profile(self):
        # Functionality for viewing profile
        print("Viewing Profile...")

    def view_fees(self):
        # Functionality for viewing fees
        print("Viewing Fees...")

    def logout(self):
        # Logout and go back to login screen
        self.controller.show_login_frame()
