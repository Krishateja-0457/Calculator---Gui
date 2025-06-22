import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Simple Calculator")
root.geometry("400x530")
root.resizable(True, True)

theme_mode = "light"
style = ttk.Style()
style.theme_use('clam')

selected_operator = tk.StringVar(value='+')  # Default operator
last_result = None  # Global variable to store previous result

def apply_theme():
    if theme_mode == "light":
        bg = "#f0f8ff"
        btn_bg = "#4da6ff"
        fg = "#000"
        entry_bg = "#ffffff"
    else:
        bg = "#2b2b2b"
        btn_bg = "#5dade2"
        fg = "#f0f0f0"
        entry_bg = "#3e3e3e"

    root.configure(bg=bg)
    style.configure("TLabel", background=bg, foreground=fg, font=("Segoe UI", 11))
    style.configure("TButton", background=btn_bg, foreground="white", font=("Segoe UI", 10, "bold"), padding=6)
    style.map("TButton", background=[("active", "#3399ff")])
    style.configure("TEntry", fieldbackground=entry_bg, foreground=fg, font=("Segoe UI", 12))
    for child in root.winfo_children():
        child.configure(style="TLabel")

def evaluate_expression():
    global last_result
    num1 = num1_entry.get().strip()
    num2 = num2_entry.get().strip()
    operator = selected_operator.get()

    if not num1 or not num2:
        result_label.config(text="Please enter both numbers")
        return

    if not num1.replace('.', '', 1).isdigit() or not num2.replace('.', '', 1).isdigit():
        result_label.config(text="Invalid number(s)")
        return

    num1, num2 = float(num1), float(num2)

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            result_label.config(text="Cannot divide by zero")
            return
        result = num1 / num2
    elif operator == '%':
        if num2 == 0:
            result_label.config(text="Cannot modulo by zero")
            return
        result = num1 % num2

    last_result = result  # Save result to memory
    result_label.config(text=f"Result: {result}")
    previous_label.config(text=f"Previous Result: {last_result}")

def clear_input():
    num1_entry.delete(0, tk.END)
    num2_entry.delete(0, tk.END)
    result_label.config(text="Result:")
    previous_label.config(text="Previous Result: ")

def toggle_theme():
    global theme_mode
    theme_mode = "dark" if theme_mode == "light" else "light"
    apply_theme()

# Title
ttk.Label(root, text="Calculator", font=("Segoe UI", 16, "bold")).pack(pady=20)

# Number inputs
input_frame = ttk.Frame(root)
input_frame.pack(pady=10)

ttk.Label(input_frame, text="Enter First Number:").grid(row=0, column=0, padx=5, pady=5)
num1_entry = ttk.Entry(input_frame, width=20)
num1_entry.grid(row=0, column=1, padx=5)

ttk.Label(input_frame, text="Enter Second Number:").grid(row=1, column=0, padx=5, pady=5)
num2_entry = ttk.Entry(input_frame, width=20)
num2_entry.grid(row=1, column=1, padx=5)

# Operator toggle buttons
ttk.Label(root, text="Select Operation:").pack(pady=10)
op_frame = ttk.Frame(root)
op_frame.pack()

for op in ['+', '-', '*', '/', '%']:
    b = ttk.Radiobutton(op_frame, text=op, variable=selected_operator, value=op)
    b.pack(side='left', padx=10)

# Buttons
btn_frame = ttk.Frame(root)
btn_frame.pack(pady=20)

ttk.Button(btn_frame, text="Calculate", command=evaluate_expression).pack(side='left', padx=10)
ttk.Button(btn_frame, text="Clear", command=clear_input).pack(side='left', padx=10)
ttk.Button(btn_frame, text="Theme", command=toggle_theme).pack(side='left', padx=10)

# Result and previous result
result_label = ttk.Label(root, text="Result:", font=("Segoe UI", 13, "bold"))
result_label.pack(pady=10)

previous_label = ttk.Label(root, text="Previous Result: ", font=("Segoe UI", 11))
previous_label.pack(pady=5)

apply_theme()
root.mainloop()
