from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from backend.weather import get_address_and_weather
class AbstractAdminGUI:
    def __init__(self, root, user):
        self.root = root
        self.user = user
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
            71.71875,
            1012.5,
            141.328125,
            fill="#D9D9D9",
            outline="")

        self.canvas.create_rectangle(
            196.171875,
            0.0,
            1012.5,
            71.71875,
            fill="#FFFFFF",
            outline="")

        self.hello_text_field = self.canvas.create_text(
            301.640625,
            18.984375,
            anchor="nw",
            text="Hello, Admin  ",
            fill="#000000",
            font=("Inter Bold", 28 * -1)
        )

        self.avatar_img = PhotoImage(
            file="assets/admin_gui/image_1.png")
        self.avatar = self.canvas.create_image(
            255.21875,
            35.765625,
            image=self.avatar_img
        )

        self.canvas.create_rectangle(
            772.03125,
            0.0,
            1012.5,
            71.71875,
            fill="#130DBA",
            outline="")

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
            141.32810974121094,
            1012.5,
            719.9999847412109,
            fill="#FFFFFF",
            outline="")

        self.home_img = PhotoImage(
            file="assets/admin_gui/button_1.png")
        self.home_button = Button(
            image=self.home_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.show_home,
            relief="flat"
        )
        self.home_button.place(
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
        self.thong_ke_button = Button(
            image=self.thong_ke_img,
            borderwidth=0,
            highlightthickness=0,
            command=self.thong_ke,
            relief="flat"
        )
        self.thong_ke_button.place(
            x=18.281219482421875,
            y=626.48431396,
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
            y=553.359375,
            width=170.859375,
            height=42.890625
            
        )

        self.phong_bat_img = PhotoImage(
            file="assets/admin_gui/image_2.png")
        self.phong_bat = self.canvas.create_image(
            98.0,
            35.0,
            image=self.phong_bat_img
        )
        ######### address and temperature ###############
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
    def show_home(self):
        pass
    def view_admin(self):
        pass
    def view_user(self):
        pass
    def manage_fee(self):
        pass
    def edit_fee(self):
        pass
    def pay(self):
        pass
    def thong_ke(self):
        pass
    def log_out(self):
        pass


        
    
