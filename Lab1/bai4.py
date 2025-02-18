import tkinter as tk
from tkinter import messagebox

def timucln(a=None, b=None):
    try:
        if a == None and b == None:
            a = int(entry_a.get())
            b = int(entry_b.get())
        if b == 0:
            label_result.config(text=f"Ket qua: {a}")
            return a
        else:
            return timucln(b,a%b)
    except ValueError:
        messagebox.showerror("Lỗi", "Vui lòng nhập số hợp lệ!")

root = tk.Tk()
root.title("Uoc chung lon nhat cua 2 so")
tk.Label(root, text="Nhập a:").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)

tk.Label(root, text="Nhập b:").grid(row=1, column=0, padx=10, pady=5)
entry_b = tk.Entry(root)
entry_b.grid(row=1, column=1, padx=10, pady=5)

btn_solve = tk.Button(root, text="Giải uoc chung lon nhat", command=timucln)
btn_solve.grid(row=2, column=0, columnspan=2, pady=10)

label_result = tk.Label(root, text="Kết quả: ")
label_result.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()