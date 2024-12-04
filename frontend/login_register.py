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
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame
from pathlib import Path
import zxcvbn
class LoginFrame(Frame):
    def __init__(self,parent):
        super().__init__(parent)  # Gọi constructor của Tk()
        self.controller = parent
        self.password_visible = False
        self.captcha_image, self.captcha_text = self.generate_captcha()

        # Tạo frame đăng nhập
        self.log_in_frame = Frame(self)
        self.log_in_frame.pack(fill="both", expand=True)

        self.canvas = Canvas(
            self.log_in_frame,
            bg = "#FFFFFF",
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)

        self.image_image_1 = PhotoImage(
            file="assets/frame0/image_1.png")
        self.image_1 = self.canvas.create_image(
            721.0,
            519.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            382.0,
            582.0,
            anchor="nw",
            text="text",
            fill="#ECD8D2",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            778.0,
            23.0,
            anchor="nw",
            text="BLUE MOON APARTMENT",
            fill="#FFFFFF",
            font=("Inter Bold", 48 * -1)
        )

        self.canvas.create_text(
            703.0,
            133.0,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Inter Bold", 36 * -1)
        )

        self.canvas.create_text(
            704.0,
            293.0,
            anchor="nw",
            text="Password:",
            fill="#FFFFFF",
            font=("Inter Bold", 36 * -1)
        )

        self.canvas.create_text(
            703.0,
            646.0,
            anchor="nw",
            text="Captcha:",
            fill="#FFFFFF",
            font=("Inter Bold", 36 * -1)
        )

        self.image_image_2 = PhotoImage(
            file="assets/frame0/image_2.png")
        self.image_2 = self.canvas.create_image(
            343.0,
            516.5,
            image=self.image_image_2
        )

        entry_image_1 = PhotoImage(
            file="assets/frame0/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            1173.0,
            157.0,
            image=entry_image_1
        )
        self.username_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.username_entry.place(
            x=950.0,
            y=121.0,
            width=446.0,
            height=70.0
        )

        entry_image_2 = PhotoImage(
            file="assets/frame0/entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            1173.0,
            319.0,
            image=entry_image_2
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
            x=950.0,
            y=283.0,
            width=446.0,
            height=70.0
        )

        self.image_image_3 = self.captcha_image,
        self.image_3 = self.canvas.create_image(
            1119.5,
            489.0,
            image=self.image_image_3
        )

        self.entry_image_3 = PhotoImage(
            file="assets/frame0/entry_3.png")
        self.entry_bg_3 = self.canvas.create_image(
            1169.0,
            660.0,
            image=self.entry_image_3
        )
        self.captcha_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.captcha_entry.place(
            x=946.0,
            y=624.0,
            width=446.0,
            height=70.0
        )

        self.eye_button = PhotoImage(
            file="assets/frame0/button_1.png")
        button_1 = Button(
            image=self.eye_button,
            borderwidth=0,
            highlightthickness=0,
            command=self.toggle_password,
            relief="flat"
        )
        button_1.place(
            x=1301.0,
            y=293.0,
            width=91.0,
            height=57.0
        )

        self.button_image_2 = PhotoImage(
            file="assets/frame0/button_2.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.login,
            relief="flat"
        )
        self.button_2.place(
            x=981.0,
            y=766.0,
            width=287.0,
            height=95.0
        )

        self.button_image_3 = PhotoImage(
            file="assets/frame0/button_3.png")
        button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.show_forget_frame,
            relief="flat"
        )
        button_3.place(
            x=785.0,
            y=907.0,
            width=293.0,
            height=51.0
        )

        self.button_image_4 = PhotoImage(
            file="assets/frame0/button_4.png")
        button_4 = Button(
            image=self.button_image_4,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.show_register_frame,
            relief="flat"
        )
        button_4.place(
            x=1187.0,
            y=903.0,
            width=160.0,
            height=60.0
        )

        self.button_image_5 = PhotoImage(
            file="assets/frame0/button_5.png")
        button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            command=self.refresh_captcha,
            relief="flat"
        )
        button_5.place(
            x=1322.0,
            y=451.0,
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
        captcha_image = captcha_image.resize((400, 100))
        captcha_image = ImageTk.PhotoImage(captcha_image)
        return captcha_image, captcha_text

    def refresh_captcha(self):
        """Refresh the CAPTCHA image and text."""
        self.captcha_image, self.captcha_text = self.generate_captcha()
        #self.image_3.configure(image=self.captcha_image)
        self.canvas.create_image(
            1119.5,
            489.0,
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
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.image_image_1 = PhotoImage(
            file="assets/frame2/image_1.png")
        self.image_1 = self.canvas.create_image(
            721.0,
            519.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            382.0,
            582.0,
            anchor="nw",
            text="text",
            fill="#ECD8D2",
            font=("Inter Bold", 12 * -1)
        )

        self.canvas.create_text(
            778.0,
            23.0,
            anchor="nw",
            text="BLUE MOON APARTMENT",
            fill="#FFFFFF",
            font=("Inter Bold", 48 * -1)
        )

        self.canvas.create_text(
            703.0,
            133.0,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Inter Bold", 36 * -1)
        )

        self.canvas.create_text(
            703.0,
            458.0,
            anchor="nw",
            text="New Password:",
            fill="#FFFFFF",
            font=("Inter Bold", 32 * -1)
        )

        self.image_image_2 = PhotoImage(
            file="assets/frame2/image_2.png")
        self.image_2 = self.canvas.create_image(
            343.0,
            512.0,
            image=self.image_image_2
        )

        self.entry_image_1 = PhotoImage(
            file="assets/frame2/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            1173.0,
            157.0,
            image=self.entry_image_1
        )
        self.username_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.username_entry.place(
            x=950.0,
            y=121.0,
            width=446.0,
            height=70.0
        )

        self.entry_image_2 = PhotoImage(
            file="assets/frame2/entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            1173.0,
            315.0,
            image=self.entry_image_2
        )
        self.phonenumber_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.phonenumber_entry.place(
            x=950.0,
            y=279.0,
            width=446.0,
            height=70.0
        )

        self.entry_image_3 = PhotoImage(
            file="assets/frame2/entry_3.png")
        self.entry_bg_3 = self.canvas.create_image(
            1173.0,
            481.0,
            image=self.entry_image_3
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
            x=950.0,
            y=445.0,
            width=446.0,
            height=70.0
        )

        self.entry_image_4 = PhotoImage(
            file="assets/frame2/entry_4.png")
        self.entry_bg_4 = self.canvas.create_image(
            1173.0,
            651.0,
            image=self.entry_image_4
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
            x=950.0,
            y=615.0,
            width=446.0,
            height=70.0
        )


        self.button_image_1 = PhotoImage(
            file="assets/frame2/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.toggle_password,
            relief="flat"
        )
        self.button_1.place(
            x=1301.0,
            y=452.0,
            width=91.0,
            height=57.0
        )

        self.canvas.create_text(
            703.0,
            643.0,
            anchor="nw",
            text="Confirm New Password:",
            fill="#FFFFFF",
            font=("Inter Bold", 22 * -1)
        )

        self.canvas.create_text(
            703.0,
            294.0,
            anchor="nw",
            text="Phone Number:",
            fill="#FFFFFF",
            font=("Inter Bold", 32 * -1)
        )

        self.button_image_2 = PhotoImage(
            file="assets/frame2/button_2.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.show_login_frame,
            relief="flat"
        )
        self.button_2.place(
            x=910.0,
            y=884.0,
            width=315.0,
            height=66.0
        )

        self.button_image_3 = PhotoImage(
            file="assets/frame2/button_3.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.change,
            relief="flat"
        )
        self.button_3.place(
            x=870.0,
            y=761.0,
            width=396.0,
            height=84.0
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
            height = 1024,
            width = 1440,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )

        self.canvas.place(x = 0, y = 0)
        self.image_image_1 = PhotoImage(
            file="assets/frame1/image_1.png")
        self.image_1 = self.canvas.create_image(
            721.0,
            519.0,
            image=self.image_image_1
        )

        self.canvas.create_text(
            778.0,
            23.0,
            anchor="nw",
            text="BLUE MOON APARTMENT",
            fill="#FFFFFF",
            font=("Inter Bold", 48 * -1)
        )

        self.canvas.create_text(
            703.0,
            133.0,
            anchor="nw",
            text="Username:",
            fill="#FFFFFF",
            font=("Inter Bold", 36 * -1)
        )

        self.canvas.create_text(
            703.0,
            244.0,
            anchor="nw",
            text="Password:",
            fill="#FFFFFF",
            font=("Inter Bold", 36 * -1)
        )

        self.canvas.create_text(
            703.0,
            359.0,
            anchor="nw",
            text="Confirm Password:",
            fill="#FFFFFF",
            font=("Inter Bold", 28 * -1)
        )
    
        self.canvas.create_text(
            703.0,
            486.0,
            anchor="nw",
            text="Full Name:",
            fill="#FFFFFF",
            font=("Inter Bold", 32 * -1)
        )

        self.canvas.create_text(
            703.0,
            603.0,
            anchor="nw",
            text="Phone Number:",
            fill="#FFFFFF",
            font=("Inter Bold", 32 * -1)
        )

        self.canvas.create_text(
            703.0,
            710.0,
            anchor="nw",
            text="Appartment ID:",
            fill="#FFFFFF",
            font=("Inter Bold", 32 * -1)
        )

        self.image_image_2 = PhotoImage(
            file="assets/frame1/image_2.png")
        self.image_2 = self.canvas.create_image(
            343.0,
            516.5,
            image=self.image_image_2
        )

        entry_image_1 = PhotoImage(
            file="assets/frame1/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            1173.0,
            157.0,
            image=entry_image_1
        )
        self.username_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.username_entry.place(
            x=950.0,
            y=121.0,
            width=446.0,
            height=70.0
        )

        self.entry_image_2 = PhotoImage(
            file="assets/frame1/entry_2.png")
        self.entry_bg_2 = self.canvas.create_image(
            1173.0,
            272.0,
            image=self.entry_image_2
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
            x=950.0,
            y=236.0,
            width=446.0,
            height=70.0
        )

        self.entry_image_3 = PhotoImage(
            file="assets/frame1/entry_3.png")
        self.entry_bg_3 = self.canvas.create_image(
            1173.0,
            385.0,
            image=self.entry_image_3
        )
        self.confirm_password_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.confirm_password_entry.place(
            x=950.0,
            y=349.0,
            width=446.0,
            height=70.0
        )

        self.entry_image_4 = PhotoImage(
            file="assets/frame1/entry_4.png")
        self.entry_bg_4 = self.canvas.create_image(
            1173.0,
            500.0,
            image=self.entry_image_4
        )
        self.fullname_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.fullname_entry.place(
            x=950.0,
            y=464.0,
            width=446.0,
            height=70.0
        )

        self.entry_image_5 = PhotoImage(
            file="assets/frame1/entry_5.png")
        self.entry_bg_5 = self.canvas.create_image(
            1173.0,
            615.0,
            image=self.entry_image_5
        )
        self.phonenumber_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.phonenumber_entry.place(
            x=950.0,
            y=579.0,
            width=446.0,
            height=70.0
        )

        self.entry_image_6 = PhotoImage(
            file="assets/frame1/entry_6.png")
        self.entry_bg_6 = self.canvas.create_image(
            1173.0,
            728.0,
            image=self.entry_image_6
        )
        self.apartment_code_entry = Entry(
            bd=0,
            bg="#EEEEEE",
            fg="#000716",
            font=("Arial", 20),
            highlightthickness=0
        )
        self.apartment_code_entry.place(
            x=950.0,
            y=692.0,
            width=446.0,
            height=70.0
        )

        self.button_image_1 = PhotoImage(
            file="assets/frame1/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.toggle_password,
            relief="flat"
        )
        self.button_1.place(
            x=1293.0,
            y=243.0,
            width=91.0,
            height=57.0
        )

        self.button_image_2 = PhotoImage(
            file="assets/frame1/button_2.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            command=self.register,
            relief="flat"
        )
        self.button_2.place(
            x=922.0,
            y=805.0,
            width=291.0,
            height=97.0
        )

        self.button_image_3 = PhotoImage(
            file="assets/frame1/button_3.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            command=self.controller.show_login_frame,
            relief="flat"
        )
        self.button_3.place(
            x=910.0,
            y=919.0,
            width=315.0,
            height=66.0
        )

    def toggle_password(self):
        """Toggle password visibility."""
        if self.password_visible:
            self.password_entry.configure(show="*")
        else:
            self.password_entry.configure(show="")
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

        # Clear previous warnings
        # self.clear_warnings()

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
        if not phone_number:
            self.phonenumber_label.configure(text="Phone number is required")
            valid = False

        if not apartment_code:
            self.apartment_code_label.configure(text="Apartment code is required")
            valid = False

        if not valid:
            return

        # Attempt to register the user
        try:
            if self.is_user:
                self.controller.auth_manager.register_user(username, password, full_name, phone_number, apartment_code)
            else:
                self.controller.auth_manager.register_user(username, password, full_name, phone_number,  apartment_code, account_type='admin')
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
        self.geometry("1440x1024")  # Default size before full screen

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
