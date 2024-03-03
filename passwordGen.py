import tkinter as tk
from tkinter import ttk
import random
import string

def generate_password():
    password_length = int(length_entry.get())

    if password_length <= 0:
        result_label.config(text="Please enter a valid password length.", foreground="red")
        return

    complexity = complexity_combobox.get()

    if complexity == "Low":
        characters = string.ascii_letters
    elif complexity == "Medium":
        characters = string.ascii_letters + string.digits
    elif complexity == "High":
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        result_label.config(text="Please select a valid complexity level.", foreground="red")
        return

    generated_password = ''.join(random.choice(characters) for _ in range(password_length))
    result_label.config(text=f"Generated Password: {generated_password}", foreground="green")

# GUI setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("500x400")

# Styles
style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 12), foreground="#000000", background="#944E63")
style.configure("TLabel", font=('Helvetica', 12))
style.configure("TCombobox", padding=8, font=('Helvetica', 12))
style.configure("TEntry", padding=8, font=('Helvetica', 12))
style.configure("TFrame", background="#944E63")

# Widgets
frame = ttk.Frame(root, style="TFrame")
frame.pack(fill=tk.BOTH, expand=True)

length_label = ttk.Label(frame, text="Enter Password Length:")
length_entry = ttk.Entry(frame, width=10)
complexity_label = ttk.Label(frame, text="Select Complexity:")
complexity_combobox = ttk.Combobox(frame, values=["Low", "Medium", "High"])
generate_button = ttk.Button(frame, text="Generate Password", command=generate_password)
result_label = ttk.Label(frame, text="", font=('Helvetica', 14, 'bold'))

# Grid layout
length_label.grid(row=0, column=0, padx=20, pady=10, sticky="e")
length_entry.grid(row=0, column=1, padx=20, pady=10, sticky="w")
complexity_label.grid(row=1, column=0, padx=20, pady=10, sticky="e")
complexity_combobox.grid(row=1, column=1, padx=20, pady=10, sticky="w")
generate_button.grid(row=2, column=0, columnspan=2, pady=20)
result_label.grid(row=3, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
