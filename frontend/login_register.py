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
from frontend.user_gui import UserGUI
from frontend.admin_gui import AdminGUI
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label 
from pathlib import Path
import zxcvbn
import re 
class LoginFrame(Frame):
    def __init__(self,parent):
        super().__init__(parent)
        self.controller = parent
        self.password_visible = False
        self.captcha_image, self.captcha_text = self.generate_captcha()

        # Tạo frame đăng nhập
        self.log_in_frame = Frame(self)
        self.log_in_frame.pack(fill="both", expand=True)

        self.canvas = Canvas(
            self.log_in_frame,
            bg = "#FFFFFF",
            height = 720,
            width = 1012,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.image_image_1 = PhotoImage(
            file="assets/login/image_1.png")
        self.image_1 = self.canvas.create_image(
            514.25,
            358.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            547.03125,
            16.171897888183594,
            anchor="nw",
            text="BLUE MOON APARTMENT",
            fill="#FFFFFF",
            font=("Inter Bold", 33 * -1)
        )

        self.canvas.create_text(
            494.296875,
            93.51563262939453,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.canvas.create_text(
            495.0,
            206.015625,
            anchor="nw",
            text="Password:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.canvas.create_text(
            494.296875,
            444.21875,
            anchor="nw",
            text="Captcha:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.image_image_2 = PhotoImage(
            file="assets/login/image_2.png")
        self.image_2 = self.canvas.create_image(
            227.25,
            363.0,
            image=self.image_image_2
        )

        self.username_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.username_entry.place(
            x=635.0,
            y=90.0,
            width=346.0,
            height=50.0
        )


        self.password_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            show="*",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.password_entry.place(
            x=635.0,
            y=200.0,
            width=346.0,
            height=50.0
        )

        self.image_image_3 = self.captcha_image
        self.image_3 = self.canvas.create_image(
            775.5,
            335.0,
            image=self.image_image_3
        )


        self.captcha_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.captcha_entry.place(
            x=635.0,
            y=434.0,
            width=346.0,
            height=50.0
        )

        self.eye_button = PhotoImage(
            file="assets/login/button_5.png")
        button_1 = Button(
            image=self.eye_button,
            borderwidth=0,
            highlightthickness=0,
            command=self.toggle_password,
            relief="flat"
        )
        button_1.place(
            x=905.0,
            y=205.0,
            width=70.0,
            height=40.0
        )

        self.button_image_2 = Image.open("assets/login/button_2.png")
        self.button_image_2 = self.button_image_2.resize((237, 75))
        self.button_image_2 = ImageTk.PhotoImage(self.button_image_2)
        button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )
        button_2.place(
            x=681.0,
            y=516.0,
            width=237.0,
            height=75.0
        )

        self.button_image_3 = Image.open("assets/login/button_3.png")
        self.button_image_3 = self.button_image_3.resize((187, 55))
        self.button_image_3 = ImageTk.PhotoImage(self.button_image_3)
        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.show_forget_frame,
            relief="flat"
        )
        button_3.place(
            x=565.0,
            y=627.0,
            width=187.0,
            height=55.0
        )

        self.button_image_4 = Image.open("assets/login/button_4.png")
        self.button_image_4 = self.button_image_4.resize((120, 55))
        self.button_image_4 = ImageTk.PhotoImage(self.button_image_4)
        button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.show_register_frame,
            relief="flat"
        )
        button_4.place(
            x=825.0,
            y=627.0,
            width=120.0,
            height=55.0
        )

        self.button_image_5 = Image.open("assets/login/button_1.png")
        self.button_image_5 = self.button_image_5.resize((83, 72))
        self.button_image_5 = ImageTk.PhotoImage(self.button_image_5)
        button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.refresh_captcha,
            relief="flat"
        )
        button_5.place(
            x=922.0,
            y=301.0,
            width=83.0,
            height=72.0
        )

    def toggle_password(self):
        """Toggle password visibility."""
        if self.password_visible:
            self.password_entry.configure(show="*")
        else:
            self.password_entry.configure(show="")
        self.password_visible = not self.password_visible
    
    def generate_captcha(self):
        folder='samples'
        image= random.choice([f for f in os.listdir(folder) if os.path.isfile(os.path.join(folder, f))])
        captcha_text=str(image[:5])
        image_path='samples/'+image
        captcha_image=Image.open(image_path)
        captcha_image = captcha_image.resize((280, 70))
        captcha_image = ImageTk.PhotoImage(captcha_image)
        return captcha_image, captcha_text

    def refresh_captcha(self):
        """Refresh the CAPTCHA image and text."""
        self.captcha_image, self.captcha_text = self.generate_captcha()
        #self.image_3.configure(image=self.captcha_image)
        self.canvas.create_image(
            775.5,
            335.0,
            image=self.captcha_image
        )

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
    
    def forget_password(self):
        self.controller.show_forget_frame(user)

class ForgetFrame(Frame):
    def __init__(self, parent, user_mode=True):
        super().__init__(parent)
        self.controller = parent
        self.password_visible = False
        self.is_user = user_mode

        self.forget_frame = Frame(self)
        self.forget_frame.pack(fill="both", expand=True)

        self.canvas = Canvas(
            self.forget_frame,
            bg = "#FFFFFF",
            height = 720,
            width = 1012,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file="assets/change/image_1.png")
        self.image_1 = self.canvas.create_image(
            514.25,
            358.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            547.03125,
            16.171897888183594,
            anchor="nw",
            text="BLUE MOON APARTMENT",
            fill="#FFFFFF",
            font=("Inter Bold", 33 * -1)
        )

        self.canvas.create_text(
            494.296875,
            93.51563262939453,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.canvas.create_text(
            494.296875,
            200,
            anchor="nw",
            text="Phone \nNumber:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.canvas.create_text(
            494.296875,
            306,
            anchor="nw",
            text="New \nPassword:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.canvas.create_text(
            494.296875,
            426,
            anchor="nw",
            text="Confirm New\nPassword:",
            fill="#FFFFFF",
            font=("Inter Bold", 23 * -1)
        )

        self.image_image_2 = PhotoImage(
            file="assets/change/image_2.png")
        self.image_2 = self.canvas.create_image(
            227.25,
            363.0,
            image=self.image_image_2
        )

        self.username_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.username_entry.place(
            x=635.0,
            y=90.0,
            width=346.0,
            height=50.0
        )

        self.phonenumber_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.phonenumber_entry.place(
            x=635.0,
            y=205.0,
            width=346.0,
            height=50.0
        )

        self.newpassword_entry = Entry(
            bd=0,
            show="*",
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.newpassword_entry.place(
            x=635.0,
            y=310.0,
            width=346.0,
            height=50.0
        )

        self.confirm_newpassword_entry = Entry(
            bd=0,
            show="*",  
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.confirm_newpassword_entry.place(
            x=635.0,
            y=422.0,
            width=346.0,
            height=50.0
        )


        self.button_image_1 = PhotoImage(
            file="assets/change/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.toggle_password,
            relief="flat"
        )
        self.button_1.place(
            x=900.0,
            y=315.0,
            width=70.0,
            height=40.0
        )

        self.button_image_2 = Image.open("assets/change/button_2.png")
        self.button_image_2 = self.button_image_2.resize((200, 40))
        self.button_image_2 = ImageTk.PhotoImage(self.button_image_2)
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.show_login_frame,
            relief="flat"
        )
        self.button_2.place(
            x=680.0,
            y=630.0,
            width=200.0,
            height=40.0
        )

        self.button_image_3 = Image.open("assets/change/button_3.png")
        self.button_image_3 = self.button_image_3.resize((220, 72))
        self.button_image_3 = ImageTk.PhotoImage(self.button_image_3)
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.change,
            relief="flat"
        )
        self.button_3.place(
            x=680.0,
            y=530.0,
            width=220.0,
            height=72.0
        )


    def toggle_password(self):
        """Toggle password visibility."""
        if self.password_visible:
            self.newpassword_entry.configure(show="*")
            self.confirm_newpassword_entry.configure(show="*")
        else:
            self.newpassword_entry.configure(show="")
            self.confirm_newpassword_entry.configure(show="")
        self.password_visible = not self.password_visible

    def check_password_strength(self, event=None):
        """Check the password strength and update the label."""
        password = self.newpassword_entry.get()
        result = zxcvbn.zxcvbn(password)

        strength_score = result['score']
        feedback = result['feedback']['suggestions']

        # Convert strength score to a user-friendly message
        strength_text = {0: "Very Weak", 1: "Weak", 2: "Medium", 3: "Strong", 4: "Very Strong"}
        strength_color = {0: "red", 1: "red", 2: "orange", 3: "green", 4: "green"}

        self.password_strength_label.configure(text=f"Strength: {strength_text[strength_score]}", text_color=strength_color[strength_score])

    def change(self):
        """Perform register action."""
        # Get input values
        username = self.username_entry.get()
        phone_number = self.phonenumber_entry.get()
        newpassword = self.newpassword_entry.get()
        confirm_newpassword = self.confirm_newpassword_entry.get()

        # Clear previous warnings
        # self.clear_warnings()

        # Input validation
        valid = True
        if not username:
            self.username_label.configure(text="Username is required")
            valid = False
        if not newpassword:
            self.newpassword_label.configure(text="Password is required")
            valid = False
        elif newpassword != confirm_newpassword:
            self.confirm_newpassword_label.configure(text="Passwords do not match")
            valid = False
        if not phone_number:
            self.phonenumber_label.configure(text="Phone number is required")
            valid = False
        if not valid:
            return

        # Attempt to register the user
        try:
            self.controller.auth_manager.change_password(username, phone_number, newpassword)
            messagebox.showinfo("Change Password Success", "Password changed successfully")
        except Exception as e:
            messagebox.showerror("Change Password Error", str(e))

    def clear_warnings(self):
        """Clear all warning labels."""
        self.username_label.configure(text="")
        self.newpassword_label.configure(text="")
        self.confirm_newpassword_label.configure(text="")
        self.phonenumber_label.configure(text="")


class RegisterFrame(Frame):
    def __init__(self, parent, user_mode=True):
        super().__init__(parent)
        self.controller = parent
        self.password_visible = False
        self.is_user = user_mode

        self.register_frame = Frame(self)
        self.register_frame.pack(fill="both", expand=True)

        self.canvas = Canvas(
            self.register_frame,
            bg = "#FFFFFF",
            height = 720,
            width = 1012,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file="assets/signup/image_1.png")
        self.image_1 = self.canvas.create_image(
            514.25,
            358.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            547.03125,
            16.171897888183594,
            anchor="nw",
            text="BLUE MOON APARTMENT",
            fill="#FFFFFF",
            font=("Inter Bold", 33 * -1)
        )

        self.canvas.create_text(
            494.296875,
            93.51563262939453,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.canvas.create_text(
            494.296875,
            171.5625,
            anchor="nw",
            text="Password:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.canvas.create_text(
            494.296875,
            245.390625,
            anchor="nw",
            text="Confirm\nPassword:",
            fill="#FFFFFF",
            font=("Inter Bold", 22 * -1)
        )
    
        self.canvas.create_text(
            494.296875,
            341.71875,
            anchor="nw",
            text="Full Name:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.canvas.create_text(
            494.296875,
            423.984375,
            anchor="nw",
            text="Phone Number:",
            fill="#FFFFFF",
            font=("Inter Bold", 23 * -1)
        )

        self.canvas.create_text(
            494.296875,
            499.21875,
            anchor="nw",
            text="Appartment ID:",
            fill="#FFFFFF",
            font=("Inter Bold", 25 * -1)
        )

        self.image_image_2 = PhotoImage(
            file="assets/signup/image_2.png")
        self.image_2 = self.canvas.create_image(
            227.25,
            363.0,
            image=self.image_image_2
        )

        self.username_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.username_entry.place(
            x=667.96875,
            y=85.07814025878906,
            width=313.59375,
            height=48.624996185302734
        )

        self.password_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            show='*',
            highlightthickness=0
        )
        self.password_entry.place(
            x=667.96875,
            y=165.93751525878906,
            width=313.59375,
            height=48.624996185302734
        )

        self.confirm_password_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            show='*',
            highlightthickness=0
        )
        self.confirm_password_entry.place(
            x=667.96875,
            y=245.390625,
            width=313.59375,
            height=48.624996185302734
        )

        self.fullname_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.fullname_entry.place(
            x=667.96875,
            y=326.25,
            width=313.59375,
            height=48.624996185302734
        )

        self.phonenumber_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.phonenumber_entry.place(
            x=667.96875,
            y=407.109375,
            width=313.59375,
            height=48.624996185302734
        )

        self.apartment_code_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.apartment_code_entry.place(
            x=667.96875,
            y=486.5625,
            width=313.59375,
            height=48.624996185302734
        )

        self.button_image_1 = PhotoImage(
            file="assets/signup/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.toggle_password,
            relief="flat"
        )
        self.button_1.place(
            x=909.140625,
            y=170.859375,
            width=63.984375,
            height=40.078125
        )

        self.button_image_2 = PhotoImage(
            file="assets/signup/button_2.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.register,
            relief="flat"
        )
        self.button_2.place(
            x=648.28125,
            y=566.015625,
            width=204.609375,
            height=68.20311737060547
        )

        self.button_image_3 = PhotoImage(
            file="assets/signup/button_3.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.show_login_frame,
            relief="flat"
        )
        self.button_3.place(
            x=639.84375,
            y=646.171875,
            width=221.484375,
            height=46.40625
        )


    def toggle_password(self):
        """Toggle password visibility."""
        if self.password_visible:
            self.password_entry.configure(show="*")
            self.confirm_password_entry.configure(show="*")
        else:
            self.password_entry.configure(show="")
            self.confirm_password_entry.configure(show="")
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
        phone_number = self.phonenumber_entry.get()
        apartment_code = self.apartment_code_entry.get()





        try:
            if self.is_user:
                self.controller.auth_manager.register_user(username, password, full_name, phone_number, apartment_code, confirm_password)
            else:
                self.controller.auth_manager.register_user(username, password, full_name, phone_number,  apartment_code, confirm_password, account_type='admin')
            messagebox.showinfo("Register Success", "User registered successfully")
        except Exception as e:
            messagebox.showerror("Register Error", str(e))

    def clear_warnings(self):
        """Clear all warning labels."""
        self.username_label.configure(text="")
        self.password_label.configure(text="")
        self.confirm_password_label.configure(text="")
        self.fullname_label.configure(text="")
        self.apartment_code_label.configure(text="")

class LoginRegisterApp(Tk):
    def __init__(self):
        super().__init__()

        self.auth_manager = AuthManager()

        self.title("Blue Moon Apartment")
        self.geometry("1012x720")  # Default size before full screen

        self.resizable(False, False)

        # Create containers for frames
        self.login_frame = None
        self.register_frame = None
        self.main_frame = None
        self.forget_frame = None
        self.root_gui = None  # Store RootGUI instance
        

        self.show_login_frame()

    def show_login_frame(self):
        """Show login frame and hide other frames."""
        if self.register_frame:
            self.register_frame.destroy()
        if self.forget_frame:
            self.forget_frame.destroy()
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
    
    def show_forget_frame(self):
        """Show forget frame and hide other frames."""
        if self.login_frame:
            self.login_frame.destroy()

        self.forget_frame = ForgetFrame(self)
        self.forget_frame.pack(fill="both", expand=True)

    def show_main_frame(self, user):
        """Show the main frame based on account type after login."""
        if self.login_frame:
            self.login_frame.destroy()
        if user['account_type'] == 'admin':
            self.admin_gui = AdminGUI(self, user)
        elif user['account_type'] == 'user':
            self.user_gui = UserGUI(self, user)  # Create an instance of UserGUI
        else:
            self.root_gui = RootGUI(self, user)  # Create an instance of RootGUI

    def show_home(self):
        """Show the home screen of RootGUI."""
        if self.root_gui:
            self.root_gui.show_home()  # Call the show_home method of RootGUI
