#! /usr/bin/env python

import tkinter as tk
import pyautogui
import threading
import time

root = tk.Tk()
root.title("do not disturb")
root.geometry("100x100")
root.resizable(False, False)
def pushed():
    quit()

button = tk.Button(root, text="halt", command=pushed)
button.pack(expand=1)

def halt():
    time.sleep(1)
    x = root.winfo_rootx() + 50
    y = root.winfo_rooty() + 50
    pyautogui.moveTo(x, y, duration=2)
    pyautogui.click()

threading.Thread(target=halt).start()
root.mainloop()

