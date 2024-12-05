from pathlib import Path
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from frontend.abstract_admin_gui import AbstractAdminGUI
class AdminGUI(AbstractAdminGUI):
    def __init__(self, root):
        super().__init__(root)
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