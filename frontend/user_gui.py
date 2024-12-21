from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, Scrollbar, RIGHT, Y, LEFT, BOTH
from tkinter import ttk
import tkinter as tk
from backend.weather import get_address_and_weather
from backend.db import DBManager
from backend.auth import AuthManager
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageTk
from tkinter import messagebox, Toplevel
import random
from datetime import datetime 

class UserGUI(Tk):
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.db_manager = AuthManager().db
        self.root.geometry("1012x720")
        self.root.configure(bg="#FFFFFF")
        self.root.resizable(False, False)

        self.canvas = Canvas(
            self.root,
            bg = "#FFFFFF",
            height = 720,
            width = 1012,
            bd = 0,
            highlightthickness = 0,
            relief = "ridge"
        )
        self.canvas.place(x = 0, y = 0)

        self.canvas.create_rectangle(
            196.171875,
            0.0,
            1012.5,
            71.71875,
            fill="#FFFFFF",
            outline="")

        self.phong_bat_img = PhotoImage(
            file="assets/admin_gui/image_2.png")
        self.phong_bat = self.canvas.create_image(
            98.0,
            35.0,
            image=self.phong_bat_img
        )

        self.canvas.create_rectangle(
            772.03125,
            0.0,
            1012.5,
            71.71875,
            fill="#130DBA",
            outline="")
        
        self.avatar_img = PhotoImage(
            file="assets/user_gui/image_1.png")
        self.avatar = self.canvas.create_image(
            255.21875,
            35.765625,
            image=self.avatar_img
        )

        self.hello_text_field = self.canvas.create_text(
            301.640625,
            18.984375,
            anchor="nw",
            text="Hello, " + user['full_name'],
            fill="#000000",
            font=("Inter Bold", 28 * -1)
        )
        
        address, temp = get_address_and_weather()
        self.canvas.create_text(
            787.25,
            14.0,
            anchor="nw",
            text=address,
            fill="#FFFFFF",
            font=("Inter", 24 * -1)
        )

        self.canvas.create_text(
            905.25-50,
            15.0,
            anchor="nw",
            text=temp,
            fill="#FFFFFF",
            font=("Inter Bold", 24 * -1)
        )

        self.noti_img = Image.open("assets/admin_gui/noti.png")
        self.noti_img = self.noti_img.resize((45, 45))
        self.noti_img = ImageTk.PhotoImage(self.noti_img)
        self.noti_button = Button(
            image=self.noti_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_noti,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            relief="flat"
        )
        self.noti_button.place(
            x=713.5,
            y=13.5,
            width=45,
            height=45
        )

        self.canvas.create_text(
            211.640625,
            85.78125,
            anchor="nw",
            text="Home",
            fill="#000000",
            font=("Inter Bold", 33 * -1)
        )

        self.canvas.create_rectangle(
            196.171875,
            71.71875,
            1012.5,
            141.328125,
            fill="#F2EDF3",
            outline="")
        
        self.canvas.create_rectangle(
            196.171875,
            71.71875,
            220,
            720,
            fill="#F2EDF3",
            outline="")

        self.canvas.create_rectangle(
            220,
            141.32812,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")
        
        self.image_image_4 = PhotoImage(
            file="assets/user_gui/image_4.png")
        self.image_4 = self.canvas.create_image(
            98.25,
            560.0,
            image=self.image_image_4
        )

        self.profile_img = PhotoImage(
            file="assets/user_gui/button_4_red.png")
        self.profile_button = Button(
            image=self.profile_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.show_profile,
            relief="flat"
        )
        self.profile_button.place(
        x=18.281219482421875,
        y=111.09375,
        width=170.859375,
        height=42.890625
        )

        self.view_fee_img= PhotoImage(
            file="assets/user_gui/button_7.png")
        self.view_fee_button= Button(
            image=self.view_fee_img,
            borderwidth=0,
            highlightthickness=0,
            background= "#FFFFFF",
            activebackground="#FFFFFF",
            command=self.view_fee,
            relief="flat"
        )
        self.view_fee_button.place(
            x=18.281219482421875,
            y=186.328,
            width=170.859375,
            height=42.890625
        )

        self.pay_img = PhotoImage(
            file="assets/user_gui/button_5.png")
        self.pay_button= Button(
            image=self.pay_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.pay,
            relief="flat"
        )
        self.pay_button.place(
            x=18.281219482421875,
            y=261.5625,
            width=170.859375,
            height=42.890625
        )

        self.noti_img = PhotoImage(
            file="assets/user_gui/button_3.png")
        self.noti_button= Button(
            image=self.noti_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.my_noti,
            relief="flat"
        )
        self.noti_button.place(
            x=18.281219482421875,
            y=336.796875,
            width=170.859375,
            height=42.890625
            
        )

        self.log_out_img = PhotoImage(
            file="assets/user_gui/button_6.png")
        self.log_out_button= Button(
            image=self.log_out_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.log_out,
            relief="flat"
        )
        self.log_out_button.place(
            x=18.281219482421875,
            y=401.796875,
            width=170.859375,
            height=42.890625
            
        )
        self.tree = None
        self.show_profile()
    
    def show_noti(self):
        pass

    def show_profile(self):
        new_image = PhotoImage(file="assets/user_gui/button_4_red.png")
        self.profile_button.config(image=new_image)
        self.profile_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_7.png")
        self.view_fee_button.config(image=new_image)
        self.view_fee_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_3.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(207.25, 103.0, 1012.5, 720)
        self.canvas.create_rectangle(
            220,
            141,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")
        
        self.image_img = Image.open("assets/profile/image_1.png")
        self.image_img = self.image_img.resize((817, 589))
        self.image_img = ImageTk.PhotoImage(self.image_img)
        self.image_1 = self.canvas.create_image(
            626.25,
            435.5,
            image=self.image_img
        )

        self.hello_text_field = self.canvas.create_text(
            301.640625,
            18.984375,
            anchor="nw",
            text="Hello, " + self.user['full_name'],
            fill="#000000",
            font=("Inter Bold", 28 * -1)
        )

        full_name = self.user.get('full_name', 'NULL')
        date_of_birth = self.user.get('dob', 'NULL')
        phone_number = self.user.get('phone_number', 'NULL')
        gender = self.user.get('gender', 'NULL')
        apartment_code = self.user.get('apartment_code', 'NULL')
        hometown = self.user.get('hometown', 'NULL')
        id_card = self.user.get('id_card', 'NULL')

        highlight_color = "#FF0000"  # Red color for highlighting

        self.canvas.create_text(
            576.25,
            180.0,
            anchor="nw",
            text="User information",
            fill="#000000",
            font=("Inter Black", 30 * -1)
        )

        self.image_image_2 = PhotoImage(
            file="assets/profile/image_2.png")
        self.image_2 = self.canvas.create_image(
            98.25,
            33.0,
            image=self.image_image_2
        )

        self.image_image_4 = PhotoImage(
            file="assets/profile/image_4.png")
        self.image_4 = self.canvas.create_image(
            98.25,
            580.0,
            image=self.image_image_4
        )

        self.image_image_5 = PhotoImage(
            file="assets/profile/image_5.png")
        self.image_5 = self.canvas.create_image(
            495.25,
            18.0,
            image=self.image_image_5
        )

        self.image_image_6 = PhotoImage(
            file="assets/profile/image_6.png")
        self.image_6 = self.canvas.create_image(
            667.25,
            231.0,
            image=self.image_image_6
        )

        self.image_image_7 = PhotoImage(
            file="assets/profile/image_7.png")
        self.image_7 = self.canvas.create_image(
            939.25,
            595.0,
            image=self.image_image_7
        )

        self.image_image_8 = PhotoImage(
            file="assets/profile/image_8.png")
        self.image_8 = self.canvas.create_image(
            373.25,
            74.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file="assets/profile/image_9.png")
        self.image_9 = self.canvas.create_image(
            607.25,
            55.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file="assets/profile/image_10.png")
        self.image_10 = self.canvas.create_image(
            431.25,
            183.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file="assets/profile/image_11.png")
        self.image_11 = self.canvas.create_image(
            415.25,
            490.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file="assets/profile/image_12.png")
        self.image_12 = self.canvas.create_image(
            811.25,
            443.0,
            image=self.image_image_12
        )

        self.image_image_13 = PhotoImage(
            file="assets/profile/image_13.png")
        self.image_13 = self.canvas.create_image(
            760.25,
            666.0,
            image=self.image_image_13
        )

        self.image_image_14 = PhotoImage(
            file="assets/profile/image_14.png")
        self.image_14 = self.canvas.create_image(
            276.25,
            354.0,
            image=self.image_image_14
        )

        self.image_image_15 = PhotoImage(
            file="assets/profile/image_15.png")
        self.image_15 = self.canvas.create_image(
            932.25,
            319.0,
            image=self.image_image_15
        )

        self.image_image_16 = PhotoImage(
            file="assets/profile/image_16.png")
        self.image_16 = self.canvas.create_image(
            330.25,
            610.0,
            image=self.image_image_16
        )

        self.image_image_17 = PhotoImage(
            file="assets/profile/image_17.png")
        self.image_17 = self.canvas.create_image(
            639.25,
            134.0,
            image=self.image_image_17
        )

        self.image_image_18 = PhotoImage(
            file="assets/profile/image_18.png")
        self.image_18 = self.canvas.create_image(
            103.25,
            235.0,
            image=self.image_image_18
        )

        self.image_image_19 = PhotoImage(
            file="assets/profile/image_19.png")
        self.image_19 = self.canvas.create_image(
            180.25,
            473.0,
            image=self.image_image_19
        )

        self.image_image_20 = PhotoImage(
            file="assets/profile/image_20.png")
        self.image_20 = self.canvas.create_image(
            36.25,
            447.0,
            image=self.image_image_20
        )

        random_color = "#{:06x}".format(random.randint(0, 0xFFFFFF))

        self.canvas.create_oval(
            229.25,
            214.0,
            363.25,
            348.0,
            fill=random_color,  # Màu ngẫu nhiên
            outline=""  # Không có đường viền
        )

        self.image_image_21 = PhotoImage(
            file="assets/profile/image_21.png")
        self.image_21 = self.canvas.create_image(
            66.25,
            89.0,
            image=self.image_image_21
        )

        self.image_image_22 = PhotoImage(
            file="assets/profile/image_22.png")
        self.image_22 = self.canvas.create_image(
            822.25,
            199.0,
            image=self.image_image_22
        )

        self.image_image_23 = PhotoImage(
            file="assets/profile/image_23.png")
        self.image_23 = self.canvas.create_image(
            544.25,
            198.0,
            image=self.image_image_23
        )
        self.canvas.create_text(
            406.25,
            236.0,
            anchor="nw",
            text=f"Full Name: {full_name}",
            fill=highlight_color if full_name == 'NULL' else "#000000",
            font=("Inter Bold", 24 * -1)
        )

        self.image_image_24 = PhotoImage(
            file="assets/profile/image_24.png")
        self.image_24 = self.canvas.create_image(
            391.25,
            245.0,
            image=self.image_image_24
        )

        self.canvas.create_text(
            682.25,
            295.0,
            anchor="nw",
            text=f"Date of birth: {date_of_birth}",
            fill=highlight_color if date_of_birth == 'NULL' else "#000000",
            font=("Inter Bold", 24 * -1)
        )

        self.canvas.create_text(
            406.25,
            356.0,
            anchor="nw",
            text=f"Phone Number: {phone_number}",
            fill=highlight_color if phone_number == 'NULL' else "#000000",
            font=("Inter Bold", 24 * -1)
        )

        self.canvas.create_text(
            405.25,
            293.0,
            anchor="nw",
            text=f"Gender: {gender}",
            fill=highlight_color if gender == 'NULL' else "#000000",
            font=("Inter Bold", 24 * -1)
        )

        self.image_image_25 = PhotoImage(
            file="assets/profile/image_25.png")
        self.image_25 = self.canvas.create_image(
            388.25,
            307.0,
            image=self.image_image_25
        )

        self.image_image_26 = PhotoImage(
            file="assets/profile/image_26.png")
        self.image_26 = self.canvas.create_image(
            664.25,
            309.0,
            image=self.image_image_26
        )
        self.image_image_27 = PhotoImage(
            file="assets/profile/image_27.png")
        self.image_27 = self.canvas.create_image(
            388.25,
            368.0,
            image=self.image_image_27
        )

        self.canvas.create_text(
            406.25,
            417.0,
            anchor="nw",
            text=f"Apartment Code: {apartment_code}",
            fill=highlight_color if apartment_code == 'NULL' else "#000000",
            font=("Inter Bold", 24 * -1)
        )

        self.image_image_28 = PhotoImage(
            file="assets/profile/image_28.png")
        self.image_28 = self.canvas.create_image(
            391.25,
            430.0,
            image=self.image_image_28
        )

        self.canvas.create_text(
            406.25,
            478.0,
            anchor="nw",
            text=f"Hometown: {hometown}",
            fill=highlight_color if hometown == 'NULL' else "#000000",
            font=("Inter Bold", 24 * -1)
        )

        self.image_image_29 = PhotoImage(
            file="assets/profile/image_29.png")
        self.image_29 = self.canvas.create_image(
            388.25,
            493.0,
            image=self.image_image_29
        )

        self.canvas.create_text(
            406.25,
            540.0,
            anchor="nw",
            text=f"ID Card: {id_card}",
            fill=highlight_color if id_card == 'NULL' else "#000000",
            font=("Inter Bold", 24 * -1)
        )

        self.image_image_30 = PhotoImage(
            file="assets/profile/image_30.png")
        self.image_30 = self.canvas.create_image(
            388.25,
            555.0,
            image=self.image_image_30
        )

        self.button_image_5 = PhotoImage(
            file="assets/profile/button_5.png")
        self.button_5 = Button(
            image=self.button_image_5,
            borderwidth=0,
            highlightthickness=0,
            bg="#ffffff",
            activebackground="#ffffff",
            command=self.button_5_click,
            relief="flat"
        )
        self.button_5.place(
            x=376.25,
            y=616.0,
            width=176.0,
            height=38.232208251953125
        )

        self.button_image_6 = PhotoImage(
            file="assets/profile/button_6.png")
        self.button_6 = Button(
            image=self.button_image_6,
            borderwidth=0,
            highlightthickness=0,
            bg="#ffffff",
            activebackground="#ffffff",
            command=self.button_6_click,
            relief="flat"
        )
        self.button_6.place(
            x=612.25,
            y=616.0,
            width=267.0,
            height=38.22999954223633
        )

        self.image_image_31 = PhotoImage(
            file="assets/profile/image_31.png")
        self.image_31 = self.canvas.create_image(
            855.25,
            524.0,
            image=self.image_image_31
        )

        self.image_image_32 = PhotoImage(
            file="assets/profile/image_32.png")
        self.image_32 = self.canvas.create_image(
            306.25,
            202.0,
            image=self.image_image_32
        )

    def button_5_click(self):
        self.update_window = Toplevel(self.root)
        self.update_window.title("Update Information")
        self.update_window.geometry("400x300")
        self.update_window.resizable(False, False)
        
        # Thêm canvas làm nền
        canvas = Canvas(self.update_window, width=400, height=300)
        canvas.pack(fill="both", expand=True)
        
        # Thêm ảnh nền (ảnh phải cùng thư mục hoặc cung cấp đường dẫn đầy đủ)
        bg_image = Image.open("assets/User_update.png")
        bg_image = bg_image.resize((400, 300))  # Điều chỉnh kích thước ảnh
        bg_photo = ImageTk.PhotoImage(bg_image)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Thêm nội dung vào cửa sổ
        label_font = ("Arial", 11, "bold")  # Đặt phông chữ cho các nhãn
        entry_font = ("Arial", 11)  # Đặt phông chữ cho ô nhập liệu

        # Full Name
        Label(self.update_window, text="Full Name:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=50, y=20)
        self.full_name_entry = Entry(self.update_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat")
        self.full_name_entry.place(x=180, y=20)
        self.full_name_entry.insert(0, self.user.get('full_name', ''))

        # Date of Birth
        Label(self.update_window, text="Date of Birth:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=50, y=60)
        self.dob_entry = Entry(self.update_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat")
        self.dob_entry.place(x=180, y=60)
        self.dob_entry.insert(0, self.user.get('dob', ''))

        # Phone Number
        Label(self.update_window, text="Phone Number:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=50, y=100)
        self.phone_entry = Entry(self.update_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat")
        self.phone_entry.place(x=180, y=100)
        self.phone_entry.insert(0, self.user.get('phone_number', ''))

        # Gender
        Label(self.update_window, text="Gender:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=50, y=140)
        self.gender_entry = Entry(self.update_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat")
        self.gender_entry.place(x=180, y=140)
        self.gender_entry.insert(0, self.user.get('gender', ''))

        # Hometown
        Label(self.update_window, text="Hometown:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=50, y=180)
        self.hometown_entry = Entry(self.update_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat")
        self.hometown_entry.place(x=180, y=180)
        self.hometown_entry.insert(0, self.user.get('hometown', ''))

        # ID Card
        Label(self.update_window, text="ID Card:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=50, y=220)
        self.id_card_entry = Entry(self.update_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat")
        self.id_card_entry.place(x=180, y=220)
        self.id_card_entry.insert(0, self.user.get('id_card', ''))

        # Save Button
        save_button = Button(self.update_window, text="Save", font=("Arial", 12, "bold"), bg="#FFB6C1", fg="#FFFFFF", command=self.save_changes)
        save_button.place(x=170, y=250)

        # Để giữ ảnh trong bộ nhớ
        self.update_window.bg_photo = bg_photo

    def save_changes(self):
        import re
        full_name = self.full_name_entry.get()
        dob = self.dob_entry.get()
        phone_number = self.phone_entry.get()
        gender = self.gender_entry.get()
        hometown = self.hometown_entry.get()
        id_card = self.id_card_entry.get()

        # Validate date of birth
        try:
            datetime.strptime(dob, "%Y-%m-%d")
        except ValueError:
            messagebox.showerror("Error", "Date of birth must be in YYYY-MM-DD format")
            return
        
        # Validate phone number
        if not re.match(r'^\d{10}$', phone_number):
            messagebox.showerror("Error", "Phone number must be 10 digits")
            return

        # Validate gender
        if gender not in ["male", "female", "undefined"]:
            messagebox.showerror("Error", "Gender must be 'male', 'female', or 'undefined'")
            return
        

        if messagebox.askyesno("Confirm", "Bạn có chắc chắn muốn thay đổi không?"):
            self.user['full_name'] = full_name
            self.user['dob'] = dob
            self.user['phone_number'] = phone_number
            self.user['gender'] = gender
            self.user['hometown'] = hometown
            self.user['id_card'] = id_card

            # Update the user information in the database
            self.db_manager.update_user(**self.user)

            messagebox.showinfo("Success", "Information updated successfully")
            self.update_window.destroy()
            self.show_profile()

    def button_6_click(self):
        self.change_password_window = Toplevel(self.root)
        self.change_password_window.title("Change Password")
        self.change_password_window.geometry("350x150")
        self.change_password_window.resizable(False, False)

        # Add canvas as background
        canvas = Canvas(self.change_password_window, width=350, height=150)
        canvas.pack(fill="both", expand=True)

        # Add background image
        bg_image = Image.open("assets/User_change.png")
        bg_image = bg_image.resize((350, 150))  # Adjust the image size
        bg_photo = ImageTk.PhotoImage(bg_image)
        canvas.create_image(0, 0, image=bg_photo, anchor="nw")

        # Add content to the window
        label_font = ("Arial", 10, "bold")  # Set font for labels
        entry_font = ("Arial", 10)  # Set font for entry fields

        # Adjusted coordinates
        x_label = 20  # x position for labels
        x_entry = 160  # x position for entry fields
        y_start = 20  # Starting y position
        y_gap = 30  # Gap between rows

        # Current Password
        Label(self.change_password_window, text="Current Password:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=x_label, y=y_start)
        self.current_password_entry = Entry(self.change_password_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat", show="*")
        self.current_password_entry.place(x=x_entry, y=y_start)

        # New Password
        Label(self.change_password_window, text="New Password:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=x_label, y=y_start + y_gap)
        self.new_password_entry = Entry(self.change_password_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat")
        self.new_password_entry.place(x=x_entry, y=y_start + y_gap)

        # Confirm Password
        Label(self.change_password_window, text="Confirm Password:", bg="#FFE6E6", fg="#000000", font=label_font).place(x=x_label, y=y_start + 2 * y_gap)
        self.confirm_password_entry = Entry(self.change_password_window, bg="#FFF5F5", fg="#000000", font=entry_font, relief="flat")
        self.confirm_password_entry.place(x=x_entry, y=y_start + 2 * y_gap)

        # Save Button
        button_width = 80  # Approximate button width in pixels
        x_center = (300 - button_width) / 2  # Centering the button horizontally
        save_button = Button(self.change_password_window, text="Save", font=("Arial", 10, "bold"), bg="#FFB6C1", fg="#FFFFFF", command=self.save_password)
        save_button.place(x=x_center+40, y=105)  # Place Save button centered vertically near the bottoms

        # Keep the background image in memory
        self.change_password_window.bg_photo = bg_photo


    def save_password(self):
        current_password = self.current_password_entry.get()
        new_password = self.new_password_entry.get()
        confirm_password = self.confirm_password_entry.get()

        if not current_password or not new_password or not confirm_password:
            messagebox.showerror("Error", "All fields are required")
            return

        if new_password != confirm_password:
            messagebox.showerror("Error", "New password and confirm password do not match")
            return

        try:
            self.db_manager.update_user_password(self.user['username'], new_password)
            messagebox.showinfo("Success", "Password updated successfully")
            self.change_password_window.destroy()
        except Exception as e:
            messagebox.showerror("Error", str(e))


        
        
    def view_fee(self):
        new_image = PhotoImage(file="assets/user_gui/button_4.png")
        self.profile_button.config(image=new_image)
        self.profile_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_7_red.png")
        self.view_fee_button.config(image=new_image)
        self.view_fee_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_3.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(202.25, 93.0, 1012.5, 720)

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        apt_code = self.user['apartment_code']
        fee_list = self.db_manager.view_fee_by_apartment_code(apt_code)


        # Create a Treeview
        style = ttk.Style()
        style.configure(
        "Custom.Treeview",
        font=("Arial", 14),  # Font set to Arial, size 14
        background="pink",  # Pink background
        foreground="black",  # Black text
        fieldbackground="pink",  # Pink table field background
        rowheight=30  # Adjust row height for better readability
    )
        style.configure(
        "Custom.Treeview.Heading",
        font=("Arial", 14, "bold"),  # Bold font for headings
        background="pink",  # Pink header background
        foreground="black"  # Black text for headers
    )
        self.tree = ttk.Treeview(self.root, style="Custom.Treeview")
        self.tree["columns"] = ("one", "two", "three","four")
        self.tree.column("#0", width=200, minwidth=100)
        self.tree.column("one", width=70, minwidth=100)
        self.tree.column("two", width=70, minwidth=100)
        self.tree.column("three", width=70, minwidth=100)
        self.tree.column("four", width=150, minwidth=100)

        self.tree.heading("#0", text="Fee Name", anchor=tk.W)
        self.tree.heading("one", text="Total", anchor=tk.W)
        self.tree.heading("two", text="Paid", anchor=tk.W)
        self.tree.heading("three", text="Remain", anchor=tk.W)
        self.tree.heading("four", text="Deadline", anchor=tk.W)

        # Insert some sample data
        for i in range(len(fee_list)):
            self.tree.insert("", "end", text=f"{fee_list[i]['fee_name']}", values=(f"{fee_list[i]['total']}", f"{fee_list[i]['paid']}", f"{fee_list[i]['remain']}", f"{fee_list[i]['deadline']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)

        # Bind double-click event
        # self.tree.bind("<Double-1>", self.on_double_click)

    def pay(self):
        new_image = PhotoImage(file="assets/user_gui/button_4.png")
        self.profile_button.config(image=new_image)
        self.profile_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_7.png")
        self.view_fee_button.config(image=new_image)
        self.view_fee_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_5_red.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_3.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(207.25, 103.0, 1012.5, 720)

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        self.canvas.create_text(
            650,
            170.0,
            text="Choose fee to pay",
            fill="#000000",
            font=("Inter Bold", 34 * -1)
        )

        self.canvas.create_text(
            305.25,
            247.0,
            anchor="nw",
            text="Fee Name:",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.button_image_1 = PhotoImage(
            file="assets/user_gui/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.find_fee,
            relief="flat"
        )
        self.button_1.place(
            x=499.25,
            y=354.0,
            width=200.0,
            height=60.0
        )

        self.paid_var = tk.StringVar()
        self.include_charity_var = tk.BooleanVar()

        def update_options():
            if self.include_charity_var.get():
                self.paid_options = self.db_manager.get_fee_need_to_pay(self.user['apartment_code'], include_charity=True)
            else:
                self.paid_options = self.db_manager.get_fee_need_to_pay(self.user['apartment_code'],include_charity=False)
            self.paid_dropdown['values'] = self.paid_options

        self.paid_options = self.db_manager.get_fee_need_to_pay(self.user['apartment_code'],include_charity=False)
        self.paid_dropdown = ttk.Combobox(
            self.root,
            textvariable=self.paid_var,
            values=self.paid_options,
            font=("Arial", 20),
            state="readonly"
        )
        self.paid_dropdown.place(
            x=610.25,
            y=242.0,
            width=278.0,
            height=36.0
        )
        self.paid_dropdown.configure(background="#00FF00", foreground="#FF0000")

        self.include_charity_check = tk.Checkbutton(
            self.root,
            text="love people ?",
            variable=self.include_charity_var,
            command=update_options,
            font=("Arial", 20),
            background="#FFFFFF"
        )
        self.paid_dropdown.place(
            x=610.25,
            y=242.0,
            width=278.0,
            height=36.0
        )
        self.include_charity_check.place(
            x=610.25,
            y=290.0
        )
        
    def log_out(self):
        self.root.show_login_frame()
    
    def on_double_click(self, event):
        # Get selected item
        item_id = self.tree.selection()[0]
        item = self.tree.item(item_id)

        # Create a top-level window for editing
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit Item")

        # Create entry widgets for each column
        tk.Label(edit_window, text="ID").grid(row=0, column=0)
        id_entry = tk.Entry(edit_window)
        id_entry.grid(row=0, column=1)
        id_entry.insert(0, item["text"])

        tk.Label(edit_window, text="Column 1").grid(row=1, column=0)
        col1_entry = tk.Entry(edit_window)
        col1_entry.grid(row=1, column=1)
        col1_entry.insert(0, item["values"][0])

        tk.Label(edit_window, text="Column 2").grid(row=2, column=0)
        col2_entry = tk.Entry(edit_window)
        col2_entry.grid(row=2, column=1)
        col2_entry.insert(0, item["values"][1])

        tk.Label(edit_window, text="Column 3").grid(row=3, column=0)
        col3_entry = tk.Entry(edit_window)
        col3_entry.grid(row=3, column=1)
        col3_entry.insert(0, item["values"][2])

        # Save button to update the item
        def save_changes():
            self.tree.item(item_id, text=id_entry.get(), values=(col1_entry.get(), col2_entry.get(), col3_entry.get()))
            edit_window.destroy()

        tk.Button(edit_window, text="Save", command=save_changes).grid(row=4, column=0, columnspan=2)

    def hide_buttons_in_region(self, x1, y1, x2, y2):
        def hide_widget(widget):
            widget_x = widget.winfo_x()
            widget_y = widget.winfo_y()
            if x1 <= widget_x <= x2 and y1 <= widget_y <= y2:
                widget.place_forget()

        for widget in self.root.winfo_children():
            if isinstance(widget, (tk.Button, tk.Entry, tk.Text, tk.Checkbutton)):
                hide_widget(widget)
            elif isinstance(widget, tk.Canvas):
                for canvas_widget in widget.winfo_children():
                    if isinstance(canvas_widget, (tk.Button, tk.Entry, tk.Text)):
                        hide_widget(canvas_widget)

    def find_fee(self):
        fee_name= self.paid_dropdown.get()
        type_of_fee = self.db_manager.get_type(fee_name)
        apartment_code= self.user['apartment_code']
        user_fee_info = self.db_manager.user_fee_info(apartment_code, fee_name)
        if user_fee_info is None and type_of_fee == 'unrequired':
            self.db_manager.add_user_info_to_charity(apartment_code, fee_name)
            # fetch again
            user_fee_info = self.db_manager.user_fee_info(apartment_code, fee_name)
        if user_fee_info is None and type_of_fee == 'required':
            raise Exception(f"Required fee {fee_name} is not added to apartment {apartment_code}")
        try:
            apt_code = user_fee_info['apt_code']
        except:
            self.canvas.create_text(
                585.25,
                465.0,
                text="No fee found",
                fill="#000000",
                font=("Arial", 20))
        feename = user_fee_info['feename']
        total= user_fee_info['total']
        money_paid = user_fee_info['money_paid']
        money_remain = user_fee_info['money_remain']
        status = user_fee_info['status']
        self.canvas.create_rectangle(
            220,
            420,
            700,
            720,
            fill="#FFFFFF",
            outline="#000000")
        self.canvas.create_rectangle(
            700,
            420,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")
        self.canvas.create_text(
            450.25,
            450.0,
            text="Fee Information",
            fill="#000000",
            font=("Arial", 24)
        )
        self.canvas.create_text(
            270.25,
            490.0,
            text="Apartment Code: ",
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
        self.canvas.create_text(
            270.25,
            530.0,
            text="Fee Name: ",
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
        if type_of_fee == 'required':
            self.canvas.create_text(
                270.25,
                570.0,
                text="Total: ",
                fill="#000000",
                anchor="nw",
                font=("Arial", 20)
            )
        self.canvas.create_text(
            270.25,
            610.0,
            text="Paid: ",
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
        if type_of_fee == 'required':
            self.canvas.create_text(
                270.25,
                650.0,
                text="Remain: ",
                fill="#000000",
                anchor="nw",
                font=("Arial", 20)
            )

        self.canvas.create_text(
            500.25,
            490.0,
            text=apt_code,
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
        truncated_feename = (feename[:15] + '...') if len(feename) > 15 else feename
        self.canvas.create_text(
            500.25,
            530.0,
            text=truncated_feename,
            fill="#000000",
            anchor="nw",
            font=("Arial", 20),
            tags="feename"
        )

        if len(feename) > 15:
            def show_full_feename(event):
                x, y, _, _ = self.canvas.bbox("feename")
                self.tooltip = self.canvas.create_text(
                    x, y - 20,
                    anchor="nw",
                    text=feename,
                    fill="#000000",
                    font=("Arial", 12),
                    tags="full_feename"
                )
                


            def hide_full_feename(event):
                self.canvas.delete("full_feename")

            self.canvas.tag_bind("feename", "<Enter>", show_full_feename)
            self.canvas.tag_bind("feename", "<Leave>", hide_full_feename)
        if type_of_fee == 'required':
            self.canvas.create_text(
                500.25,
                570.0,
                text=total,
                fill="#000000",
                anchor="nw",
                font=("Arial", 20)
            )
        self.canvas.create_text(
            500.25,
            610.0,
            text=money_paid,
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
        if type_of_fee == 'required':
            self.canvas.create_text(
                500.25,
                650.0,
                text=money_remain,
                fill="#000000",
                anchor="nw",
                font=("Arial", 20)
            )
        
        self.canvas.create_text(
            850.25,
            450.0,
            text="Payment",
            fill="#000000",
            font=("Arial", 24)
        )
        self.button_image_2 = PhotoImage(
            file="assets/user_gui/button_2.png")
        self.button_2 = Button(
            image=self.button_image_2,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=lambda: self.pay_money(apartment_code, fee_name,money_remain),
            relief="flat"
        )
        self.button_2.place(
            x=800.25,
            y=630.0,
            width=118.0,
            height=46.0
        )

        self.entry_image = PhotoImage(
            file="assets/user_gui/entry_2.png")
        self.entry_bg = self.canvas.create_image(
            855.75,
            527.0,
            image=self.entry_image
        )
        self.paid_entry = Entry(
            bd=0,
            bg="#96E6A1",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20)
        )
        self.paid_entry.place(
            x=758.25,
            y=497.0,
            width=195.0,
            height=58.0
        )

    def pay_money(self, apt_code, fee_name, money_remain):
        money_paid = int(self.paid_entry.get())
        fee_type = self.db_manager.get_type(fee_name)
        violate_condition_for_required = False
        if fee_type == 'required':
            violate_condition_for_required = money_paid<1000 or money_paid>money_remain or money_paid%1000!=0
        condition = (fee_type == 'unrequired') or (fee_type == 'required' and not violate_condition_for_required)
        if (not condition):
            self.canvas.create_text(
                850.25,
                600.0,
                text="Invalid amount",
                fill="red",
                font=("Arial", 16)
            )
        else:       
            self.hide_buttons_in_region(700, 420, 1012.5, 720)

            self.canvas.create_rectangle(
            700,
            420,
            1012.5,
            720,
            fill="#FFFFFF",

            outline="#000000")
            self.canvas.create_text(
                850.25,
                440.0,
                text="Scan QR to payment",
                fill="#000000",
                font=("Arial", 20)
            )

            self.qr_img = Image.open("assets/user_gui/qr.png")
            self.qr_img = self.qr_img.resize((200, 200))
            self.qr_img = ImageTk.PhotoImage(self.qr_img)
            self.canvas.create_image(
                850.75,
                570.0,
                image=self.qr_img)

            self.finish_img = Image.open("assets/user_gui/finish.png")
            self.finish_img = self.finish_img.resize((200, 60))
            self.finish_img = ImageTk.PhotoImage(self.finish_img)
            self.finish_button = Button(
                image=self.finish_img,
                borderwidth=0,
                highlightthickness=0,
                background="#FFFFFF",
                activebackground="#FFFFFF",
                command=lambda: self.finish(money_paid, apt_code, fee_name),
                relief="flat"
            )
            self.finish_button.place(
                x=750,
                y=646,
                width=200.0,
                height=54.0
            )
    
    def finish(self, money_paid, apt_code, fee_name):
        self.db_manager.thu_fee( apt_code, fee_name, money_paid)
        self.hide_buttons_in_region(220,141, 1012.5, 720)
        self.canvas.create_rectangle(
            220,
            141,
            1012.5,
            720,
            fill="#FFFFFF",

            outline="#000000")
        self.canvas.create_text(
            450.25,
            158.0,
            anchor="nw",
            text="Payment successful",
            fill="#000000",
            font=("Inter Bold", 36 * -1)
        )

        self.continue_img = Image.open("assets/user_gui/continue.png")
        self.continue_img = self.continue_img.resize((300, 60))
        self.continue_img = ImageTk.PhotoImage(self.continue_img)
        self.continue_button = Button(
            image=self.continue_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.pay,
            relief="flat"
        )
        self.continue_button.place(
            x=450,
            y=640,
            width=300.0,
            height=60.0
        )

        self.success_img = Image.open("assets/user_gui/success.png")
        self.success_img = self.success_img.resize((400, 400))
        self.success_img = ImageTk.PhotoImage(self.success_img)
        self.canvas.create_image(
            600.75,
            400.0,
            image=self.success_img)


    def send_noti(self):
        new_image = PhotoImage(file="assets/user_gui/button_4.png")
        self.profile_button.config(image=new_image)
        self.profile_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_7.png")
        self.view_fee_button.config(image=new_image)
        self.view_fee_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_3_red.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(220, 141, 1012.5, 720)

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        self.my_noti_img = Image.open("assets/user_gui/my_white.png")
        self.my_noti_img = self.my_noti_img.resize((397, 60))
        self.my_noti_img = ImageTk.PhotoImage(self.my_noti_img)
        self.my_noti_button = Button(
            image=self.my_noti_img,
            borderwidth=1,
            highlightthickness=0,
            command=self.my_noti,
            relief="solid"
        )
        self.my_noti_button.place(
            x=220,
            y=141.32812,
            width=396.5,
            height=60
        )

        self.send_noti_img = Image.open("assets/user_gui/send_noti.png")
        self.send_noti_img = self.send_noti_img.resize((397, 60))
        self.send_noti_img = ImageTk.PhotoImage(self.send_noti_img)
        self.send_noti_button = Button(
            image=self.send_noti_img,
            borderwidth=1,
            highlightthickness=0,
            command=self.send_noti,
            relief="solid"
        )
        self.send_noti_button.place(
            x=616.5,
            y=141.32812,
            width=396.5,
            height=60
        )

        self.canvas.create_text(
            225,
            210,
            text="To:",
            anchor="nw",
            fill="#000000",
            font=("Arial", 20)
        )

        self.canvas.create_text(
            225,
            250,
            text="Title:",
            anchor="nw",
            fill="#000000",
            font=("Arial", 20)
        )

        self.canvas.create_text(
            225,
            290,
            text="Content:",
            anchor="nw",
            fill="#000000",
            font=("Arial", 20)
        )

        self.to_entry_img = Image.open("assets/user_gui/entry_7.png")
        self.to_entry_img = self.to_entry_img.resize((230, 40))
        self.to_entry_img = ImageTk.PhotoImage(self.to_entry_img)
        self.canvas.create_image(
            285,
            205.0,
            anchor="nw",
            image=self.to_entry_img
        )

        self.to_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font = ("Arial", 20)
        )
        self.to_entry.place(
            x=293.0,
            y=212.0,
            anchor="nw",
            width=200.0,
            height=30.0
        )

        self.title_entry_img = Image.open("assets/user_gui/entry_4.png")
        self.title_entry_img = self.title_entry_img.resize((700, 40))
        self.title_entry_img = ImageTk.PhotoImage(self.title_entry_img)
        self.canvas.create_image(
            287,
            245.0,
            anchor="nw",
            image=self.title_entry_img
        )

        self.title_entry = Entry(
            bd=0,
            bg="#FFFFFF",
            highlightthickness=0,
            font = ("Arial", 20),
            validate="key",
            validatecommand=(self.canvas.register(self.validate_entry), "%P")
        )
        self.title_entry.place(
            x=297.0,
            y=252.0,
            anchor="nw",
            width=660.0,
            height=30.0
        )

        self.content_entry_img = Image.open("assets/user_gui/entry_5.png")
        self.content_entry_img = self.content_entry_img.resize((730, 380))
        self.content_entry_img = ImageTk.PhotoImage(self.content_entry_img)
        self.canvas.create_image(
            257,
            325.0,
            anchor="nw",
            image=self.content_entry_img
        )

        self.custom_text = Text(
            borderwidth=0,  # Set border width
            relief="solid",  # Set relief to solid to show the border
            font=("Arial", 20),  # Set font size
            wrap="word"  # Enable word wrapping
        )
        self.custom_text.place(
            x=277,  # Adjust x position
            y=335,  # Adjust y position
            anchor="nw",
            width=700,  # Adjust width
            height=350  # Adjust height
        )
        self.custom_text.insert("1.0", "")

        self.send_button_img = Image.open("assets/user_gui/send.png")
        self.send_button_img = self.send_button_img.resize((105, 35))
        self.send_button_img = ImageTk.PhotoImage(self.send_button_img)
        self.send_button = Button(
            image=self.send_button_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=lambda: self.try_send(self.user['apartment_code']),
            relief="flat"
        )
        self.send_button.place(
            x=850.0,
            y=205.0,
            width=108.0,
            height=38.0
        )
    
    def try_send(self, apt_code):
        self.canvas.create_rectangle(
        340.0,
        290.0,
        600.0,
        315,
        fill="#FFFFFF",
        outline="#FFFFFF")
        to= self.to_entry.get()
        title= self.title_entry.get()
        content= self.custom_text.get("1.0", "end-1c")
        if (to=="" or title=="" or content==""):
            self.canvas.create_text(
                350,
                290.0,
                anchor="nw",
                text="Please fill all fields",
                fill="red",
                font=("Arial", 20)
            )
        elif (to==self.user['apartment_code']):
            self.canvas.create_text(
                350,
                290.0,
                anchor="nw",
                text="Cannot send to yourself",
                fill="red",
                font=("Arial", 20))
        elif (self.db_manager.get_user_by_apartment_code(to)==None):
            self.canvas.create_text(
                350,
                290.0,
                anchor="nw",
                text="Apartment code not found",
                fill="red",
                font=("Arial", 20))
        else:
            self.db_manager.send_noti(apt_code, to, title, content)
            self.send_success()

    def send_success(self):
        self.hide_buttons_in_region(220, 141, 1012.5, 720)
        self.canvas.create_rectangle(
            220,
            141,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")
        self.canvas.create_text(
            380.25,
            158.0,
            anchor="nw",
            text="Notification Sent Successfully",
            fill="#000000",
            font=("Inter Bold", 36 * -1)
        )

        self.continue_img = Image.open("assets/user_gui/finish.png")
        self.continue_img = self.continue_img.resize((200, 60))
        self.continue_img = ImageTk.PhotoImage(self.continue_img)
        self.continue_button = Button(
            image=self.continue_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.my_noti,
            relief="flat"
        )
        self.continue_button.place(
            x=500,
            y=650,
            width=200.0,
            height=60.0
        )

        self.success_img = Image.open("assets/user_gui/send_success.png")
        self.success_img = self.success_img.resize((400, 350))
        self.success_img = ImageTk.PhotoImage(self.success_img)
        self.canvas.create_image(
            600.75,
            400.0,
            image=self.success_img)

    def my_noti(self):
        new_image = PhotoImage(file="assets/user_gui/button_4.png")
        self.profile_button.config(image=new_image)
        self.profile_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_7.png")
        self.view_fee_button.config(image=new_image)
        self.view_fee_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_3_red.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(220, 141, 1012.5, 720)

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        self.my_noti_img = Image.open("assets/user_gui/my_noti.png")
        self.my_noti_img = self.my_noti_img.resize((397, 60))
        self.my_noti_img = ImageTk.PhotoImage(self.my_noti_img)
        self.my_noti_button = Button(
            image=self.my_noti_img,
            borderwidth=1,
            highlightthickness=0,
            command=self.my_noti,
            relief="solid"
        )
        self.my_noti_button.place(
            x=220,
            y=141.32812,
            width=396.5,
            height=60
        )

        self.send_noti_img = Image.open("assets/user_gui/send_white.png")
        self.send_noti_img = self.send_noti_img.resize((397, 60))
        self.send_noti_img = ImageTk.PhotoImage(self.send_noti_img)
        self.send_noti_button = Button(
            image=self.send_noti_img,
            borderwidth=1,
            highlightthickness=0,
            command=self.send_noti,
            relief="solid"
        )
        self.send_noti_button.place(
            x=616.5,
            y=141.32812,
            width=396.5,
            height=60
        )

        notis = self.db_manager.get_noti_by_apartment_code(self.user['apartment_code'])
        style = ttk.Style()
        style.configure(
        "Custom.Treeview",
        font=("Arial", 14),  # Font set to Arial, size 14
        background="pink",  # Pink background
        foreground="black",  # Black text
        fieldbackground="pink",  # Pink table field background
        rowheight=30  # Adjust row height for better readability
    )
        style.configure(
        "Custom.Treeview.Heading",
        font=("Arial", 14, "bold"),  # Bold font for headings
        background="pink",  # Pink header background
        foreground="black"  # Black text for headers
    )
        self.tree = ttk.Treeview(self.canvas, style="Custom.Treeview")
        self.tree["columns"] = ( "one", "two", "three")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=250, minwidth=100)
        self.tree.column("two", width=0, minwidth=0,stretch=tk.NO)
        self.tree.column("three", width=70, minwidth=100)

        self.tree.heading("#0", text="Sender", anchor=tk.W)
        self.tree.heading("one", text="Title", anchor=tk.W)
        self.tree.heading("two", text="Content", anchor=tk.W)
        self.tree.heading("three", text="Time", anchor=tk.W)

        # Insert some sample data
        for noti in notis:
            self.tree.insert("", "end", text=noti['full_name'], values=(noti['title'], noti['content'], noti['time']))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=201.32812, width=792, height=520)

        # Bind double-click event
        self.tree.bind("<Double-1>", self.show_noti_detail)

    def show_noti_detail(self, event):
        # Get selected item
        item_id = self.tree.selection()[0]
        noti = self.tree.item(item_id)
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(220, 201.32812, 1012.5, 720)

        self.canvas.create_rectangle(
        220,
        201.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        self.back_img = Image.open("assets/user_gui/back.png")
        self.back_img = self.back_img.resize((40, 40))
        self.back_img = ImageTk.PhotoImage(self.back_img)
        self.back_button = Button(
            image=self.back_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.my_noti,
            relief="solid"
        )
        self.back_button.place(
            x=230,
            y=215,
            width=40,
            height=40
        )

        self.canvas.create_text(
            630.25,
            220.0,
            text="Notification Detail",
            fill="#000000",
            font=("Arial", 24)
        )
        self.canvas.create_text(
            270.25,
            250.0,
            text="Sender: ",
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
        self.canvas.create_text(
            270.25,
            290.0,
            text="Title: ",
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
        self.canvas.create_text(
            270.25,
            330.0,
            text="Content: ",
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )

        self.canvas.create_text(
            400.25,
            250.0,
            text=noti['text'],
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
        self.canvas.create_text(
            350.25,
            290.0,
            text=noti['values'][0],
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )

        self.noti_text = Text(
            self.canvas,
            borderwidth=1,
            relief="solid",
            font=("Arial", 20),
            wrap="word"  # Enable word wrapping
        )
        self.noti_text.place(
            x=240.25,
            y=360.0,
            width=750,  # Adjust width to fit your layout
            height=350  # Adjust height to fit your layout
        )
        self.noti_text.insert("end", f"{noti['values'][1]}\n")
        self.noti_text.config(state="disabled")

        self.canvas.create_text(
            800.25,
            210.0,
            text=noti['values'][2],
            fill="#000000",
            anchor="nw",
            font=("Arial", 16)
        )
    def validate_entry(self, new_value):
        words = new_value.split()
        if len(words) > 15:
            return False
        return True
        