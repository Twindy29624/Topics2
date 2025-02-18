import tkinter as tk
from tkinter import messagebox

def linear_equation():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if a == 0:
            if b == 0:
                result = "The equation has infinitely many solutions."
            else:
                result = "THe equation has no solution."
        else:
            x = -b/a
            result = f"The solution is x = {x}"
        label_result.config(text=f"Result \n {result}")
    except ValueError:
        messagebox.showerror("Error, Please enter a valid number!")

root = tk.Tk()
root.title("Solve the linear equation")
root.geometry("200x200")
root.resizable(False,False)

tk.Label(root, text="Enter a = ").grid(row=0 , column=0 , padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=5, pady=10)

tk.Label(root, text="Enter b = ").grid(row=1, column=0, padx=10, pady=15)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=5, pady=10)

stle = tk.Button(root, text="Solve the equation", command=linear_equation)
stle.grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text= f"Result ")
label_result.grid(row=3 , column=0, columnspan=2, pady=10)

root.mainloop()
