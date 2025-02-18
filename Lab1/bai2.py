import tkinter as tk
from tkinter import messagebox
import math

def phuongtrinhbac2():
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        c = float(entry_c.get())
        if a == 0:
            if b == 0:
                if c == 0:
                    result = "Phương trình vô số nghiệm"
                else:
                    result = "Phương trình vô nghiệm"
            else:
                x = -c/b
                result = f"Nghiệm x = {x:.2f}"
        else:
            delta = b*b-4*a*c
            delta_text = f"Δ = {delta:.2f}"
            if delta < 0:
                result = "Phương trình vô nghiệm"
            elif delta == 0:
                x = -b/2*a
                result = f"Phương trình có 1 nghiệm kép x1 = x2 = {x:.2f}"
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                result = f"Phương trình có 2 nghiệm phân biệt x1 = {x1:.2f} và x2 = {x2:.2f}"
        label_result.config(text=f"{delta_text}\n{result}")
    except ValueError:
        messagebox.showerror("Lỗi, vui lòng nhập số hợp lệ!")

root = tk.Tk()
root.title("Giải phương trình bậc 2")

tk.Label(root, text="Nhập a: ").grid(row=0, column=0,  padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nhập b: ").grid(row=1, column=0,  padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)

tk.Label(root, text="Nhập c ").grid(row=2, column=0,  padx=10, pady=5)
entry_c = tk.Entry(root)
entry_c.grid(row=2, column=1, padx=10, pady=5)

bpt = tk.Button(root, text="Giải phương trình", command=phuongtrinhbac2)
bpt.grid(row=3, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Kết quả: ")
label_result.grid(row=4, column=0, columnspan=2, pady=10)

root.mainloop()