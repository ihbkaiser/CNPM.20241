# frontend/normal_gui.py

import customtkinter as ctk

class NormalGUI(ctk.CTkFrame):
    def __init__(self, parent, user):
        super().__init__(parent)
        self.controller = parent
        self.user = user

        # Normal User's GUI Layout
        ctk.CTkLabel(self, text=f"Welcome,{self.user['full_name']} ").pack(pady=10)
        ctk.CTkLabel(self, text=f"Appartment ID: {self.user['apartment_code']}").pack(pady=5)
        ctk.CTkButton(self, text="View Profile", command=self.view_profile).pack(pady=5)
        ctk.CTkButton(self, text="View Fees", command=self.view_fees).pack(pady=5)
        ctk.CTkButton(self, text="Logout", command=self.logout).pack(pady=5)
        ctk.CTkButton(self, text = "Change Password", command = self.show_change_password).pack(pady=5)
        
    def view_profile(self):
        # Functionality for viewing profile
        print("Viewing Profile...")

    def view_fees(self):
        # Functionality for viewing fees
        print("Viewing Fees...")
    
    def show_change_password(self):
        # Change password functionality
        print("Changing Password...")

    def logout(self):
        # Logout and go back to login screen
        self.destroy()
        self.controller.show_login_frame()
