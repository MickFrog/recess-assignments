# Ssenono Jordan Michael
# 21/U/1013
# 2100701013

import tkinter as tk
from tkinter import ttk

def perform_operation():
    try:
        # Get values from the entry fields and convert them to floats
        value1 = float(entry1.get())
        value2 = float(entry2.get())

        # Get the selected operation from the dropdown
        operation = dropdown.get()

        # Perform selected operation on the values
        if operation == 'Addition':
            result = value1 + value2
        elif operation == 'Subtraction':
            result = value1 - value2
        elif operation == 'Multiplication':
            result = value1 * value2
        elif operation == 'Division':
            result = value1 / value2

        # Display the result in the result_label
        result_label.config(text=f"Result: {result}")
    except ValueError:
        # Display an error message if the entered values are not valid floats or integers
        result_label.config(text="Please enter valid integers / floats.")
    except ZeroDivisionError:
        # Display an error message if division by zero occurs
        result_label.config(text="Cannot divide by zero.")

# Create the main window
window = tk.Tk()
window.title("Ssenono Jordan Calculator")

# Create labels and entry fileds for the values
label1 = tk.Label(window, text="Value 1:")
entry1 = tk.Entry(window)
window.geometry("500x400")

label2 = tk.Label(window, text="Value 2:")
entry2 = tk.Entry(window)

# Create a Combobox widget for selecting the operation
label3 = tk.Label(window, text="Choose operation")
dropdown = ttk.Combobox(window, values=['Addition', 'Subtraction', 'Multiplication', 'Division'])
dropdown.set('Addition') #initally selected elem in dropdown

# Create the calculate button and associate it with the perform_operation function
calculate_button = tk.Button(window, text="Calculate", command=perform_operation)

# Create the initially empty label to display the result
result_label = tk.Label(window, text="")

# Pack everything created in order to the window
label1.pack()
entry1.pack()
label2.pack()
entry2.pack()
label3.pack()
dropdown.pack()
calculate_button.pack()
result_label.pack()

# Start the Tkinter event loop
window.mainloop()