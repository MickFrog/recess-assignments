# Ssenono Jordan Michael
# 21/U/1013
# 2100701013

import tkinter as tk
from datetime import datetime


def calculate_total_payment(amount, taxes):
    total_payment = amount + (amount * taxes)
    return total_payment


def print_receipt():
    # Get the input values
    payer = payer_entry.get()
    amount = float(amount_entry.get())
    counter_person = counter_person_entry.get()
    taxes = float(taxes_entry.get())

    # Calculate the total payment
    total_payment = calculate_total_payment(amount, taxes)

    # Get the current date and time
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Create the receipt content
    receipt_content = f"Receipt\n\nDate: {current_date}\n\nPayer: {payer}\nAmount Paid: UGX {amount}\nCounter Person: {counter_person}\nTaxes: {taxes}%\nTotal Payment: UGX {total_payment}"

    # Print the receipt
    receipt_text.delete('1.0', tk.END)
    receipt_text.insert(tk.END, receipt_content)


# Create the main window
window = tk.Tk()
window.title("Ssenono Jordan Receipt Printer")
window.geometry("500x400")

# Create the input fields
payer_label = tk.Label(window, text="Person Making Payment:")
payer_label.pack()
payer_entry = tk.Entry(window)
payer_entry.pack()

amount_label = tk.Label(window, text="Amount Paid:")
amount_label.pack()
amount_entry = tk.Entry(window)
amount_entry.pack()

counter_person_label = tk.Label(window, text="Person at Counter:")
counter_person_label.pack()
counter_person_entry = tk.Entry(window)
counter_person_entry.pack()

taxes_label = tk.Label(window, text="Taxes:")
taxes_label.pack()
taxes_entry = tk.Entry(window)
taxes_entry.pack()

# Create the print receipt button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.pack()

# Create the receipt display area
receipt_text = tk.Text(window, height=10, width=50)
receipt_text.pack()

# Run the GUI application
window.mainloop()
