import time, pyautogui, keyboard, threading

from tkinter import *

window = Tk()

window.title("Auto clicker")


# Functions
def clickedStart():
    time.sleep(2)

    run = True
    intervalInt = None

    # try:
    #     intervalInt = int(txt.get())
    # except:
    #     pass

    start = time.time()

    while run == True:

        if keyboard.is_pressed('z'):
            run = False
            break

        if intervalInt != None:
            if time.time() >= (start + intervalInt):
                pyautogui.click()
                start = time.time()
        else:
            pyautogui.click()


lbl = Label(window, text="Press Z to Stop")
lbl.grid(column=1, row=0, padx=(75, 10))

# txt = Entry(window, width=10)
# txt.grid(column=1, row=1, padx=(75, 10))

btn = Button(window, text="Start clicking", command=clickedStart, bg="blue", fg="lightblue")
btn.grid(column=1, row=2, padx=(75, 10), pady=(15, 10))

window.geometry("220x100")

# txt.focus()
window.mainloop()