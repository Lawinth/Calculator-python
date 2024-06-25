import tkinter as tk
from tkinter import messagebox
def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    else:
        return x / y
def calculate():
    a = entry_a.get()
    b = entry_b.get()
    operation = operation_var.get()
    
    try:
        a = float(a)
        b = float(b)
        
        if operation == 'Add':
            result = add(a, b)
        elif operation == 'Subtract':
            result = subtract(a, b)
        elif operation == 'Multiply':
            result = multiply(a, b)
        elif operation == 'Divide':
            result = divide(a, b)
        
        result_label.config(text=f"Result: {result}")    
    except ValueError:
        messagebox.showerror("Input error", "Please enter valid numbers")
root = tk.Tk()
root.config(background="cyan")
root.title("Calculator")
tk.Label(root,bg="cyan", text="First number:").grid(row=0, column=0)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1)
tk.Label(root,bg="cyan", text="Second number:").grid(row=1, column=0)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1)
tk.Label(root, text="Select operation:").grid(row=2, column=0)
operation_var = tk.StringVar(value="Add")
operations = ["Add", "Subtract", "Multiply", "Divide"]
operation_menu = tk.OptionMenu(root, operation_var, *operations)
operation_menu.grid(row=2, column=1)
calculate_button = tk.Button(root,bg="violet", text="Calculate", command=calculate)
calculate_button.grid(row=3, columnspan=2)
result_label = tk.Label(root, bg="lightblue",text="Result: ")
result_label.grid(row=4, columnspan=2)
root.mainloop()
