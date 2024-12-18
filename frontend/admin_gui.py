from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label
from tkinter import ttk
from PIL import Image, ImageTk
import tkinter as tk
from tkinter import PhotoImage, Canvas
from backend.weather import get_address_and_weather
from backend.auth import AuthManager
from frontend.root_gui import RootGUI  # Import RootGUI to extend it
import matplotlib.pyplot as plt
from matplotlib.gridspec import GridSpec
import cv2
import pandas as pd 
from os import environ
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
# database ready

class AdminGUI(Tk):
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
            text="Hello, Admin  ",
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
            file="assets/admin_gui/button_2.png")
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

        self.pay_img= PhotoImage(
            file="assets/admin_gui/button_6.png")
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
            y=487.265625,
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
            y=553.359375,
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
            y=626.48431396,
            width=170.859375,
            height=42.890625
            
        )


        self.hide_buttons_in_region(1,1,1,1)

        self.tree = None
        self.show_home()

    def show_home(self):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1_red.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
        if self.tree:
            self.tree.place_forget()
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)

        self.canvas.create_text(
            424.25,
            147.0,
            anchor="nw",
            text="This is just an example.  \nAbsolutely don’t deploy!",
            fill="#2E0DEB",
            font=("Inter", 32 * -1)
        )
        self.sample_img = PhotoImage(
            file="assets/admin_gui/image_3.png")
        self.sample_image_element = self.canvas.create_image(
            609.25,
            451.0,
            image=self.sample_img
        )

        
    def view_admin(self, editable=True):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_2_red.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_7.png")
        self.statistic_button.config(image=new_image)
        self.statistic_button.image = new_image
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
            self.tree.bind("<Double-1>", lambda event: self.edit_double_click(event, 'admin'))

    def view_user(self, editable=True):
        # Hide buttons in the specified region
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)

        # Update button images
        button_images = [
            ("assets/admin_gui/button_1.png", self.home_button),
            ("assets/admin_gui/button_2.png", self.view_admin_button),
            ("assets/admin_gui/button_3_red.png", self.view_user_button),
            ("assets/admin_gui/button_4.png", self.noti_button),
            ("assets/admin_gui/button_5.png", self.edit_fee_button),
            ("assets/admin_gui/button_6.png", self.pay_button),
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



    from tkinter import Canvas


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
        old_username = user_details['username']

        # Create a top-level window for editing
        edit_window = tk.Toplevel(self.root)
        edit_window.title("Edit User")
        edit_window.geometry("1400x700")
        edit_window.protocol("WM_DELETE_WINDOW", lambda: None)
        edit_window.attributes("-toolwindow", True)

        # Use grid for the background canvas
        canvas = Canvas(edit_window, width=1400, height=700)
        canvas.grid(row=0, column=0, rowspan=10, columnspan=2, sticky="nsew")

        # Load and display the background image
        bg_image = Image.open("assets/fun_time/christmas2.png")
        bg_image = bg_image.resize((1400, 700), Image.Resampling.LANCZOS)
        bg_image_tk = ImageTk.PhotoImage(bg_image)
        canvas.create_image(0, 0, anchor="nw", image=bg_image_tk)

        font_large = ("Arial", 16)
        labels = ["Full Name", "Username", "Password", "Role", apt_high, "Email", "Phone Number"]
        label_lower = ['full_name', 'username', 'password', 'account_type', 'apartment_code', 'email', 'phone_number']
        entries = {}

        # Add labels and entries on top of the canvas
        for idx, label in enumerate(labels):
            tk.Label(edit_window, text=label + ":", font=font_large, bg='pink', fg='black').grid(
                row=idx + 1, column=0, padx=(20, 10), pady=5, sticky="e"
            )
            entry = tk.Entry(edit_window, width=25, font=font_large, bg="lightgreen", fg="black", relief="flat")
            entry_element = user_details.get(label_lower[idx], "")
            entry.insert(0, entry_element)
            entries[label] = entry
            entry.grid(row=idx + 1, column=1, padx=(10, 20), pady=5, sticky="w")

        def save_changes():
            new_values = {label: entries[label].get() for label in labels}
            for label in labels:
                if new_values[label] == "":
                    new_values[label] = None
            self.db_manager.update_user(
                old_username, new_values["Password"], new_values["Role"],
                new_values["Full Name"], new_values["Phone Number"],
                new_values[apt_high], new_values["Email"]
            )
            self.tree.item(selected_item, values=(new_values["Full Name"], new_values[apt_high]))
            pygame.mixer.music.stop() 
            edit_window.destroy()
        def cancel_changes():
            pygame.mixer.music.stop()  # Stop the music
            edit_window.destroy()
        def delete_record():
            confirmation = tk.messagebox.askyesno("Delete Record", "Are you sure you want to delete this record?")
            if confirmation:
                self.db_manager.delete_user(old_username)  
                self.tree.delete(selected_item)
                pygame.mixer.music.stop()
                edit_window.destroy()

        # Add Save and Cancel buttons
        tk.Button(edit_window, text="Save", command=save_changes, width=12, bg="lightgreen", font=("Arial", 12)).grid(
            row=len(labels) + 2, column=0, padx=5
        )
        tk.Button(edit_window, text="Delete", command=delete_record, width=12, bg="lightgreen", font=("Arial", 12)).grid(
            row=len(labels) + 3, column=0, padx=5
        )
        tk.Button(edit_window, text="Cancel", command=cancel_changes, width=12, bg="lightgreen", font=("Arial", 12)).grid(
            row=len(labels) + 2, column=1, padx=5
        )

        # Keep a reference to the background image
        edit_window.bg_image_tk = bg_image_tk


    def edit_fee(self):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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

    def pay(self):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6_red.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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

    def show_statistic_electric(self, mode="Electricity"):
        # self.hide_buttons_in_region(220, 141.32812, 792, 579)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image



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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image

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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
            if isinstance(widget, (tk.Button, tk.Entry, tk.Text)):
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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
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
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        



        
    
