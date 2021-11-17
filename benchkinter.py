import win32api
import pyautogui
import keyboard
import win32con
from pynput.keyboard import Key, Controller
from tkinter import *
import webbrowser
import time


root = Tk()
root.geometry("300x300+2021+396")
keyboard1 = Controller()


def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, x, y, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, x, y, 0, 0)


def reaction():
    inf = Label(root, text="Started").grid(row=4, column=0)
    click(952, 601)
    time.sleep(0.1)
    click(952, 601)
    cor = False
    if cor is False:
        while keyboard.is_pressed("q") is False:
            try:
                if pyautogui.pixel(952, 407) == (75, 219, 106):
                    click(958, 554)
            except Exception:
                inf1 = Label(root, text="Error, restarting...").grid(row=5, column=0)
                cor = False
        if keyboard.is_pressed("q"):
            inf2 = Label(root, text="Stopped").grid(row=6, column=0)


def target():
    inf = Label(root, text="Started").grid(row=4, column=0)
    click(952, 601)
    time.sleep(0.1)
    click(952, 601)
    cor = False
    if cor is False:
        alvo = pyautogui.screenshot()
        while keyboard.is_pressed("q") is False:
            try:
                if pyautogui.locateOnScreen("alvo.jpg", region="0, 165, 1900, 694", confidence=0.8):
                    width, height = alvo.size
                    for x in range(0, width, 5):
                        for y in range(0, height, 5):
                            r, g, b = alvo.getpixel((x,y))
                            if b == 232:
                                click(x + 0, y + 0)
            except Exception:
                inf1 = Label(root, text="Error, restarting...").grid(row=5, column=0)
                cor = False
        if keyboard.is_pressed("q"):
            inf2 = Label(root, text="Stopped").grid(row=6, column=0)


def browser():
    webbrowser.open("https://humanbenchmark.com/")


rot = Label(root, text='a HumanBenchMark "cheat"').grid(row=0, column=0)
rot2 = Label(root, text='Press "q" to stop the bot').grid(row=1, column=0)
root.title("BenchBot")
log = Label(root, text='Log:').grid(row=3, column=0, sticky="e")
bb = Button(root, text="Site", padx=50, command=browser, bg="light gray").grid(row=2, column=0)
button1 = Button(root, text="Reaction Test", padx=50, command=reaction, bg="light gray").grid(row=3, column=0)
button2 = Button(root, text="Target Test", padx=50, command=target, bg="light gray").grid(row=4, column=0)

root.mainloop()
