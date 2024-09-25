import random
import string
import os
import customtkinter as ctk
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageTk
from tkinter import messagebox
import io
from backend.auth import AuthManager
from frontend.root_gui import RootGUI
from frontend.normal_gui import NormalGUI
from frontend.admin_gui import AdminGUI
import zxcvbn
class LoginFrame(ctk.CTkFrame):
    def __init__(self, parent):
        super().__init__(parent)
        self.controller = parent
        self.password_visible = False
        self.header_label = ctk.CTkLabel(self, text="Phần mềm quản lý chung cư BlueMoon", font=("Arial", 26, "bold"))
        self.header_label.grid(row=0, column=0, columnspan=3, pady=20)

        # Custom fonts and sizes
        font_large = ("Arial", 20)
        button_width = 200
        entry_width = 400
        entry_height = 50

        # Setup grid configuration for centering elements
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_columnconfigure(2, weight=1)

        # Username entry
        self.username_label = ctk.CTkLabel(self, text="Username:", font=font_large)
        self.username_label.grid(row=1, column=1, sticky="w", pady=10)
        self.username_entry = ctk.CTkEntry(self, placeholder_text="Username", width=entry_width, height=entry_height, font=font_large)
        self.username_entry.grid(row=1, column=1, pady=20, padx=20)

        # Password entry with eye icon
        self.password_label = ctk.CTkLabel(self, text="Password:", font=font_large)
        self.password_label.grid(row=2, column=1, sticky="w", pady=10)
        self.password_entry = ctk.CTkEntry(self, placeholder_text="Password", show="*", width=entry_width, height=entry_height, font=font_large)
        self.password_entry.grid(row=2, column=1, pady=20, padx=20)

        # Button to toggle password visibility
        self.eye_button = ctk.CTkButton(self, text="👁", width=50, height=50, font=font_large, command=self.toggle_password)
        self.eye_button.grid(row=2, column=2, padx=10, pady=0)

        # Image CAPTCHA
        self.captcha_image, self.captcha_text = self.generate_captcha()

        # Display the CAPTCHA image
        self.captcha_image_label = ctk.CTkLabel(self, image=self.captcha_image, text="")
        self.captcha_image_label.grid(row=3, column=1, pady=10)
        
        self.refresh_image = ImageTk.PhotoImage(Image.open("assets/refresh_button.png").resize((50, 50)))
        self.refresh_captcha_button = ctk.CTkButton(self, image=self.refresh_image, text="", width=20, height=50, font=font_large, command=self.refresh_captcha)
        self.refresh_captcha_button.grid(row=3, column=2, padx=10, pady=0)

        # CAPTCHA entry
        self.captcha_entry = ctk.CTkEntry(self, placeholder_text="Enter CAPTCHA", width=entry_width, height=entry_height, font=font_large)
        self.captcha_entry.grid(row=5, column=1, pady=20, padx=20)
        self.captcha_error_label = ctk.CTkLabel(self, text="", text_color="red")
        self.captcha_error_label.grid(row=6, column=1)

        # Login button
        self.login_button = ctk.CTkButton(self, text="Login", width=button_width, height=60, font=font_large, command=self.login)
        self.login_button.grid(row=7, column=1, pady=20, padx=20)

        # Switch to register frame button
        self.switch_register_button = ctk.CTkButton(self, text="Sign Up ", width=button_width, height=60, font=font_large, command=self.controller.show_register_frame)
        self.switch_register_button.grid(row=8, column=1, pady=20)

    def toggle_password(self):
        """Toggle password visibility."""
        if self.password_visible:
            self.password_entry.configure(show="*")
            self.eye_button.configure(text="👁")
        else:
            self.password_entry.configure(show="")
            self.eye_button.configure(text="🚫")
        self.password_visible = not self.password_visible
    
    def generate_captcha(self):
        folder='samples'
        image= random.choice([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
        captcha_text=str(image[:5])
        image_path='samples/'+image
        captcha_image=Image.open(image_path)
        captcha_image = captcha_image.resize((400, 100))
        captcha_image = ImageTk.PhotoImage(captcha_image)
        return captcha_image, captcha_text

    def refresh_captcha(self):
        """Refresh the CAPTCHA image and text."""
        self.captcha_image, self.captcha_text = self.generate_captcha()
        self.captcha_image_label.configure(image=self.captcha_image)

    def login(self):
        """Perform login action with CAPTCHA validation."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        captcha_input = self.captcha_entry.get()

        # Validate CAPTCHA
        if not captcha_input:
            self.captcha_error_label.configure(text="CAPTCHA is required")
            return
        elif captcha_input != self.captcha_text:
            self.captcha_error_label.configure(text="Incorrect CAPTCHA")
            return

        # Simulate login process
        try:
            user = self.controller.auth_manager.login(username, password)
            self.controller.show_main_frame(user)
        except Exception as e:
            messagebox.showerror("Login Error", str(e))
class RegisterFrame(ctk.CTkFrame):
    def __init__(self, parent, user_mode=True):
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
        ctk.CTkLabel(self, text="Full Name:", font=font_large).grid(row=6, column=0, padx=20, pady=10, sticky="w")
        self.fullname_entry = ctk.CTkEntry(self, placeholder_text="Full Name", width=entry_width, height=entry_height, font=font_large)
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
        self.register_button = ctk.CTkButton(self, text="Sign Up", width=button_width, height=60, font=font_large, command=self.register)
        self.register_button.grid(row=10, column=1, pady=20)

        # Switch to login frame
        self.switch_login_button = ctk.CTkButton(self, text="Back to log in", width=button_width, height=60, font=font_large, command=self.controller.show_login_frame)
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
                self.controller.auth_manager.register_user(username, password, full_name, apartment_code)
            else:
                self.controller.auth_manager.register_user(username, password, full_name,  apartment_code, account_type='admin')
<<<<<<< Updated upstream
            ctk.CTkLabel(self, text="Register success", font=("Arial", 18)).grid(row=12, column=1, pady=10)
=======
            messagebox.showinfo("Register Success", "User registered successfully")
>>>>>>> Stashed changes
        except Exception as e:
            messagebox.showerror("Register Error", str(e))

    def clear_warnings(self):
        """Clear all warning labels."""
        self.username_label.configure(text="")
        self.password_label.configure(text="")
        self.confirm_password_label.configure(text="")
        self.fullname_label.configure(text="")
        self.apartment_code_label.configure(text="")
class LoginRegisterApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.auth_manager = AuthManager()

        self.title("Login and Register")
        self.geometry("1200x1000")  # Default size before full screen

        # Create containers for frames
        self.login_frame = None
        self.register_frame = None
        self.main_frame = None
        self.root_gui = None  # Store RootGUI instance
        

        self.show_login_frame()

    def show_login_frame(self):
        """Show login frame and hide other frames."""
        if self.register_frame:
            self.register_frame.destroy()
        if self.main_frame:
            self.main_frame.destroy()

        self.login_frame = LoginFrame(self)
        self.login_frame.pack(fill="both", expand=True)

    def show_register_frame(self):
        """Show register frame and hide other frames."""
        if self.login_frame:
            self.login_frame.destroy()

        self.register_frame = RegisterFrame(self)
        self.register_frame.pack(fill="both", expand=True)

    def show_main_frame(self, user):
        """Show the main frame based on account type after login."""
        if self.login_frame:
            self.login_frame.destroy()
        if user['account_type'] == 'admin':
            self.admin_gui = AdminGUI(self, user)  # Create an instance of AdminGUI
            self.admin_gui.pack(fill="both", expand=True)
        elif user['account_type'] == 'user':
            self.user_gui = NormalGUI(self, user)  # Create an instance of UserGUI
            self.user_gui.pack(fill="both", expand=True)
        else:
            self.root_gui = RootGUI(self, user)  # Create an instance of RootGUI
            self.root_gui.pack(fill="both", expand=True)

    def show_home(self):
        """Show the home screen of RootGUI."""
        if self.root_gui:
            self.root_gui.show_home()  # Call the show_home method of RootGUI
