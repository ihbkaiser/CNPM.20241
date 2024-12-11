from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from frontend.abstract_admin_gui import AbstractAdminGUI
class AdminGUI(AbstractAdminGUI):
    def __init__(self, root, user):
        super().__init__(root, user)
        self.show_home()
    def show_home(self):
        # self.home_img = PhotoImage(
        #     file="assets/admin_gui/button_1.png")
        # self.home_button = Button(
        #     image=self.home_img,
        #     borderwidth=0,
        #     highlightthickness=0,
        #     command=self.show_home,
        #     relief="flat"
        # )
        self.canvas.delete(self.hello_text_field)
        self.canvas.create_text(
            301.640625,
            18.984375,
            anchor="nw",
            text=f"Hello, Admin {self.user['username']}  ",
            fill="#000000",
            font=("Inter Bold", 28 * -1)
        )
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