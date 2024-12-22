from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, messagebox, Toplevel
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import PhotoImage, Canvas
from backend.weather import get_address_and_weather
from backend.auth import AuthManager
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import cv2
import pandas as pd 
from os import environ
from tkinter import messagebox, Toplevel
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
# database ready

class RootGUI(Tk):
    def __init__(self, root, user):
        self.root = root
        self.user = user
        self.active_list = []
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
            file="assets/admin_gui/image_1.png")
        self.avatar = self.canvas.create_image(
            255.21875,
            35.765625,
            image=self.avatar_img
        )

        self.hello_text_field = self.canvas.create_text(
            301.640625,
            18.984375,
            anchor="nw",
            text="Hello, " + self.user['full_name'],
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

        self.home_img = PhotoImage(
            file="assets/admin_gui/button_1.png")
        self.home_button = Button(
            image=self.home_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.show_home,
            relief="flat"
        )
        self.home_place = self.home_button.place(
        x=18.281219482421875,
        y=111.09375,
        width=170.859375,
        height=42.890625
        )

        self.view_admin_img= PhotoImage(
            file="assets/admin_gui/edit_admin.png")
        self.view_admin_button= Button(
            image=self.view_admin_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.view_admin,
            relief="flat"
        )
        self.view_admin_button.place(
            x=18.281219482421875,
            y=186.328,
            width=170.859375,
            height=42.890625
        )

        self.view_user_img = PhotoImage(
            file="assets/admin_gui/button_3.png")
        self.view_user_button= Button(
            image=self.view_user_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.view_user,
            relief="flat"
        )
        self.view_user_button.place(
            x=18.281219482421875,
            y=261.5625,
            width=170.859375,
            height=42.890625
        )

        self.noti_img = PhotoImage(
            file="assets/admin_gui/button_4.png")
        self.noti_button = Button(
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

        self.edit_fee_img = PhotoImage(
            file="assets/admin_gui/button_5.png")
        self.edit_fee_button= Button(
            image=self.edit_fee_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.edit_fee,
            relief="flat"
        )
        self.edit_fee_button.place(
            x=18.281219482421875,
            y=412.03125,
            width=170.859375,
            height=42.890625
        )

        self.thong_ke_img = PhotoImage(
            file="assets/admin_gui/button_7.png")
        self.statistic_button = Button(
            image=self.thong_ke_img,
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.statistic,
            relief="flat"
        )
        self.statistic_button.place(
            x=18.281219482421875,
            y=487.265625,
            width=170.859375,
            height=42.890625
        )

        self.log_out_img = PhotoImage(
            file="assets/admin_gui/button_8.png")
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
            x=12.65625,
            y=553.359375,
            width=170.859375,
            height=42.890625
            
        )

        self.hide_buttons_in_region(1,1,1,1)

        self.tree = None
        self.show_home()

    def show_home(self):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1_red.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
        if self.tree:
            self.tree.place_forget()
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(220, 141, 1012.5, 720)
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
            text="Admin information",
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

        self.canvas.create_oval(
            229.25,
            214.0,
            363.25,
            348.0,
            fill="blue",
            outline="")

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
            836.25,
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
        if messagebox.askyesno("Confirm", "Bạn có chắc chắn muốn thay đổi không?"):
            self.user['full_name'] = self.full_name_entry.get()
            self.user['dob'] = self.dob_entry.get()
            self.user['phone_number'] = self.phone_entry.get()
            self.user['gender'] = self.gender_entry.get()
            self.user['hometown'] = self.hometown_entry.get()
            self.user['id_card'] = self.id_card_entry.get()

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


        
    def view_admin(self, editable=True):
        self.hide_buttons_in_region(190, 79.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_10_red.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
        if self.tree:
            self.tree.place_forget()

        # Draw background rectangle for the Treeview
        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        # Set up Treeview style
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

        # Initialize Treeview with two columns: Full Name and Apartment Code
        self.tree = ttk.Treeview(self.root, style="Custom.Treeview")
        self.tree["columns"] = ("full_name", "apartment_code")

        # Configure columns
        column_configs = [
            ("#0", "", 0),  # Hide default column
            ("full_name", "Full Name", 200),
            ("apartment_code", "Officer Code", 150),
        ]
        for col_id, col_name, width in column_configs:
            self.tree.column(col_id, width=width, minwidth=width, anchor=tk.W)
            self.tree.heading(col_id, text=col_name, anchor=tk.W)
        
        # Insert sample data
        data_full = self.db_manager.get_all_users(account_type='admin')
        data = [
            {"full_name": entry['full_name'], "apartment_code": entry['apartment_code']}
        for entry in data_full]
        for item in data:
            self.tree.insert("", "end", values=(item["full_name"], item["apartment_code"]))
        self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        # Place Treeview
        self.tree.place(x=220, y=141, width=792, height=579)
        self.vsb.place(x=992, y=141, height=579)

        # Bind events if editable
        if editable:
            self.tree.bind("<Double-1>", lambda event: self.edit_double_click2(event, 'admin'))

    def view_user(self, editable=True):
        # Hide buttons in the specified region
        self.hide_buttons_in_region(190, 79.32812, 1012, 720)

        # Update button images
        button_images = [
            ("assets/admin_gui/button_1.png", self.home_button),
            ("assets/admin_gui/edit_admin.png", self.view_admin_button),
            ("assets/admin_gui/button_3_red.png", self.view_user_button),
            ("assets/admin_gui/button_4.png", self.noti_button),
            ("assets/admin_gui/button_5.png", self.edit_fee_button),
            ("assets/admin_gui/button_7.png", self.statistic_button),
        ]
        for image_path, button in button_images:
            new_image = PhotoImage(file=image_path)
            button.config(image=new_image)
            button.image = new_image

        # Remove existing tree if present
        if hasattr(self, 'tree') and self.tree:
            self.tree.place_forget()

        # Draw background rectangle for the Treeview
        self.canvas.create_rectangle(
            220, 141.32812, 1012.5, 720,
            fill="#FFFFFF", outline="#000000"
        )

        # Set up Treeview style
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

        # Initialize Treeview with two columns: Full Name and Apartment Code
        self.tree = ttk.Treeview(self.root, style="Custom.Treeview")
        self.tree["columns"] = ("full_name", "apartment_code")

        # Configure columns
        column_configs = [
            ("#0", "", 0),  # Hide default column
            ("full_name", "Full Name", 200),
            ("apartment_code", "Apartment Code", 150),
        ]
        for col_id, col_name, width in column_configs:
            self.tree.column(col_id, width=width, minwidth=width, anchor=tk.W)
            self.tree.heading(col_id, text=col_name, anchor=tk.W)
        
        # Insert sample data
        data_full = self.db_manager.get_all_users(account_type='user')
        data = [
            {"full_name": entry['full_name'], "apartment_code": entry['apartment_code']}
        for entry in data_full]
        for item in data:
            self.tree.insert("", "end", values=(item["full_name"], item["apartment_code"]))
        self.vsb = ttk.Scrollbar(self.root, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscrollcommand=self.vsb.set)
        # Place Treeview
        self.tree.place(x=220, y=141, width=792, height=579)
        self.vsb.place(x=992, y=141, height=579)
        # Place Treeview
        self.tree.place(x=220, y=141, width=792, height=579)

        # Bind events if editable
        if editable:
            self.tree.bind("<Double-1>", lambda event: self.edit_double_click(event, 'user'))

    def edit_double_click(self, event, type):
        apt_high = "Apartment Code" if type == "user" else "Officer Code"
        pygame.mixer.init()
        pygame.mixer.music.load("assets/fun_time/bg.mp3")  # Replace with your music file path
        pygame.mixer.music.play(-1)
        data = self.db_manager.get_all_users(account_type=type)
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        user_details = None
        for item in data:
            if item['full_name'] == values[0] and item['apartment_code'] == values[1]:
                user_details = item
                break
        assert user_details is not None, f"User details not found for full_name {values[0]} - apt {values[1]}"
        old_apt_code = user_details['apartment_code']
        self.hide_buttons_in_region(190, 79.32812, 1012, 720)
        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        self.image_img = Image.open("assets/edit_user/image_1.png")
        self.image_img = self.image_img.resize((792, 579))
        self.image_img = ImageTk.PhotoImage(self.image_img)
        self.image_1 = self.canvas.create_image(
            220,
            141.32812,
            anchor="nw",
            image=self.image_img
        )
        self.canvas.create_rectangle(
            220 - 1, 141.32812 - 1, 220 + 792 + 1, 141.32812 + 579 + 1,  # Adjust the coordinates to fit the border
            outline="#000000",  # Border color
            width=2  # Border width
        )

        self.canvas.create_text(
            558.0,
            160.0,
            anchor="nw",
            text="Edit information",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.canvas.create_text(
            330,
            240,
            anchor="nw",
            text="Full Name:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            626.5+30+50,
            220.0+30,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_1.place(
            x=485.0+30+50,
            y=203.0+30,
            width=283.0,
            height=34.0
        )

        self.canvas.create_text(
            330,
            310,
            anchor="nw",
            text="User Name:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_2 = self.canvas.create_image(
            626.5+30+50,
            290.0+30,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_2.place(
            x=485.0+30+50,
            y=273.0+30,
            width=283.0,
            height=34.0
        )

        self.canvas.create_text(
            330,
            380,
            anchor="nw",
            text="Password:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_3 = self.canvas.create_image(
            626.5+30+50,
            360.0+30,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_3.place(
            x=485.0+30+50,
            y=343.0+30,
            width=283.0,
            height=34.0
        )

        self.canvas.create_text(
            330,
            450,
            anchor="nw",
            text=apt_high + ":",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_4 = self.canvas.create_image(
            626.5+30+50,
            430.0+30,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_4.place(
            x=485.0+30+50,
            y=413.0+30,
            width=283.0,
            height=34.0
        )

        self.canvas.create_text(
            330,
            520,
            anchor="nw",
            text="Phone Number:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_5 = self.canvas.create_image(
            626.5+30+50,
            500.0+30,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_5.place(
            x=485.0+30+50,
            y=483.0+30,
            width=283.0,
            height=34.0
        )

        self.entry_1.insert(0, user_details['full_name'])
        self.entry_2.insert(0, user_details['username'])
        self.entry_3.insert(0, user_details['password'])
        self.entry_4.insert(0, user_details['apartment_code'])
        self.entry_5.insert(0, user_details['phone_number'])

        def cancel_edit():
            pygame.mixer.music.stop()
            self.view_user()

        def delete_user():
            self.db_manager.delete_apt(old_apt_code)
            self.tree.delete(selected_item)
            pygame.mixer.music.stop()
            self.view_user()
        
        def save_edit():
            self.canvas.create_rectangle(
                500,
                600,
                1000,
                630,
                fill="#E1F3FD",
                outline="")
            full_name = self.entry_1.get()
            username = self.entry_2.get()
            password = self.entry_3.get()
            apt_code = self.entry_4.get()
            phone_number = self.entry_5.get()
            if not full_name or not username or not password or not apt_code or not phone_number:
                self.canvas.create_text(
                    500,
                    600,
                    anchor="nw",
                    text="Please fill in all fields",
                    fill="red",
                    font=("Inter", 20 * -1)
                )
                return
            if self.db_manager.get_user_by_apartment_code(apt_code) and apt_code != old_apt_code:
                self.canvas.create_text(
                    500,
                    600,
                    anchor="nw",
                    text="Apartment code already exists",
                    fill="red",
                    font=("Inter", 20 * -1)
                )
                return
            self.db_manager.update_user_by_admin(old_apt_code, full_name, username, password, apt_code, phone_number)
            pygame.mixer.music.stop()
            self.view_user()

        self.button_image_1 = PhotoImage(
            file="assets/edit_user/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            background="#E1F3FD",
            activebackground="#E1F3FD",
            command=save_edit, 
            relief="flat"
        )
        self.button_1.place(
            x=270.0,
            y=650.0,
            width=176.0,
            height=38.232208251953125
        )

        self.button_image_2 = PhotoImage(
            file="assets/edit_user/button_3.png")
        self.button_2 = Button(
            image=self.button_image_2, 
            borderwidth=0,
            highlightthickness=0,
            background="#E1F3FD",
            activebackground="#E1F3FD",
            command=cancel_edit,
            relief="flat"
        )
        self.button_2.place(
            x=520.0,
            y=650.0,
            width=176.0,
            height=38.232208251953125
        )

        self.button_image_3 = PhotoImage(
            file="assets/edit_user/button_2.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            background="#E1F3FD",
            activebackground="#E1F3FD",
            command=delete_user,
            relief="flat"
        )
        self.button_3.place(
            x=770.0,
            y=650.0,
            width=176.0,
            height=38.232208251953125
        )

        self.edit_img_2 = PhotoImage(
            file="assets/edit_user/image_2.png")
        self.edit_image_2 = self.canvas.create_image(
            309.0,
            255.0,
            image=self.edit_img_2
        )

        self.edit_img_3 = PhotoImage(
            file="assets/edit_user/image_3.png")
        self.edit_image_3 = self.canvas.create_image(
            309.0,
            322.0,
            image=self.edit_img_3
        )

        self.edit_img_4 = PhotoImage(
            file="assets/edit_user/image_4.png")
        self.edit_image_4 = self.canvas.create_image(
            309.0,
            391.0,
            image=self.edit_img_4
        )

        self.edit_img_6 = PhotoImage(
            file="assets/edit_user/image_6.png")
        self.edit_image_6 = self.canvas.create_image(
            308.0,
            466.0,
            image=self.edit_img_6
        )

        self.edit_img_7 = PhotoImage(
            file="assets/edit_user/image_7.png")
        self.edit_image_7 = self.canvas.create_image(
            311.0,
            532.0,
            image=self.edit_img_7
        )

        self.image_image_8 = PhotoImage(
            file="assets/edit_user/image_8.png")
        self.image_8 = self.canvas.create_image(
            535.0,
            175.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file="assets/edit_user/image_9.png") 
        self.image_9 = self.canvas.create_image(
            790.0,
            175.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file="assets/edit_user/image_10.png")
        self.image_10 = self.canvas.create_image(
            980.0,
            180.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file="assets/edit_user/image_11.png")
        self.image_11 = self.canvas.create_image(
            250.0,
            680.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file="assets/edit_user/image_12.png")
        self.image_12 = self.canvas.create_image(
            255.0,
            180.0,
            image=self.image_image_12
        )

    def edit_double_click2(self, event, type):
        apt_high = "Apartment Code" if type == "user" else "Officer Code"
        pygame.mixer.init()
        pygame.mixer.music.load("assets/fun_time/bg.mp3")  # Replace with your music file path
        pygame.mixer.music.play(-1)
        data = self.db_manager.get_all_users(account_type=type)
        selected_item = self.tree.selection()[0]
        values = self.tree.item(selected_item, 'values')
        user_details = None
        for item in data:
            if item['full_name'] == values[0] and item['apartment_code'] == values[1]:
                user_details = item
                break
        assert user_details is not None, f"User details not found for full_name {values[0]} - apt {values[1]}"
        old_apt_code = user_details['apartment_code']
        self.hide_buttons_in_region(190, 79.32812, 1012, 720)
        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        self.image_img = Image.open("assets/edit_user/image_1.png")
        self.image_img = self.image_img.resize((792, 579))
        self.image_img = ImageTk.PhotoImage(self.image_img)
        self.image_1 = self.canvas.create_image(
            220,
            141.32812,
            anchor="nw",
            image=self.image_img
        )
        self.canvas.create_rectangle(
            220 - 1, 141.32812 - 1, 220 + 792 + 1, 141.32812 + 579 + 1,  # Adjust the coordinates to fit the border
            outline="#000000",  # Border color
            width=2  # Border width
        )

        self.canvas.create_text(
            558.0,
            160.0,
            anchor="nw",
            text="Edit information",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.canvas.create_text(
            330,
            240,
            anchor="nw",
            text="Full Name:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            626.5+30+50,
            220.0+30,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_1.place(
            x=485.0+30+50,
            y=203.0+30,
            width=283.0,
            height=34.0
        )

        self.canvas.create_text(
            330,
            310,
            anchor="nw",
            text="User Name:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_2 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_2 = self.canvas.create_image(
            626.5+30+50,
            290.0+30,
            image=self.entry_image_2
        )
        self.entry_2 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_2.place(
            x=485.0+30+50,
            y=273.0+30,
            width=283.0,
            height=34.0
        )

        self.canvas.create_text(
            330,
            380,
            anchor="nw",
            text="Password:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_3 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_3 = self.canvas.create_image(
            626.5+30+50,
            360.0+30,
            image=self.entry_image_3
        )
        self.entry_3 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_3.place(
            x=485.0+30+50,
            y=343.0+30,
            width=283.0,
            height=34.0
        )

        self.canvas.create_text(
            330,
            450,
            anchor="nw",
            text=apt_high + ":",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_4 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_4 = self.canvas.create_image(
            626.5+30+50,
            430.0+30,
            image=self.entry_image_4
        )
        self.entry_4 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_4.place(
            x=485.0+30+50,
            y=413.0+30,
            width=283.0,
            height=34.0
        )

        self.canvas.create_text(
            330,
            520,
            anchor="nw",
            text="Phone Number:",
            fill="#000000",
            font=("Inter", 24 * -1)
        )

        self.entry_image_5 = PhotoImage(
            file="assets/edit_user/entry_1.png")
        self.entry_bg_5 = self.canvas.create_image(
            626.5+30+50,
            500.0+30,
            image=self.entry_image_5
        )
        self.entry_5 = Entry(
            bd=0,
            bg="#FFFFFF",
            fg="#000716",
            font=("Inter", 24 * -1),
            highlightthickness=0
        )
        self.entry_5.place(
            x=485.0+30+50,
            y=483.0+30,
            width=283.0,
            height=34.0
        )

        self.entry_1.insert(0, user_details['full_name'])
        self.entry_2.insert(0, user_details['username'])
        self.entry_3.insert(0, user_details['password'])
        self.entry_4.insert(0, user_details['apartment_code'])
        self.entry_5.insert(0, user_details['phone_number'])

        def cancel_edit():
            pygame.mixer.music.stop()
            self.view_admin()

        def delete_user():
            self.db_manager.delete_apt(old_apt_code)
            self.tree.delete(selected_item)
            pygame.mixer.music.stop()
            self.view_admin()
        
        def save_edit():
            self.canvas.create_rectangle(
                500,
                600,
                1000,
                630,
                fill="#E1F3FD",
                outline="")
            full_name = self.entry_1.get()
            username = self.entry_2.get()
            password = self.entry_3.get()
            apt_code = self.entry_4.get()
            phone_number = self.entry_5.get()
            if not full_name or not username or not password or not apt_code or not phone_number:
                self.canvas.create_text(
                    500,
                    600,
                    anchor="nw",
                    text="Please fill in all fields",
                    fill="red",
                    font=("Inter", 20 * -1)
                )
                return
            if self.db_manager.get_user_by_apartment_code(apt_code) and apt_code != old_apt_code:
                self.canvas.create_text(
                    500,
                    600,
                    anchor="nw",
                    text="Apartment code already exists",
                    fill="red",
                    font=("Inter", 20 * -1)
                )
                return
            self.db_manager.update_user_by_admin(old_apt_code, full_name, username, password, apt_code, phone_number)
            pygame.mixer.music.stop()
            self.view_admin()

        self.button_image_1 = PhotoImage(
            file="assets/edit_user/button_1.png")
        self.button_1 = Button(
            image=self.button_image_1,
            borderwidth=0,
            highlightthickness=0,
            background="#E1F3FD",
            activebackground="#E1F3FD",
            command=save_edit, 
            relief="flat"
        )
        self.button_1.place(
            x=270.0,
            y=650.0,
            width=176.0,
            height=38.232208251953125
        )

        self.button_image_2 = PhotoImage(
            file="assets/edit_user/button_3.png")
        self.button_2 = Button(
            image=self.button_image_2, 
            borderwidth=0,
            highlightthickness=0,
            background="#E1F3FD",
            activebackground="#E1F3FD",
            command=cancel_edit,
            relief="flat"
        )
        self.button_2.place(
            x=520.0,
            y=650.0,
            width=176.0,
            height=38.232208251953125
        )

        self.button_image_3 = PhotoImage(
            file="assets/edit_user/button_2.png")
        self.button_3 = Button(
            image=self.button_image_3,
            borderwidth=0,
            highlightthickness=0,
            background="#E1F3FD",
            activebackground="#E1F3FD",
            command=delete_user,
            relief="flat"
        )
        self.button_3.place(
            x=770.0,
            y=650.0,
            width=176.0,
            height=38.232208251953125
        )

        self.edit_img_2 = PhotoImage(
            file="assets/edit_user/image_2.png")
        self.edit_image_2 = self.canvas.create_image(
            309.0,
            255.0,
            image=self.edit_img_2
        )

        self.edit_img_3 = PhotoImage(
            file="assets/edit_user/image_3.png")
        self.edit_image_3 = self.canvas.create_image(
            309.0,
            322.0,
            image=self.edit_img_3
        )

        self.edit_img_4 = PhotoImage(
            file="assets/edit_user/image_4.png")
        self.edit_image_4 = self.canvas.create_image(
            309.0,
            391.0,
            image=self.edit_img_4
        )

        self.edit_img_6 = PhotoImage(
            file="assets/edit_user/image_6.png")
        self.edit_image_6 = self.canvas.create_image(
            308.0,
            466.0,
            image=self.edit_img_6
        )

        self.edit_img_7 = PhotoImage(
            file="assets/edit_user/image_7.png")
        self.edit_image_7 = self.canvas.create_image(
            311.0,
            532.0,
            image=self.edit_img_7
        )

        self.image_image_8 = PhotoImage(
            file="assets/edit_user/image_8.png")
        self.image_8 = self.canvas.create_image(
            535.0,
            175.0,
            image=self.image_image_8
        )

        self.image_image_9 = PhotoImage(
            file="assets/edit_user/image_9.png") 
        self.image_9 = self.canvas.create_image(
            790.0,
            175.0,
            image=self.image_image_9
        )

        self.image_image_10 = PhotoImage(
            file="assets/edit_user/image_10.png")
        self.image_10 = self.canvas.create_image(
            980.0,
            180.0,
            image=self.image_image_10
        )

        self.image_image_11 = PhotoImage(
            file="assets/edit_user/image_11.png")
        self.image_11 = self.canvas.create_image(
            250.0,
            680.0,
            image=self.image_image_11
        )

        self.image_image_12 = PhotoImage(
            file="assets/edit_user/image_12.png")
        self.image_12 = self.canvas.create_image(
            255.0,
            180.0,
            image=self.image_image_12
        )


    def edit_fee(self):
        self.hide_buttons_in_region(190, 79.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5_red.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        fee_list = self.db_manager.get_all_userfee()

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
        self.tree["columns"] = ("zero", "one", "three","four")
        self.tree.column("#0", width=200, minwidth=100)
        self.tree.column("zero", width=100, minwidth=100)
        self.tree.column("one", width=70, minwidth=100)
        # self.tree.column("two", width=70, minwidth=100)
        self.tree.column("three", width=70, minwidth=100)
        self.tree.column("four", width=150, minwidth=100)

        self.tree.heading("#0", text="Fee Name", anchor=tk.W)
        self.tree.heading("zero", text="Apartment", anchor=tk.W)
        self.tree.heading("one", text="Total", anchor=tk.W)
        # self.tree.heading("two", text="Paid", anchor=tk.W)
        self.tree.heading("three", text="Remain", anchor=tk.W)
        self.tree.heading("four", text="Deadline", anchor=tk.W)

        # Insert some sample data
        for i in range(len(fee_list)):
            self.tree.insert("", "end", text=f"{fee_list[i]['fee_name']}", values=(f"{fee_list[i]['apartment_code']}",f"{fee_list[i]['total']}",  f"{fee_list[i]['remain']}", f"{fee_list[i]['deadline']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=506)

        def confirm_delete_fee(event):
            selected_item = self.tree.selection()[0]
            values = self.tree.item(selected_item, 'values')
            fee_name = self.tree.item(selected_item, 'text')
            if messagebox.askokcancel("Delete Fee", f"Are you sure you want to delete {fee_name} for apartment {values[0]}?"):
                self.db_manager.delete_userfee(fee_name, values[0])
                self.tree.delete(selected_item)

        def confirm_delete_fee2(event):
            selected_item = self.tree.selection()[0]
            values = self.tree.item(selected_item, 'values')
            fee_name = self.tree.item(selected_item, 'text')
            if messagebox.askokcancel("Delete Fee", f"Are you sure you want to delete {fee_name} for all apartment?"):
                self.db_manager.delete_fee_to_all(fee_name)
                self.tree.place_forget()
                fee_list = self.db_manager.get_all_userfee()

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
                self.tree["columns"] = ("zero", "one", "three","four")
                self.tree.column("#0", width=200, minwidth=100)
                self.tree.column("zero", width=100, minwidth=100)
                self.tree.column("one", width=70, minwidth=100)
                # self.tree.column("two", width=70, minwidth=100)
                self.tree.column("three", width=70, minwidth=100)
                self.tree.column("four", width=150, minwidth=100)

                self.tree.heading("#0", text="Fee Name", anchor=tk.W)
                self.tree.heading("zero", text="Apartment", anchor=tk.W)
                self.tree.heading("one", text="Total", anchor=tk.W)
                # self.tree.heading("two", text="Paid", anchor=tk.W)
                self.tree.heading("three", text="Remain", anchor=tk.W)
                self.tree.heading("four", text="Deadline", anchor=tk.W)

                # Insert some sample data
                for i in range(len(fee_list)):
                    self.tree.insert("", "end", text=f"{fee_list[i]['fee_name']}", values=(f"{fee_list[i]['apartment_code']}",f"{fee_list[i]['total']}",  f"{fee_list[i]['remain']}", f"{fee_list[i]['deadline']}"))

                # Place the Treeview on top of the Canvas
                self.tree.place(x=220, y=141, width=792, height=506)
                self.tree.bind("<Double-1>", confirm_delete_fee)
                self.tree.bind("<Double-3>", confirm_delete_fee2)



        self.tree.bind("<Double-1>", confirm_delete_fee)
        self.tree.bind("<Double-3>", confirm_delete_fee2)

        self.addall_img=Image.open("assets/admin_gui/add_all.png")
        self.addall_img = self.addall_img.resize((220, 45))
        self.addall_img = ImageTk.PhotoImage(self.addall_img)
        self.add_all_button = Button(
            image=self.addall_img, 
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.add_all,
            relief="flat"
        )
        self.add_all_button.place(
            x=230.0,
            y=665.0,
            anchor="nw",
            width=220,
            height=45
        )

        self.add_img=Image.open("assets/admin_gui/add1.png")
        self.add_img = self.add_img.resize((320, 45))
        self.add_img = ImageTk.PhotoImage(self.add_img)
        self.add_button = Button(
            image=self.add_img, 
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.add1,
            relief="flat"
        )
        self.add_button.place(
            x=660.0,
            y=665.0,
            anchor="nw",
            width=320,
            height=45
        )

        self.new_img=Image.open("assets/admin_gui/new_fee.png")
        self.new_img = self.new_img.resize((150, 45))
        self.new_img = ImageTk.PhotoImage(self.new_img)
        self.new_fee_button = Button(
            image=self.new_img, 
            borderwidth=0,
            highlightthickness=0,
            background="#FFFFFF",
            activebackground="#FFFFFF",
            command=self.new_fee,
            relief="flat"
        )
        self.new_fee_button.place(
            x=480.0,
            y=665.0,
            anchor="nw",
            width=150,
            height=45
        )

    def add_all(self):
        popup = Toplevel(self.canvas)
        popup.title("Add Fee to All Apartments")
        popup.geometry("400x420")
        popup.resizable(False, False)
        # Create canvas to hold background image
        bg_canvas = Canvas(popup, width=400, height=420, highlightthickness=0)
        bg_canvas.pack(fill="both", expand=True)

        # Load and display background image
        bg_image = Image.open("assets/admin_gui/bg.png")
        bg_image = bg_image.resize((400, 420))
        self.bg_photo = ImageTk.PhotoImage(bg_image) # Save as instance var to prevent garbage collection
        bg_canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create frame to hold other widgets
        content_frame = Frame(popup, bg='#FFFFFF')
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        Label(popup, text="Fee Name:",font=("Arial",20), bg="#E1F3FD").place(x=20, y=20)
        self.fee_name_entry = Entry(popup,  font=("Arial",20))
        self.fee_name_entry.place(x=170, y=20,height=30, width=200)

        def on_type_selected(*args):
            selected_type = self.type_entry.get()
            if selected_type == "Unrequired":
                self.amount_entry.config(state="disabled")
            else:
                self.amount_entry.config(state="normal")

        Label(popup, text="Type:", font=("Arial",20), bg="#E1F3FD").place(x=20, y=80)
        self.type_entry = ttk.Combobox(popup, values=["Required", "Unrequired"],  font=("Arial",18) )
        self.type_entry.place(x=170, y=80, height=30, width=200)
        self.type_entry.bind("<<ComboboxSelected>>", on_type_selected)

        Label(popup, text="Total:", font=("Arial",20), bg="#E1F3FD").place(x=20, y=140)
        self.amount_entry = Entry(popup,  font=("Arial",20))
        self.amount_entry.place(x=170, y=140,height=30, width=200)

        Label(popup, text="Deadline:", font=("Arial",20), bg="#E1F3FD").place(x=20, y=200)
        self.deadline_entry = DateEntry(popup,  font=("Arial",20), date_pattern='y-mm-dd')
        self.deadline_entry.place(x=170, y=200,height=30, width=200)

        Label(popup, text="Time:", font=("Arial",20), bg="#E1F3FD").place(x=20, y=260)
        self.hour_entry = ttk.Combobox(popup, values=[f"{i:02d}" for i in range(24)], font=("Arial",18), width=3)
        self.hour_entry.place(x=170, y=260, height=30, width=60)
        self.minute_entry = ttk.Combobox(popup, values=[f"{i:02d}" for i in range(60)], font=("Arial",18), width=3)
        self.minute_entry.place(x=240, y=260, height=30, width=60)
        self.success_label = Label(popup, text="", font=("Arial",20), fg="red", bg="#E1F3FD")
        self.success_label.place(x=50, y=385)

        def submit_entries():
            fee_name = self.fee_name_entry.get()
            fee_type = self.type_entry.get()
            fee_type=fee_type.lower()
            if not fee_name or not fee_type:
                self.success_label.config(text="Please fill in all fields!")
            if fee_type == "unrequired":
                deadline_date = self.deadline_entry.get()
                deadline_time = f"{self.hour_entry.get()}:{self.minute_entry.get()}:00"
                if not deadline_date or not self.hour_entry.get() or not self.minute_entry.get(): 
                    self.success_label.config(text="Please fill in all fields!")
                    return
                deadline = f"{deadline_date} {deadline_time}"
                self.db_manager.add_userfee_all(fee_name, fee_type,"0", deadline)
            else:
                total = self.amount_entry.get()
                if not total:
                    self.success_label.config(text="Please fill in all fields!")
                    return
                if total == '0':
                    self.success_label.config(text="Total cannot be 0!")
                    return
                deadline_date = self.deadline_entry.get()
                deadline_time = f"{self.hour_entry.get()}:{self.minute_entry.get()}:00"
                if not deadline_date or not self.hour_entry.get() or not self.minute_entry.get(): 
                    self.success_label.config(text="Please fill in all fields!")
                    return
                deadline = f"{deadline_date} {deadline_time}"
                self.db_manager.add_userfee_all(fee_name, fee_type, total, deadline)
            self.success_label.config(text="Fee added successfully!", fg="green")
            popup.after(2000, popup.destroy)

        Button(popup, text="Add",  command=submit_entries, font=("Arial",20)).place(x=170, y=320)
    
    def add1(self):
        popup = Toplevel(self.canvas)
        popup.title("Add Fee to Apartment")
        popup.geometry("400x300")
        popup.resizable(False, False)
         # Create canvas to hold background image
        bg_canvas = Canvas(popup, width=400, height=300, highlightthickness=0)
        bg_canvas.pack(fill="both", expand=True)

        # Load and display background image
        bg_image = Image.open("assets/admin_gui/bg.png")
        bg_image = bg_image.resize((400, 300))
        self.bg_photo = ImageTk.PhotoImage(bg_image) # Save as instance var to prevent garbage collection
        bg_canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create frame to hold other widgets
        content_frame = Frame(popup, bg='#FFFFFF')
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        Label(popup, text="Apartment:", font=("Arial",20), bg="#E1F3FD").place(x=20, y=20)
        apt_list = []
        for apt in self.db_manager.get_all_apts():
            apt_list.append(apt['apartment_code'])
        self.apt_entry = ttk.Combobox(popup, values=apt_list,  font=("Arial",18) )
        self.apt_entry.place(x=170, y=20, height=30, width=200)
        Label(popup, text="Fee Name:", font=("Arial",20), bg="#E1F3FD").place(x=20, y=80)
        fees_list = []
        selected_apt = None
        def on_apt_selected(*args):
            nonlocal selected_apt
            selected_apt = self.apt_entry.get()
            # Get fees this apartment doesn't have yet
            existing_fees = self.db_manager.get_userfee_by_apartment_code(selected_apt)
            existing_fee_names = [fee['fee_name'] for fee in existing_fees]
            all_fees = self.db_manager.get_all_fees()
            fees_list.clear()
            for fee in all_fees:
                if fee['fee_name'] not in existing_fee_names:
                    fees_list.append(fee['fee_name'])
            self.fee_entry['values'] = fees_list

        self.apt_entry.bind("<<ComboboxSelected>>", on_apt_selected)
        
        self.fee_entry = ttk.Combobox(popup, values=fees_list, font=("Arial",18))
        self.fee_entry.place(x=170, y=80, height=30, width=200)

        def on_fee_selected(*args):
            selected_fee = self.fee_entry.get()
            fee_data = self.db_manager.get_fee_by_name(selected_fee)
            if fee_data and fee_data['type'] == 'unrequired':
                self.amount_entry.config(state="disabled")
                self.amount_entry.delete(0, 'end')
                self.amount_entry.insert(0, '0')
            else:
                self.amount_entry.config(state="normal")
                self.amount_entry.delete(0, 'end')

        self.fee_entry.bind("<<ComboboxSelected>>", on_fee_selected)

        Label(popup, text="Total:", font=("Arial",20), bg="#E1F3FD").place(x=20, y=140)
        self.amount_entry = Entry(popup, font=("Arial",20))
        self.amount_entry.place(x=170, y=140,height=30, width=200)

        self.success_label = Label(popup, text="", font=("Arial",20), fg="red", bg="#E1F3FD")
        self.success_label.place(x=50, y=260)

        def submit_entries():
            if not selected_apt or not self.fee_entry.get():
                self.success_label.config(text="Please fill in all fields!")
                return
            apt_name = self.apt_entry.get()
            fee_name = self.fee_entry.get()
            fee_data = self.db_manager.get_fee_by_name(fee_name)
            if fee_data and fee_data['type'] == 'unrequired':
                self.db_manager.add_userfee(apt_name, fee_name, 0, 0, 0)
            if fee_data and fee_data['type'] == 'required':
                total = self.amount_entry.get()
                if not total:
                    self.success_label.config(text="Please fill in all fields!")
                    return
                if total == '0':
                    self.success_label.config(text="Total cannot be 0!")
                    return
                self.db_manager.add_userfee(apt_name, fee_name, total, 0, total)
            
            self.success_label.config(text="Fee added successfully!", fg="green")
            popup.after(2000, popup.destroy)

        Button(popup, text="Add", command=submit_entries, font=("Arial",20)).place(x=170, y=200)

    def new_fee(self):
        popup = Toplevel(self.canvas)
        popup.title("Create New Fee") 
        popup.geometry("400x380")
        popup.resizable(False, False)

        # Create canvas to hold background image
        bg_canvas = Canvas(popup, width=400, height=380, highlightthickness=0)
        bg_canvas.pack(fill="both", expand=True)

        # Load and display background image
        bg_image = Image.open("assets/admin_gui/bg.png")
        bg_image = bg_image.resize((400, 380))
        self.bg_photo = ImageTk.PhotoImage(bg_image) # Save as instance var to prevent garbage collection
        bg_canvas.create_image(0, 0, image=self.bg_photo, anchor="nw")

        # Create frame to hold other widgets
        content_frame = Frame(popup, bg='#FFFFFF')
        content_frame.place(relx=0.5, rely=0.5, anchor="center")
        Label(popup, text="Fee Name:",font=("Arial",20),bg="#E1F3FD").place(x=20, y=20)
        self.fee_name_entry = Entry(popup,  font=("Arial",20))
        self.fee_name_entry.place(x=170, y=20,height=30, width=200)

        Label(popup, text="Type:", font=("Arial",20),bg="#E1F3FD").place(x=20, y=80)
        self.type_entry = ttk.Combobox(popup, values=["Required", "Unrequired"],  font=("Arial",18) )
        self.type_entry.place(x=170, y=80, height=30, width=200)

        Label(popup, text="Deadline:", font=("Arial",20),bg="#E1F3FD").place(x=20, y=140)
        self.deadline_entry = DateEntry(popup,  font=("Arial",20), date_pattern='y-mm-dd')
        self.deadline_entry.place(x=170, y=140,height=30, width=200)

        Label(popup, text="Time:", font=("Arial",20),bg="#E1F3FD").place(x=20, y=200)
        self.hour_entry = ttk.Combobox(popup, values=[f"{i:02d}" for i in range(24)], font=("Arial",18), width=3)
        self.hour_entry.place(x=170, y=200, height=30, width=60)
        self.minute_entry = ttk.Combobox(popup, values=[f"{i:02d}" for i in range(60)], font=("Arial",18), width=3)
        self.minute_entry.place(x=240, y=200, height=30, width=60)
        self.success_label = Label(popup, text="", font=("Arial",20), fg="red",bg="#E1F3FD")
        self.success_label.place(x=50, y=325)

        def submit_entries():
            fee_name = self.fee_name_entry.get()
            fee_type = self.type_entry.get()
            fee_type=fee_type.lower()
            if not fee_name or not fee_type:
                self.success_label.config(text="Please fill in all fields!")
            deadline_date = self.deadline_entry.get()
            deadline_time = f"{self.hour_entry.get()}:{self.minute_entry.get()}:00"
            if not deadline_date or not self.hour_entry.get() or not self.minute_entry.get(): 
                self.success_label.config(text="Please fill in all fields!")
                return
            deadline = f"{deadline_date} {deadline_time}"
            self.db_manager.add_fee(fee_name, deadline, 0, 0, 0, fee_type)
            self.success_label.config(text="Fee added successfully!", fg="green")
            popup.after(2000, popup.destroy)

        Button(popup, text="Add",  command=submit_entries, font=("Arial",20)).place(x=170, y=260)
        

    def show_statistic_electric(self, mode="Electricity"):
        # self.hide_buttons_in_region(220, 141.32812, 792, 579)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image


        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
            220,
            141.32812,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")

        if mode == "Electricity":
            data = self.db_manager.get_electricity_fee_summary()
        elif mode == "Water":
            data = self.db_manager.get_water_fee_summary()
        elif mode == "Service":
            data = self.db_manager.get_service_fee_summary()
        elif mode == "Parking":
            data = self.db_manager.get_parking_fee_summary()
        else:
            data = []


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
        self.tree["columns"] = ("one", "two")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)

        self.tree.heading("#0", text="Month_Year", anchor=tk.W)
        self.tree.heading("one", text="Total_Paid", anchor=tk.W)
        self.tree.heading("two", text="Remaining_Fee", anchor=tk.W)

        # Insert some sample data
        for i in range(len(data)):
            self.tree.insert("", "end", text=f"{data[i]['Month_Year']}", values=(f"{data[i]['Total_Paid']}", f"{data[i]['Remaining_Fee']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)


    def show_statistic_electric(self, mode="Electricity"):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image

        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
            220,
            141.32812,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")

        if mode == "Electricity":
            data = self.db_manager.get_electricity_fee_summary()
        elif mode == "Water":
            data = self.db_manager.get_water_fee_summary()
        elif mode == "Service":
            data = self.db_manager.get_service_fee_summary()
        elif mode == "Parking":
            data = self.db_manager.get_parking_fee_summary()
        else:
            data = []


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
        self.tree["columns"] = ("one", "two")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)

        self.tree.heading("#0", text="Month_Year", anchor=tk.W)
        self.tree.heading("one", text="Total_Paid", anchor=tk.W)
        self.tree.heading("two", text="Remaining_Fee", anchor=tk.W)

        # Insert some sample data
        for i in range(len(data)):
            self.tree.insert("", "end", text=f"{data[i]['Month_Year']}", values=(f"{data[i]['Total_Paid']}", f"{data[i]['Remaining_Fee']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)


    def show_statistic_electric(self, mode="Electricity"):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image

        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
            220,
            141.32812,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")

        if mode == "Electricity":
            data = self.db_manager.get_electricity_fee_summary()
        elif mode == "Water":
            data = self.db_manager.get_water_fee_summary()
        elif mode == "Service":
            data = self.db_manager.get_service_fee_summary()
        elif mode == "Parking":
            data = self.db_manager.get_parking_fee_summary()
        else:
            data = []


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
        self.tree["columns"] = ("one", "two")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)

        self.tree.heading("#0", text="Month_Year", anchor=tk.W)
        self.tree.heading("one", text="Total_Paid", anchor=tk.W)
        self.tree.heading("two", text="Remaining_Fee", anchor=tk.W)

        # Insert some sample data
        for i in range(len(data)):
            self.tree.insert("", "end", text=f"{data[i]['Month_Year']}", values=(f"{data[i]['Total_Paid']}", f"{data[i]['Remaining_Fee']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)

    def show_statistic_water(self, mode="Water"):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image


        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
            220,
            141.32812,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")

        if mode == "Electricity":
            data = self.db_manager.get_electricity_fee_summary()
        elif mode == "Water":
            data = self.db_manager.get_water_fee_summary()
        elif mode == "Service":
            data = self.db_manager.get_service_fee_summary()
        elif mode == "Parking":
            data = self.db_manager.get_parking_fee_summary()
        else:
            data = []


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
        self.tree["columns"] = ("one", "two")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)

        self.tree.heading("#0", text="Month_Year", anchor=tk.W)
        self.tree.heading("one", text="Total_Paid", anchor=tk.W)
        self.tree.heading("two", text="Remaining_Fee", anchor=tk.W)

        # Insert some sample data
        for i in range(len(data)):
            self.tree.insert("", "end", text=f"{data[i]['Month_Year']}", values=(f"{data[i]['Total_Paid']}", f"{data[i]['Remaining_Fee']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)


    def show_statistic_parking(self, mode="Parking"):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image

        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
            220,
            141.32812,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")

        if mode == "Electricity":
            data = self.db_manager.get_electricity_fee_summary()
        elif mode == "Water":
            data = self.db_manager.get_water_fee_summary()
        elif mode == "Service":
            data = self.db_manager.get_service_fee_summary()
        elif mode == "Parking":
            data = self.db_manager.get_parking_fee_summary()
        else:
            data = []


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
        self.tree["columns"] = ("one", "two")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)

        self.tree.heading("#0", text="Month_Year", anchor=tk.W)
        self.tree.heading("one", text="Total_Paid", anchor=tk.W)
        self.tree.heading("two", text="Remaining_Fee", anchor=tk.W)

        # Insert some sample data
        for i in range(len(data)):
            self.tree.insert("", "end", text=f"{data[i]['Month_Year']}", values=(f"{data[i]['Total_Paid']}", f"{data[i]['Remaining_Fee']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)


    def show_statistic_service(self, mode="Service"):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image

        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
            220,
            141.32812,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")

        if mode == "Electricity":
            data = self.db_manager.get_electricity_fee_summary()
        elif mode == "Water":
            data = self.db_manager.get_water_fee_summary()
        elif mode == "Service":
            data = self.db_manager.get_service_fee_summary()
        elif mode == "Parking":
            data = self.db_manager.get_parking_fee_summary()
        else:
            data = []


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
        self.tree["columns"] = ("one", "two")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)

        self.tree.heading("#0", text="Month_Year", anchor=tk.W)
        self.tree.heading("one", text="Total_Paid", anchor=tk.W)
        self.tree.heading("two", text="Remaining_Fee", anchor=tk.W)

        # Insert some sample data
        for i in range(len(data)):
            self.tree.insert("", "end", text=f"{data[i]['Month_Year']}", values=(f"{data[i]['Total_Paid']}", f"{data[i]['Remaining_Fee']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)
        # self.generate_visualization(data)

    def generate_visualization(self, data):
        # Create a DataFrame
        df = pd.DataFrame(data)

        # Create a figure and axis
        fig, ax = plt.subplots(figsize=(10, 6))

        # Hide axes
        ax.xaxis.set_visible(False)
        ax.yaxis.set_visible(False)
        ax.set_frame_on(False)

        # Create a table
        table = ax.table(
            cellText=df.values,
            colLabels=df.columns,
            cellLoc='center',
            loc='center'
        )

        table.auto_set_font_size(False)
        table.set_fontsize(12)
        table.scale(1.2, 1.2)

        ax.set_title("Fee Summary", fontsize=14, weight="bold")

        # Save the figure
        plt.savefig("assets/admin_gui/fee_summary.png")
        plt.close()
        self.show_visualization()


    def statistic(self):
        self.hide_buttons_in_region(190, 79.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7_red.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")

        self.canvas.create_text(
            316.25 + 70 + 70,
            188.0 - 30,
            anchor="nw",
            text="Choose a statistics option",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )


        self.button_image_9 = PhotoImage(
            file="assets/frame4/button_9.png")
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.show_statistic_electric,
            relief="flat"
        )
        self.button_9.place(
            x=429.25 + 70,
            y=204.0,
            width=245.0,
            height=52.0
        )



        self.button_image_10 = PhotoImage(
            file="assets/frame4/button_10.png")
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.show_statistic_water,
            relief="flat"
        )
        self.button_10.place(
            x=429.25 + 70,
            y=269.0,
            width=245.0,
            height=52.0
        )

        self.button_image_11 = PhotoImage(
            file="assets/frame4/button_11.png")
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.show_statistic_service,
            relief="flat"
        )
        self.button_11.place(
            x=430.25 + 70,
            y=335.0,
            width=245.0,
            height=52.0
        )

        self.button_image_12 = PhotoImage(
            file="assets/frame4/button_12.png")
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.show_statistic_parking,
            relief="flat"
        )
        self.button_12.place(
            x=430.25 + 70,
            y=408.0,
            width=245.0,
            height=52.0
        )

        self.button_image_13 = PhotoImage(
            file="assets/frame4/button_14.png")
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.show_voluntary_statistic,
            relief="flat"
        )
        self.button_13.place(
            x=429.25 + 70,
            y=550.0,
            width=245.0,
            height=52.0
        )

        self.button_image_14 = PhotoImage(
            file="assets/frame4/button_13.png")
        self.button_14 = Button(
            image=self.button_image_14,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.show_housing_statistic,
            relief="flat"
        )
        self.button_14.place(
            x=429.25 + 70,
            y=479.0,
            width=245.0,
            height=52.0
        )


        self.button_image_15 = PhotoImage(
            file="assets/frame4/button_15.png")
        self.button_15 = Button(
            image=self.button_image_15,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.show_visualization,
            relief="flat"
        )
        self.button_15.place(
            x=429.25 + 70,
            y=625.0,
            width=245.0,
            height=52.0
        )

    def show_voluntary_statistic(self, mode="Service"):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image

        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
            220,
            141.32812,
            1012.5,
            720,
            fill="#FFFFFF",
            outline="#000000")

        data = self.db_manager.get_voluntary_fee_summary()


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
        self.tree["columns"] = ("one", "two")
        self.tree.column("#0", width=25, minwidth=25)
        self.tree.column("one", width=225, minwidth=225)
        self.tree.column("two", width=50, minwidth=50)

        self.tree.heading("#0", text="Month_Year", anchor=tk.W)
        self.tree.heading("one", text="Voluntary_Fee", anchor=tk.W)
        self.tree.heading("two", text="Total_paid", anchor=tk.W)
                          
        # Insert some sample data
        for i in range(len(data)):
            self.tree.insert("", "end", text=f"{data[i]['Month_Year']}", values=(f"{data[i]['Volutary_fee']}", f"{data[i]['Total_Paid']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)
        # self.generate_visualization(data)
        

    def show_housing_statistic(self):
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7_red.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
        if self.tree:
            self.tree.place_forget()

        self.canvas.create_rectangle(
        220,
        141.32812,
        1012.5,
        720,
        fill="#FFFFFF",
        outline="#000000")



        self.canvas.create_text(
            239.25,
            86.0 + 65,
            anchor="nw",
            text="Enter Apartment Code:",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.entry_image_1 = PhotoImage(
            file="assets/admin_gui/entry_1.png")
        self.entry_bg_1 = self.canvas.create_image(
            788.75,
            115.0 + 65,
            image=self.entry_image_1
        )
        self.entry_1 = Entry(
            self.root,
            bd=0,
            bg="#ffffff",
            fg="#000716",
            highlightthickness=0,
            font=("Inter", 20)
        )
        self.entry_1.place(
            x=647.75,
            y=98.0 + 65,
            width=272.0,
            height=33.0
        )


        self.button_image_9 = PhotoImage(
            file="assets/admin_gui/Submit_button.png")
        self.button_9 = Button(
            self.root,
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.submit_housing_statistic,
            relief="flat"
        )
        self.button_9.place(
            x=418.25,
            y=226.0,
            width=160.0,
            height=50.0
        )

        self.button_image_10 = PhotoImage(
            file="assets/admin_gui/Back_button.png")
        self.button_10 = Button(
            self.root,
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            background="#ffffff",
            activebackground="#ffffff",
            command=self.statistic,
            relief="flat"
        )
        self.button_10.place(
            x=629.25,
            y=226.0,
            width=160.0,
            height=50.0
        )

        self.canvas.create_rectangle(
            220,
            360-65,
            1012.5,
            720,
            fill="#123456",
            outline="")
        
    def submit_housing_statistic(self):
        apartment_code = self.entry_1.get()
        # fee_name = self.entry_2.get()
        data = self.db_manager.get_userfee_by_apartment_code(apartment_code)
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
        self.tree["columns"] = ("one", "two")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)

        self.tree.heading("#0", text="Fee_name", anchor=tk.W)
        self.tree.heading("one", text="Total_Paid", anchor=tk.W)
        self.tree.heading("two", text="Remaining_Fee", anchor=tk.W)

        # Insert some sample data
        for i in range(len(data)):
            self.tree.insert("", "end", text=f"{data[i]['fee_name']}", values=(f"{data[i]['paid']}", f"{data[i]['remain']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=360-65+10, width=792, height=360)
        # self.generate_visualization(data)
        







        
    def log_out(self):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        self.root.show_login_frame()
    
    def on_double_click(self, event):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
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
            if isinstance(widget, (tk.Button, tk.Entry, tk.Text,ttk.Scrollbar)):
                hide_widget(widget)
            elif isinstance(widget, tk.Canvas):
                for canvas_widget in widget.winfo_children():
                    if isinstance(canvas_widget, (tk.Button, tk.Entry, tk.Text)):
                        hide_widget(canvas_widget)


    def generate_pie_charts(self):
        # Fetch data for each fee type
        electricity_data = self.db_manager.get_electricity_fee_summary()
        water_data = self.db_manager.get_water_fee_summary()
        service_data = self.db_manager.get_service_fee_summary()
        parking_data = self.db_manager.get_parking_fee_summary()

        # Prepare data for pie charts
        fee_types = {
            "Electricity": electricity_data,
            "Water": water_data,
            "Service": service_data,
            "Parking": parking_data
        }

        # Define colors for the pie charts
        colors = ["#4CAF50", "#FF9800"]  # Green and Orange

        # Create a figure with GridSpec layout
        fig = plt.figure(figsize=(12, 10))
        gs = GridSpec(3, 2, figure=fig, height_ratios=[3, 3, 1])

        # Plot each fee type in a 2x2 grid
        for idx, (fee_type, data) in enumerate(fee_types.items()):
            ax = fig.add_subplot(gs[idx // 2, idx % 2])
            total_paid = sum(row["Total_Paid"] for row in data)
            remaining_fee = sum(row["Remaining_Fee"] for row in data)
            
            wedges, texts, autotexts = ax.pie(
                [total_paid, remaining_fee],
                labels=["Total Paid", "Remaining Fee"],
                autopct='%1.1f%%',
                colors=colors,
                textprops=dict(color="w")
            )
            
            # Beautify pie chart
            for text in texts:
                text.set_fontsize(10)
            for autotext in autotexts:
                autotext.set_fontsize(12)
                autotext.set_weight("bold")
            
            ax.set_title(fee_type, fontsize=14, weight="bold")

        # Add a legend to the bottom
        ax_legend = fig.add_subplot(gs[2, :])
        ax_legend.axis("off")
        labels = ["Total Paid", "Remaining Fee"]
        handles = [plt.Line2D([0], [0], marker='o', color='w', label=label,
                               markerfacecolor=color, markersize=10) for label, color in zip(labels, colors)]
        ax_legend.legend(handles=handles, loc="center", fontsize=12, title="Legend")

        # Set the main title
        fig.suptitle("Fee Summary Visualization", fontsize=16, weight="bold")

        # Save and close the figure
        plt.tight_layout(rect=[0, 0, 1, 0.95])
        plt.savefig("assets/admin_gui/fee_summary.png")
        plt.close()


    def show_visualization(self):
        self.generate_pie_charts()
        # Use OpenCV to open and display the image
        img = cv2.imread("assets/admin_gui/fee_summary.png")
        resized_img = cv2.resize(img, (600, 500))
        cv2.imshow("Fee Summary Visualization", resized_img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def send_noti(self):
        self.hide_buttons_in_region(190, 79.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4_red.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
        if self.tree:
            self.tree.place_forget()

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
        self.hide_buttons_in_region(190, 79.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/edit_admin.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4_red.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
        if self.tree:
            self.tree.place_forget()

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
        self.send_noti_img = self.send_noti_img.resize((396, 60))
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
            width=395,
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
        self.tree.column("one", width=240, minwidth=100)
        self.tree.column("two", width=0, minwidth=0,stretch=tk.NO)
        self.tree.column("three", width=80, minwidth=100)

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
        



        
    
