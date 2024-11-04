import tkinter as tk
from math import sin, cos, tan, log, sqrt, pi, e, radians

# Creating the main window
root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")

# Global variable to hold the expression
expression = ""

# Function to update expression in the text entry box
def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

# Function to evaluate the final expression
def equalpress():
    try:
        global expression
        result = str(eval(expression))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""

# Function to clear the contents of the text entry box
def clear():
    global expression
    expression = ""
    equation.set("")

# Define exact values for common angles
exact_trig_values = {
    "sin": {
        0: "0", 30: "1/2", 45: "1/√2", 60: "√3/2", 90: "1"
    },
    "cos": {
        0: "1", 30: "√3/2", 45: "1/√2", 60: "1/2", 90: "0"
    },
    "tan": {
        0: "0", 30: "1/√3", 45: "1", 60: "√3", 90: "undefined"
    }
}

# Function to handle trigonometric calculations with exact values
def trig_func(func_name):
    global expression
    try:
        angle = eval(expression)
        if func_name in exact_trig_values and angle in exact_trig_values[func_name]:
            result = exact_trig_values[func_name][angle]
        else:
            # Use radians for non-exact values and fallback to decimal if no exact match
            angle_rad = radians(angle)
            if func_name == "sin":
                result = str(sin(angle_rad))
            elif func_name == "cos":
                result = str(cos(angle_rad))
            elif func_name == "tan":
                result = str(tan(angle_rad))

        equation.set(result)
        expression = str(result)
    except:
        equation.set("error")
        expression = ""

# Function for logarithmic and square root operations
def log_func():
    global expression
    try:
        result = str(log(eval(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""

def sqrt_func():
    global expression
    try:
        result = str(sqrt(eval(expression)))
        equation.set(result)
        expression = result
    except:
        equation.set("error")
        expression = ""

# StringVar to update the expression entry field
equation = tk.StringVar()

# Entry widget for displaying the equation
entry_field = tk.Entry(root, textvariable=equation, font=("Arial", 20), bd=10, insertwidth=2, width=16, borderwidth=4)
entry_field.grid(row=0, column=0, columnspan=4)

# Button Layout
button_text = [
    ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
    ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
    ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
    ('0', 4, 0), ('.', 4, 1), ('+', 4, 2), ('=', 4, 3),
    ('C', 5, 0), ('(', 5, 1), (')', 5, 2), ('sqrt', 5, 3),
    ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('log', 6, 3),
    ('pi', 7, 0), ('e', 7, 1), ('^', 7, 2)
]

# Adding Buttons to the grid
for (text, row, col) in button_text:
    if text == 'sin':
        tk.Button(root, text=text, command=lambda: trig_func('sin'), height=2, width=8).grid(row=row, column=col)
    elif text == 'cos':
        tk.Button(root, text=text, command=lambda: trig_func('cos'), height=2, width=8).grid(row=row, column=col)
    elif text == 'tan':
        tk.Button(root, text=text, command=lambda: trig_func('tan'), height=2, width=8).grid(row=row, column=col)
    elif text == 'log':
        tk.Button(root, text=text, command=log_func, height=2, width=8).grid(row=row, column=col)
    elif text == 'sqrt':
        tk.Button(root, text=text, command=sqrt_func, height=2, width=8).grid(row=row, column=col)
    elif text == 'pi':
        tk.Button(root, text=text, command=lambda: press(pi), height=2, width=8).grid(row=row, column=col)
    elif text == 'e':
        tk.Button(root, text=text, command=lambda: press(e), height=2, width=8).grid(row=row, column=col)
    elif text == '^':
        tk.Button(root, text=text, command=lambda: press("**"), height=2, width=8).grid(row=row, column=col)
    elif text == 'C':
        tk.Button(root, text=text, command=clear, height=2, width=8).grid(row=row, column=col)
    elif text == '=':
        tk.Button(root, text=text, command=equalpress, height=2, width=8).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, command=lambda t=text: press(t), height=2, width=8).grid(row=row, column=col)

# Start the Tkinter main loop
root.mainloop()

