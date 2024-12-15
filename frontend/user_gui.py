from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label
from tkinter import ttk
import tkinter as tk
from backend.weather import get_address_and_weather
from backend.db import DBManager
from backend.auth import AuthManager
from PIL import Image, ImageDraw, ImageFont
from PIL import ImageTk

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
        
        self.image_image_4 = PhotoImage(
            file="assets/user_gui/image_4.png")
        self.image_4 = self.canvas.create_image(
            98.25,
            560.0,
            image=self.image_image_4
        )

        self.profile_img = PhotoImage(
            file="assets/user_gui/button_4.png")
        self.profile_button = Button(
            image=self.profile_img,
            borderwidth=0,
            highlightthickness=0,
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
            command=self.pay,
            relief="flat"
        )
        self.pay_button.place(
            x=18.281219482421875,
            y=261.5625,
            width=170.859375,
            height=42.890625
        )

        self.log_out_img = PhotoImage(
            file="assets/user_gui/button_6.png")
        self.log_out_button= Button(
            image=self.log_out_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.log_out,
            relief="flat"
        )
        self.log_out_button.place(
            x=18.281219482421875,
            y=336.796875,
            width=170.859375,
            height=42.890625
            
        )
        self.tree = None
        self.show_profile()
    
    def show_noti(self):
        pass

    def show_profile(self):
        new_image = PhotoImage(file="assets/user_gui/button_4.png")
        self.profile_button.config(image=new_image)
        self.profile_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_7.png")
        self.view_fee_button.config(image=new_image)
        self.view_fee_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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
        
    def view_fee(self):
        new_image = PhotoImage(file="assets/user_gui/button_4.png")
        self.profile_button.config(image=new_image)
        self.profile_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_7.png")
        self.view_fee_button.config(image=new_image)
        self.view_fee_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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

        apt_code = self.user['apartment_code']
        fee_list = self.db_manager.view_fee_by_apartment_code(apt_code)


        # Create a Treeview
        style = ttk.Style()
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
        self.tree = ttk.Treeview(self.root, style="Custom.Treeview")
        self.tree["columns"] = ("one", "two", "three")
        self.tree.column("#0", width=100, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=100, minwidth=100)
        self.tree.column("three", width=100, minwidth=100)

        self.tree.heading("#0", text="Fee Name", anchor=tk.W)
        self.tree.heading("one", text="Total", anchor=tk.W)
        self.tree.heading("two", text="Paid", anchor=tk.W)
        self.tree.heading("three", text="Remain", anchor=tk.W)

        # Insert some sample data
        for i in range(len(fee_list)):
            self.tree.insert("", "end", text=f"{fee_list[i]['fee_name']}", values=(f"{fee_list[i]['total']}", f"{fee_list[i]['paid']}", f"{fee_list[i]['remain']}"))

        # Place the Treeview on top of the Canvas
        self.tree.place(x=220, y=141, width=792, height=579)

        # Bind double-click event
        self.tree.bind("<Double-1>", self.on_double_click)

    def pay(self):
        new_image = PhotoImage(file="assets/user_gui/button_4.png")
        self.profile_button.config(image=new_image)
        self.profile_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_7.png")
        self.view_fee_button.config(image=new_image)
        self.view_fee_button.image = new_image
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
        self.pay_button.config(image=new_image)
        self.pay_button.image = new_image
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

        self.entry_image_2 = PhotoImage(
            file="assets/user_gui/entry_3.png")
        self.entry_bg_2 = self.canvas.create_image(
            749.25,
            259.5,
            image=self.entry_image_2
        )
        self.fee_name_entry = Entry(
            bd=0,
            bg="#D4FC79",
            fg="#000716",
            highlightthickness=0,
            font=("Arial", 20)
        )

        self.fee_name_entry.place(
            x=610.25,
            y=242.0,
            width=278.0,
            height=36.0
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
        for widget in self.root.winfo_children():
            if isinstance(widget, (tk.Button,tk.Entry)):
                widget_x = widget.winfo_x()
                widget_y = widget.winfo_y()
                if x1 <= widget_x <= x2 and y1 <= widget_y <= y2:
                    widget.place_forget()

    def find_fee(self):
        fee_name= self.fee_name_entry.get()
        apartment_code= self.user['apartment_code']
        user_fee_info = self.db_manager.user_fee_info(apartment_code, fee_name)
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
        self.canvas.create_text(
            500.25,
            530.0,
            text=feename,
            fill="#000000",
            anchor="nw",
            font=("Arial", 20)
        )
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
        if (money_paid<1000 or money_paid>money_remain or money_paid%1000!=0):
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

            self.finish_img = PhotoImage(
                file="assets/user_gui/button_1.png")
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
                y=650,
                width=200.0,
                height=60.0
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

        self.continue_img = PhotoImage(
            file="assets/user_gui/button_1.png")
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
            x=500,
            y=650,
            width=200.0,
            height=60.0
        )

        self.success_img = Image.open("assets/user_gui/success.png")
        self.success_img = self.success_img.resize((400, 400))
        self.success_img = ImageTk.PhotoImage(self.success_img)
        self.canvas.create_image(
            600.75,
            400.0,
            image=self.success_img)



    

