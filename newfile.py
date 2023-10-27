import tkinter as tk
from tkinter import CENTER
import webbrowser

def show_birthday_alert():
    alert_window = tk.Toplevel(window)
    alert_window.title("Selamat Ulang Tahun")
    alert_window.geometry("300x200")

    # Membuat frame untuk menengahkan tombol
    frame = tk.Frame(alert_window)
    frame.pack(expand=True)

    # Desain tambahan untuk alert
    alert_frame = tk.Frame(frame, bg="pink")
    alert_frame.pack(fill="both", expand=True)

    alert_label = tk.Label(alert_frame, text="Selamat Ulang Tahun Sayangku!", font=('Arial', 16), padx=10, pady=10)
    alert_label.pack()

    # Fungsi untuk membuka tautan ke halaman web saat tombol ditekan
    def open_webpage():
        webbrowser.open("https://tamassr.github.io/bungauntukpacarkutersayang/")

    # Tombol "Hadiah Lainnya Nih" ditengah
    link_button = tk.Button(alert_frame, text="Hadiah Lainnya Nih", command=open_webpage, width=20, height=2, bg='purple')
    link_button.pack(side=CENTER)

    # Tombol untuk menutup jendela alert
    close_button = tk.Button(alert_frame, text="Close", command=alert_window.destroy, width=20, height=2, bg='red')
    close_button.pack(side=CENTER)

# Fungsi untuk mengeksekusi operasi matematika
def evaluate():
    expression = entry.get()
    if expression == "011110":
        show_birthday_alert()
    else:
        try:
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")

# Fungsi untuk menghapus input
def clear():
    entry.delete(0, tk.END)

# Fungsi untuk menambahkan tombol
def add_button(button_text, row, col, width=10, height=2, bg="lightgray"):
    return tk.Button(frame, text=button_text, command=lambda: entry.insert(tk.END, button_text), width=width, height=height, bg=bg)

# Membuat jendela utama
window = tk.Tk()
window.title("Kalkulator")
window.configure(bg='black')

frame = tk.Frame(window, bg='black')
frame.pack()

entry = tk.Entry(frame, font=('Arial', 20), bg='black', fg='white')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")

buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    '0', '.', '+'
]

row, col = 1, 0

for button_text in buttons:
    button = add_button(button_text, row, col)
    button.grid(row=row, column=col, padx=10, pady=10, sticky="nsew")
    col += 1
    if col > 3:
        col = 0
        row += 1

# Tombol untuk angka 0
zero_button = add_button("0", row, col, width=22, height=2)
zero_button.grid(row=row, column=col, columnspan=2, padx=10, pady=10, sticky="nsew")

# Tombol "Clear"
clear_button = add_button("C", row, col + 2, width=10, height=2, bg='red')
clear_button.config(command=clear)
clear_button.grid(row=row, column=col+2, padx=10, pady=10, sticky="nsew")

# Tombol khusus untuk menghitung hasil
equal_button = add_button("=", row, col, width=10, height=2, bg='orange')
equal_button.config(command=evaluate)
equal_button.grid(row=row + 1, column=col+2, padx=10, pady=10, sticky="nsew")

# Konfigurasi agar sel-sel dapat melebar saat jendela diperbesar
for r in range(6):
    frame.grid_rowconfigure(r, weight=1)
for c in range(4):
    frame.grid_columnconfigure(c, weight=1)

# Menjalankan aplikasi
window.mainloop()