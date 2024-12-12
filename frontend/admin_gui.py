from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label
from tkinter import ttk
import tkinter as tk
from backend.weather import get_address_and_weather
from backend.auth import AuthManager
from frontend.root_gui import RootGUI  # Import RootGUI to extend it

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
            fill="#D9D9D9",
            outline="")
        
        self.canvas.create_rectangle(
            196.171875,
            71.71875,
            220,
            720,
            fill="#D9D9D9",
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
            command=self.view_user,
            relief="flat"
        )
        self.view_user_button.place(
            x=18.281219482421875,
            y=261.5625,
            width=170.859375,
            height=42.890625
        )

        self.manage_fees_img = PhotoImage(
            file="assets/admin_gui/button_4.png")
        self.manage_fees_button = Button(
            image=self.manage_fees_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.manage_fee,
            relief="flat"
        )
        self.manage_fees_button.place(
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
            command=self.log_out,
            relief="flat"
        )
        self.log_out_button.place(
            x=12.65625,
            y=626.48431396,
            width=170.859375,
            height=42.890625
            
        )

        self.button_visual = PhotoImage(
            file="assets/admin_gui/Visualization.png")
        self.visual = Button(
            image=self.button_visual,
            borderwidth=0,
            highlightthickness=0,
            command=lambda: print("button_9 clicked"),
            relief="flat"
        )
        self.visual.place(
            x=704.25,
            y=86.0,
            width=235.0,
            height=39.0
        )
        self.hide_buttons_in_region(1,1,1,1)

        self.tree = None
        self.show_home()

    def show_home(self):
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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

        
    def view_admin(self):
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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

        # Create a Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
        self.tree = ttk.Treeview(self.root, style="Custom.Treeview")
        self.tree["columns"] = ("one", "two", "three")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)
        self.tree.column("three", width=100, minwidth=100)

        self.tree.heading("#0", text="ID", anchor=tk.W)
        self.tree.heading("one", text="Column 1", anchor=tk.W)
        self.tree.heading("two", text="Column 2", anchor=tk.W)
        self.tree.heading("three", text="Column 3", anchor=tk.W)

        # Insert some sample data
        for i in range(10):
            self.tree.insert("", "end", text=f"Item {i+1}", values=(f"A{i+1}", f"B{i+1}", f"C{i+1}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)

        # Bind double-click event
        self.tree.bind("<Double-1>", self.on_double_click)

    def view_user(self):
        self.hide_buttons_in_region(220, 141.32812, 1012, 720)
        new_image = PhotoImage(file="assets/admin_gui/button_1.png")
        self.home_button.config(image=new_image)
        self.home_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_2.png")
        self.view_admin_button.config(image=new_image)
        self.view_admin_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_3_red.png")
        self.view_user_button.config(image=new_image)
        self.view_user_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_4.png")
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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

        # Create a Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
        self.tree = ttk.Treeview(self.root, style="Custom.Treeview")
        self.tree["columns"] = ("one", "two", "three")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)
        self.tree.column("three", width=100, minwidth=100)

        self.tree.heading("#0", text="ID", anchor=tk.W)
        self.tree.heading("one", text="Column 1", anchor=tk.W)
        self.tree.heading("two", text="Column 2", anchor=tk.W)
        self.tree.heading("three", text="Column 3", anchor=tk.W)

        # Insert some sample data
        for i in range(10):
            self.tree.insert("", "end", text=f"Item {i+1}", values=(f"A{i+1}", f"B{i+1}", f"C{i+1}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)

        # Bind double-click event
        self.tree.bind("<Double-1>", self.on_double_click)

    def manage_fee(self):
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
        new_image = PhotoImage(file="assets/admin_gui/button_4_red.png")
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_5.png")
        self.edit_fee_button.config(image=new_image)
        self.edit_fee_button.image = new_image
        new_image = PhotoImage(file="assets/admin_gui/button_6.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image

        new_image = PhotoImage(file="assets/admin_gui/Visualization.png")
        self.visual.config(image=new_image)
        self.visual.image = new_image



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
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
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


    def statistic(self):
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
        self.manage_fees_button.config(image=new_image)
        self.manage_fees_button.image = new_image
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
            376.25,
            188.0,
            anchor="nw",
            text="Choose a statistics option",
            fill="#000000",
            font=("Inter Bold", 30 * -1)
        )

        self.button_image_9 = PhotoImage(
            file="assets/admin_gui/button_9.png")
        self.button_9 = Button(
            image=self.button_image_9,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_statistic_electric,
            relief="flat"
        )
        self.button_9.place(
            x=432.25,
            y=238.0,
            width=272.0,
            height=49.0
        )

        self.button_image_10 = PhotoImage(
            file="assets/admin_gui/button_10.png")
        self.button_10 = Button(
            image=self.button_image_10,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_statistic_water,
            relief="flat"
        )
        self.button_10.place(
            x=432.25,
            y=311.0,
            width=272.0,
            height=49.0
        )

        self.button_image_11 = PhotoImage(
            file="assets/admin_gui/button_11.png")
        self.button_11 = Button(
            image=self.button_image_11,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_statistic_service,
            relief="flat"
        )
        self.button_11.place(
            x=432.25,
            y=390.0,
            width=272.0,
            height=49.0
        )

        self.button_image_12 = PhotoImage(
            file="assets/admin_gui/button_12.png")
        self.button_12 = Button(
            image=self.button_image_12,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_statistic_parking,
            relief="flat"
        )
        self.button_12.place(
            x=432.25,
            y=468.0,
            width=272.0,
            height=49.0
        )

        self.button_image_13 = PhotoImage(
            file="assets/admin_gui/button_13.png")
        self.button_13 = Button(
            image=self.button_image_13,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_statistic_parking,
            relief="flat"
        )
        self.button_13.place(
            x=432.25,
            y=547.0,
            width=272.0,
            height=49.0
        )


        
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
        self.visual.place_forget()
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Button):
                widget_x = widget.winfo_x()
                widget_y = widget.winfo_y()
                if x1 <= widget_x <= x2 and y1 <= widget_y <= y2:
                    widget.place_forget()



        
    
