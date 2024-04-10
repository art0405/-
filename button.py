import tkinter as tk
from PIL import Image, ImageTk
import subprocess
import sys

# Функция, которая будет запускать скрипт app.py
def run_app_script():
    # Запускаем скрипт app.py в отдельном процессе
    subprocess.Popen([sys.executable, "app.py"])

# Создание главного окна
root = tk.Tk()
root.title("Голосовой ассистент")

# Установка фона
background_image = Image.open("background.jpg")
background_photo = ImageTk.PhotoImage(background_image)
background_label = tk.Label(root, image=background_photo)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Создание кнопки
microphone_image = Image.open("background.jpg")
microphone_photo = ImageTk.PhotoImage(microphone_image)
microphone_button = tk.Button(root, image=microphone_photo, command=run_app_script)
microphone_button.pack(pady=20)

# Запуск главного цикла
root.mainloop()