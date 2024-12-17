from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, Label, Scrollbar, RIGHT, Y, LEFT, BOTH
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

        self.noti_img = PhotoImage(
            file="assets/user_gui/button_5.png")
        self.noti_button= Button(
            image=self.noti_img,
            borderwidth=0,
            highlightthickness=0,
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
            command=self.log_out,
            relief="flat"
        )
        self.log_out_button.place(
            x=18.281219482421875,
            y=411.796875,
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
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
        self.noti_button.config(image=new_image)
        self.noti_button.image = new_image
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
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
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
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
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
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
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
        self.send_button_img = self.send_button_img.resize((120, 30))
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
            width=123.0,
            height=33.0
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
            self.canvas.create_text(
                350,
                290.0,
                anchor="nw",
                text="Notification sent",
                fill="green",
                font=("Arial", 20))

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
        new_image = PhotoImage(file="assets/user_gui/button_5.png")
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
        style.configure("Custom.Treeview", bordercolor="black", borderwidth=2)
        self.tree = ttk.Treeview(self.root, style="Custom.Treeview")
        self.tree["columns"] = ( "one", "two", "three")
        self.tree.column("#0", width=50, minwidth=100)
        self.tree.column("one", width=100, minwidth=100)
        self.tree.column("two", width=150, minwidth=100)
        self.tree.column("three", width=100, minwidth=100)

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
        