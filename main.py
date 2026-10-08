import tkinter as tk


def on_click():
    label.config(text="Привет, Git!")


root = tk.Tk()
root.title("Генератор паролей")
root.geometry("300x150")

label = tk.Label(root, text="Здесь будет пароль", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Нажми меня", command=on_click)
button.pack()

root.mainloop()