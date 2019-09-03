import datetime
import sys
import os
from tkinter import *
from tkinter import ttk
import board
import digitalio

break_beam1 = digitalio.DigitalInOut(board.D4)
break_beam1.direction = digitalio.Direction.INPUT
break_beam1.pull = digitalio.Pull.UP

break_beam2 = digitalio.DigitalInOut(board.D18)
break_beam2.direction = digitalio.Direction.INPUT
break_beam2.pull = digitalio.Pull.UP

break_beam3 = digitalio.DigitalInOut(board.D26)
break_beam3.direction = digitalio.Direction.INPUT
break_beam3.pull = digitalio.Pull.UP

break_beam4 = digitalio.DigitalInOut(board.D23)
break_beam4.direction = digitalio.Direction.INPUT
break_beam4.pull = digitalio.Pull.UP

while break_beam4.value == True:
    if break)beam4.value == False:
        break

start = datetime.datetime.now()

beam1 = break_beam1.value
beam2 = break_beam2.value
beam3 = break_beam3.value

lane1Running = True
lane2Running = True
lane3Running = True

while beam1 == True or beam2 == True or beam3 == True:

    if break_beam1.value == False:
        beam2 = break_beam2.value
        beam3 = bream_beam3.value

    if break_beam2.value == False:
        beam1 = break_beam2.value
        beam3 = bream_beam3.value

    if break_beam3.value == False:
        beam1 = break_beam2.value
        beam2 = bream_beam3.value

    if break_beam1.value == False or break_beam2.value == False or break_beam3.value == False:

        if break_beam1.value == False and lane1Running == True:
            beam1 = False
            lane1 = datetime.datetime.now()
            lane1Running = False

        if break_beam2.value == False and lane2Running == True:
            beam2 = False
            lane2 = datetime.datetime.now()
            lane2Running = False

        if break_beam3.value == False and lane3Running == True:
            beam3 = False
            lane3 = datetime.datetime.now()
            lane3Running = False

print("Here are the final results of the race:")
lane1Time = (lane1 - start).total_seconds()
lane2Time = (lane2 - start).total_seconds()
lane3Time = (lane3 - start).total_seconds()

def restart_program():
    python = sys.executable
    os.execl(python, python, * sys.argv)

root = Tk()
root.configure(background='black')
w = 800 # width for the TK root
h = 250 # height for the TK root

# get screen width and height
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

# calculate x and y coordinates for the TK root window
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

# set the dimensions of the screen
# and where it is placed
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
label1 = Label(root, text="Thank you for participating in the Great Moment of Inertia Race!", background = 'black', foreground = 'white', font=("Courier", 18), wraplength = 700)
label1.pack()
label2 = Label(root, text="Here are the final results:", background = 'black', foreground = 'white', font=("Courier", 16), wraplangth = 700)
label2.pack()
label3 = Label(root, text=("Lane 1 time is", lane1Time, "seconds"), background = 'green', foreground = 'white', font=("Courier", 14), wraplength = 600)
label3.pack()
label4 = Label(root, text=("Lane 2 time is", lane2Time, "seconds"), background = 'green', foreground = 'white', font=("Courier", 14), wraplength = 600)
label4.pack()
label5 = Label(root, text=("Lane 3 time is", lane3Time, "seconds"), background = 'green', foreground = 'white', font=("Courier", 14), wraplength = 600)
label5.pack()
label6 = Label(root, text="To restart the race, click the button below, or, close this window to end the program!", font=("Courier", 12), foreground = 'white', background = 'black', wraplength = 700)
label6.pack()
restartButton = Button(root, text="Restart Race", font=("Courier", 12), command = restart_progrram).pack()
root.mainloop() # starts the mainloop
