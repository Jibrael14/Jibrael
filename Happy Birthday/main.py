import tkinter as tk
import time
from threading import Thread

def animate_message(label, message, delay=100):
    def inner():
        label.config(text="")
        for i in range(len(message) + 1):
            label.config(text=message[:i])
            time.sleep(delay / 1000.0)
    Thread(target=inner).start()

def show_birthday_message():
    name = name_entry.get()
    if not name:
        name = "Jibreal Malik"

    cake_label.config(text="🎂🎂🎂🎂🎂🎂🎂🎂\n  HAPPY BIRTHDAY\n   " + name.upper() + "!\n🎉🎉🎉🎉🎉🎉🎉🎉")
    animate_message(message_label, f"🎈🎊 Happy Birthday, {name}! 🎊🎈", delay=100)
    animate_message(message2_label, "Wishing you joy, success, and love! 💖", delay=150)


root = tk.Tk()
root.title("🎂 Happy Birthday 🎂")
root.geometry("500x400")
root.configure(bg="#FFF0F5")


tk.Label(root, text="Enter Name:", font=("Helvetica", 14), bg="#FFF0F5").pack(pady=10)
name_entry = tk.Entry(root, font=("Helvetica", 14), width=30, justify='center')
name_entry.pack()


tk.Button(root, text="🎉 Show Birthday Wishes 🎉", font=("Helvetica", 14, "bold"), bg="#1C42BE", fg="white", command=show_birthday_message).pack(pady=20)


cake_label = tk.Label(root, font=("Helvetica", 16), bg="#FFF0F5", fg="#1424FF")
cake_label.pack()

message_label = tk.Label(root, font=("Helvetica", 16, "italic"), bg="#FFF0F5", fg="purple", wraplength=450)
message_label.pack(pady=10)

message2_label = tk.Label(root, font=("Helvetica", 14), bg="#FFF0F5", fg="green", wraplength=450)
message2_label.pack(pady=5)


root.mainloop()
