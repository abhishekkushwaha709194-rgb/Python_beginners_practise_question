import tkinter as tk

class Calculator:
    def add(self, a, b): return a + b
    def subtract(self, a, b): return a - b
    def multiply(self, a, b): return a * b
    def divide(self, a, b):
        return a / b if b != 0 else "Error"

calc = Calculator()

def click(value):
    entry.insert(tk.END, value)

def clear():
    entry.delete(0, tk.END)

def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")


# Window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")

entry = tk.Entry(root, font=("Arial", 20), bd=5, relief="ridge", justify="right")
entry.grid(row=0, column=0, columnspan=4)

# Buttons layout
buttons = [
    ('7',1,0), ('8',1,1), ('9',1,2), ('/',1,3),
    ('4',2,0), ('5',2,1), ('6',2,2), ('*',2,3),
    ('1',3,0), ('2',3,1), ('3',3,2), ('-',3,3),
    ('0',4,0), ('C',4,1), ('=',4,2), ('+',4,3)
]

for (text, row, col) in buttons:
    if text == "C":
        tk.Button(root, text=text, width=5, height=2,
                  command=clear).grid(row=row, column=col)
    elif text == "=":
        tk.Button(root, text=text, width=5, height=2,
                  command=calculate).grid(row=row, column=col)
    else:
        tk.Button(root, text=text, width=5, height=2,
                  command=lambda t=text: click(t)).grid(row=row, column=col)

root.mainloop()