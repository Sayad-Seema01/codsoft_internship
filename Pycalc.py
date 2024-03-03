import tkinter as tk

def on_button_click(value):
    current_text = entry.get()
    entry.delete(0, tk.END)
    entry.insert(tk.END, current_text + value)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main window
root = tk.Tk()
root.title("Stylish Calculator")
root.geometry("400x500")
root.configure(bg="#070F2B")  # Set background color

# Entry widget to display input and results
entry = tk.Entry(root, width=20, font=('Arial', 18), justify='right', bd=10, bg="#1B1A55", fg="white")
entry.grid(row=0, column=0, columnspan=4, pady=10)

# Define button layout and create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '=', '+'
]

row_val = 1
col_val = 0

for button in buttons:
    tk.Button(root, text=button, padx=20, pady=20, font=('Arial', 14),
              command=lambda btn=button: on_button_click(btn) if btn != '=' else calculate_result(),
              bg="#535C91", fg="white", bd=5).grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Clear button
tk.Button(root, text='C', padx=20, pady=20, font=('Arial', 14), command=clear_entry,
          bg="#FF5733", fg="white", bd=5).grid(row=row_val, column=col_val, padx=5, pady=5)

# Run the application
root.mainloop()
