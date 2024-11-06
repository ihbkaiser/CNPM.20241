import customtkinter as ctk
from tkinter import messagebox, ttk, simpledialog, Toplevel, Label, Entry, Button
from ttkwidgets.autocomplete import AutocompleteCombobox
from tkcalendar import Calendar
from datetime import datetime
from backend.fee_db import FeeTable

class FeeGUI(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Fee Management")
        self.geometry("600x600")
        self.configure(bg_color='#f0f0f0')

        self.fee_table = FeeTable()

        # Create initial widgets
        self.create_initial_widgets()

    def create_initial_widgets(self):
        # Buttons
        button_style = {
            'fg_color': '#4CAF50',
            'text_color': 'white',
            'font': ('Arial', 12),
            'width': 200,
            'height': 40
        }

        self.view_fees_button = ctk.CTkButton(
            self, text="View All Fees", command=self.show_view_widgets, **button_style)
        self.view_fees_button.pack(pady=10)

        self.payment_button = ctk.CTkButton(
            self, text="Payment", command=self.show_payment_widgets, **button_style)
        self.payment_button.pack(pady=10)

        self.exit_button = ctk.CTkButton(
            self, text="Exit", command=self.exit_app, **button_style)
        self.exit_button.pack(pady=10)

    def show_view_widgets(self):
        # Clear all widgets
        for widget in self.winfo_children():
            widget.pack_forget()

        # Month/Year filter
        self.month_year_label = ctk.CTkLabel(self, text="Select Month and Year:")
        self.month_year_label.pack(pady=5)

        self.month_var = ctk.StringVar(value=str(int(datetime.now().strftime("%m"))))
        self.year_var = ctk.StringVar(value=datetime.now().strftime("%Y"))

        self.month_menu = ctk.CTkOptionMenu(
            self, variable=self.month_var, values=[str(i) for i in range(1, 13)])
        self.month_menu.pack(pady=5)

        self.year_menu = ctk.CTkOptionMenu(
            self, variable=self.year_var, values=[str(i) for i in range(2000, 2100)])
        self.year_menu.pack(pady=5)

        # Checkbox to show all fees
        self.show_all_var = ctk.BooleanVar()
        self.show_all_check = ctk.CTkCheckBox(
            self, text="Show all fees of all months", variable=self.show_all_var, command=self.toggle_month_year_selection)
        self.show_all_check.pack(pady=5)

        # View Fees Button
        button_style = {
            'fg_color': '#4CAF50',
            'text_color': 'white',
            'font': ('Arial', 12),
            'width': 200,
            'height': 40
        }

        self.view_fees_button = ctk.CTkButton(
            self, text="View Fees", command=self.view_fees, **button_style)
        self.view_fees_button.pack(pady=10)

        # Treeview for displaying fees
        self.fees_tree = ttk.Treeview(self, columns=("name", "month"), show="headings")
        self.fees_tree.heading("name", text="Fee Name")
        self.fees_tree.heading("month", text="Month/Year")
        self.fees_tree.pack(pady=10, fill="both", expand=True)

        # Back Button
        self.back_button = ctk.CTkButton(
            self, text="Back", command=self.back_to_main, **button_style)
        self.back_button.pack(pady=10)

    def toggle_month_year_selection(self):
        if self.show_all_var.get():
            self.month_menu.configure(state="disabled")
            self.year_menu.configure(state="disabled")
        else:
            self.month_menu.configure(state="normal")
            self.year_menu.configure(state="normal")

    def view_fees(self):
        show_all = self.show_all_var.get()

        if show_all:
            fees = self.fee_table.get_fees_name()
        else:
            month_year = f"{self.month_var.get()}/{self.year_var.get()}"
            fees = self.fee_table.get_fees_name(month_year)

        # Clear the treeview
        for item in self.fees_tree.get_children():
            self.fees_tree.delete(item)

        # Insert fees into the treeview
        for fee in fees:
            self.fees_tree.insert("", "end", values=(fee['name'], fee['month']))

    def show_payment_widgets(self):
        # Clear all widgets
        for widget in self.winfo_children():
            widget.pack_forget()

        # Payment Label
        payment_label = ctk.CTkLabel(self, text="Payment", font=('Arial', 16))
        payment_label.pack(pady=10)

        # Apartment Code
        self.apartment_code_label = ctk.CTkLabel(self, text="Apartment Code:")
        self.apartment_code_label.pack(pady=5)
        self.apartment_code_var = ctk.StringVar()
        apartment_codes = self.fee_table.get_apartment_codes()
        self.apartment_code_entry = AutocompleteCombobox(
            self, textvariable=self.apartment_code_var, completevalues=apartment_codes)
        self.apartment_code_entry.pack(pady=5)

        # Month/Year
        self.month_year_label = ctk.CTkLabel(self, text="Select Month and Year:")
        self.month_year_label.pack(pady=5)

        self.month_var = ctk.StringVar(value=str(int(datetime.now().strftime("%m"))))
        self.year_var = ctk.StringVar(value=datetime.now().strftime("%Y"))

        self.month_menu = ctk.CTkOptionMenu(
            self, variable=self.month_var, values=[str(i) for i in range(1, 13)])
        self.month_menu.pack(pady=5)

        self.year_menu = ctk.CTkOptionMenu(
            self, variable=self.year_var, values=[str(i) for i in range(2000, 2100)])
        self.year_menu.pack(pady=5)

        # Fee Name
        self.fee_name_label = ctk.CTkLabel(self, text="Fee Name:")
        self.fee_name_label.pack(pady=5)
        self.fee_name_var = ctk.StringVar()
        fee_names = self.fee_table.get_fee_names()
        self.fee_name_entry = AutocompleteCombobox(
            self, textvariable=self.fee_name_var, completevalues=fee_names)
        self.fee_name_entry.pack(pady=5)

        # Show Information Button
        button_style = {
            'fg_color': '#4CAF50',
            'text_color': 'white',
            'font': ('Arial', 12),
            'width': 150,
            'height': 40
        }

        self.show_info_button = ctk.CTkButton(
            self, text="Show Information", command=self.show_information, **button_style)
        self.show_info_button.pack(pady=10)

        # Payment Button
        self.payment_button = ctk.CTkButton(
            self, text="Payment", command=self.show_payment_dialog, **button_style)
        self.payment_button.pack(pady=10)

        # Information Display Frame
        self.info_frame = ctk.CTkFrame(self)
        self.info_frame.pack(padx=10, pady=10, fill="both", expand=True)


    def show_information(self):
        apartment_code = self.apartment_code_var.get()
        month_year = f"{self.month_var.get()}/{self.year_var.get()}"
        fee_name = self.fee_name_var.get()

        if not apartment_code or not month_year or not fee_name:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            info = self.fee_table.show_info(apartment_code, month_year, fee_name)
            fee_amount = info['fee']
            fee_paid = info['paid']
            state = info['state']
            money_left = info['money_left']

            # Clear previous information labels
            for widget in self.info_frame.winfo_children():
                widget.destroy()

            # Display information using labels
            ctk.CTkLabel(self.info_frame, text=f"Apartment Code: {apartment_code}").pack(anchor='w', padx=10)
            ctk.CTkLabel(self.info_frame, text=f"Month/Year: {month_year}").pack(anchor='w', padx=10)
            ctk.CTkLabel(self.info_frame, text=f"Fee Name: {fee_name}").pack(anchor='w', padx=10)
            ctk.CTkLabel(self.info_frame, text=f"Fee Amount: {fee_amount}").pack(anchor='w', padx=10)
            ctk.CTkLabel(self.info_frame, text=f"Amount Paid: {fee_paid}").pack(anchor='w', padx=10)
            ctk.CTkLabel(self.info_frame, text=f"Money Left: {money_left}").pack(anchor='w', padx=10)

            # Display state with colored bold text
            if state == 'completed':
                color = 'green'
            else:
                color = 'red'
            state_label = ctk.CTkLabel(
                self.info_frame,
                text=f"State: {state}",
                text_color=color,
                font=('Arial', 12, 'bold')
            )
            state_label.pack(anchor='w', padx=10)
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def show_payment_dialog(self):
        apartment_code = self.apartment_code_var.get()
        month_year = f"{self.month_var.get()}/{self.year_var.get()}"
        fee_name = self.fee_name_var.get()

        if not apartment_code or not month_year or not fee_name:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        # Create a custom dialog for payment
        dialog = Toplevel(self)
        dialog.title("Payment")
        dialog.geometry("400x400")

        Label(dialog, text="Enter payment amount:").pack(pady=5)
        payment_amount_var = ctk.StringVar()
        payment_amount_entry = Entry(dialog, textvariable=payment_amount_var)
        payment_amount_entry.pack(pady=5)

        Label(dialog, text="Select payment date/time:").pack(pady=5)
        cal = Calendar(dialog, selectmode='day', year=datetime.now().year, month=datetime.now().month, day=datetime.now().day)
        cal.pack(pady=5)

        time_var = ctk.StringVar(value=datetime.now().strftime("%H:%M:%S"))
        time_entry = Entry(dialog, textvariable=time_var)
        time_entry.pack(pady=5)

        def on_confirm():
            payment_amount = payment_amount_var.get()
            payment_date = cal.get_date() + " " + time_var.get()

            if not payment_amount:
                messagebox.showerror("Input Error", "Please enter a payment amount.")
                return

            if messagebox.askyesno("Confirm Payment", "Are you sure?"):
                try:
                    payment_amount = float(payment_amount)
                    self.fee_table.payment(apartment_code, month_year, fee_name, payment_amount)
                    messagebox.showinfo("Payment", "Payment successful!")
                    dialog.destroy()
                    # Update the displayed information
                    self.show_information()
                except ValueError:
                    messagebox.showerror("Input Error", "Please enter a valid number for payment amount.")
                except Exception as e:
                    messagebox.showerror("Payment Error", str(e))

        Button(dialog, text="OK", command=on_confirm).pack(pady=10)

    def pay_fee(self):
        apartment_code = self.apartment_code_var.get()
        month_year = f"{self.month_var.get()}/{self.year_var.get()}"
        fee_name = self.fee_name_var.get()
        payment_amount_str = self.payment_amount_var.get()

        if not apartment_code or not month_year or not fee_name or not payment_amount_str:
            messagebox.showerror("Input Error", "Please fill in all fields.")
            return

        try:
            payment_amount = float(payment_amount_str)
            # Call the payment method
            self.fee_table.payment(apartment_code, month_year, fee_name, payment_amount)
            messagebox.showinfo("Payment", "Payment successful!")
            # Update the displayed information
            self.show_information()
        except ValueError:
            messagebox.showerror("Input Error", "Please enter a valid number for payment amount.")
        except Exception as e:
            messagebox.showerror("Payment Error", str(e))

    def back_to_main(self):
        # Clear all widgets
        for widget in self.winfo_children():
            widget.pack_forget()
        # Recreate initial widgets
        self.create_initial_widgets()

    def exit_app(self):
        self.destroy()

if __name__ == "__main__":
    app = FeeGUI()
    app.mainloop()