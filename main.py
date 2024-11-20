import pyautogui as pag
import random
import time
import keyboard
import tkinter as tk
from tkinter import *
from tkinter import messagebox
import threading

window = tk.Tk()
window.title("Mouse Bot")
window.geometry('900x500')
window.configure(bg="#fff")
window.resizable(False, False)

# Create a stop flag
stop_flag = False

def mouse_bot():
    global stop_flag
    stop_flag = False  # Reset flag each time the function is called

    def run_bot():
        global stop_flag
        while not stop_flag:
            x = random.randint(100, 900)
            y = random.randint(100, 900)
            pag.moveTo(x, y, 0.5)
            time.sleep(2)
        tk.messagebox.showinfo(title="Info", message="Stopped")

    # Run the bot in a separate thread
    bot_thread = threading.Thread(target=run_bot)
    bot_thread.start()

def stop_bot():
    global stop_flag
    stop_flag = True  # Set flag to True to stop the bot

def close_mouse():
    stop_bot()  # Ensure the bot stops if the window is closed
    window.destroy()

# label
label1 = tk.Label(window, text="Welcome to Mouse Bot", font=('Times New Roman', 30), bg="white")
label1.place(relx=0.5, rely=0.2, anchor=CENTER)
label2 = tk.Label(window, text="Press 'x' and wait to stop", bg="white")
label2.place(relx=0.5, rely=0.3, anchor=CENTER)

# button
button1 = Button(window, width=10, bg="green", bd=2, text="Start", command=mouse_bot)
button1.place(relx=0.3, rely=0.6, anchor=CENTER)
button2 = Button(window, width=10, bg="red", bd=2, text="Close", command=close_mouse)
button2.place(relx=0.7, rely=0.6, anchor=CENTER)

# Set keyboard listener to stop bot
keyboard.add_hotkey('x', stop_bot)

# mainloop
window.mainloop()
