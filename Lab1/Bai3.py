import tkinter as tk
from tkinter import messagebox

def tinhgiaithua(a = None):
    try:
        if a is None: 
            a = int(entry_a.get())
        if a < 0:
           messagebox.showerror("Lỗi", "Vui lòng nhập số nguyên không âm!")
           return
        elif a == 0:
            label_result.config(text="Ket qua: 1")
            return 1
        else:
           result = a * tinhgiaithua(a -1)

        if a == int(entry_a.get()):
            label_result.config(text=f"ket qua: {result}")
        return result 
    except ValueError:
        messagebox.showerror("Lỗi, vui lòng nhập số hợp lệ!")

root = tk.Tk()
root.title("Tinh giai thua")
tk.Label(root, text="Nhập a:").grid(row=0, column=0, padx=10, pady=5)
entry_a = tk.Entry(root)
entry_a.grid(row=0, column=1, padx=10, pady=5)
btn_solve = tk.Button(root, text="Tinh giai thua", command=tinhgiaithua)
btn_solve.grid(row=1, column=0, columnspan=2, pady=10)
label_result = tk.Label(root, text="Kết quả: ")
label_result.grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
