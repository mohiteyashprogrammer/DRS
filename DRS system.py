# DRS review system

import tkinter
import PIL.Image, PIL.ImageTk
import cv2
from functools import partial
import threading # This is help to not to block programm
import imutils # To resize a image
import time


stream = cv2.VideoCapture(r"C:\Users\yash mohite\OneDrive\Desktop\drs\clip.mp4")
def play(speed):
    print(f"You clicked on play. speed is {speed}")

    # Play the video in reverse mode
    frame1 = stream.get(cv2.CAP_PROP_POS_FRAMES)
    stream.set(cv2.CAP_PROP_POS_FRAMES, frame1 + speed)
    grabbed, frame = stream.read()
    if not grabbed:
        exit()
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0, 0, image= frame, anchor=tkinter.NW)
    canvas.create_text(120, 25, fill = "black", font="time 20 italic bold", text= "Decision pending")


    


def pending(decision):
    # Display decision pending image
    frame = cv2.cvtColor(cv2.imread(r"C:\Users\yash mohite\OneDrive\Desktop\drs\pending.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)
    
    # Wite for 1 second
    time.sleep(1)

    # Display sponsor image   
    frame = cv2.cvtColor(cv2.imread(r"C:\Users\yash mohite\Downloads\sponser.png"), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)

    # Wait for 1.5 second
    time.sleep(1.5)

    # Display out/not out image
    if decision== 'out':
        decisionimg = r"C:\Users\yash mohite\OneDrive\Desktop\drs\out.png"
    else:
        decisionimg = r"C:\Users\yash mohite\OneDrive\Desktop\drs\not_out.png"    
    frame = cv2.cvtColor(cv2.imread(decisionimg), cv2.COLOR_BGR2RGB)
    frame = imutils.resize(frame, width= SET_WIDTH, height= SET_HEIGHT)
    frame = PIL.ImageTk.PhotoImage(image= PIL.Image.fromarray(frame))
    canvas.image = frame
    canvas.create_image(0,0,image=frame, anchor=tkinter.NW)





def out():
    thread = threading.Thread(target=pending, args=("out",))
    thread.daemon = 1
    thread.start()
    print("Player is Out ")

def not_out():
    thread = threading.Thread(target=pending, args=("not out",))
    thread.daemon = 1
    thread.start()
    print("Player is not out")

# Width and Height of our screen
SET_WIDTH = 650
SET_HEIGHT = 368

# tkinter gui starts here
window = tkinter.Tk()
window.title("Third umpire Decision Review kit")
img = cv2.cvtColor(cv2.imread(r"C:\Users\yash mohite\OneDrive\Desktop\drs\welcome.png"),cv2.COLOR_BGR2RGB)
canvas = tkinter.Canvas(window, width= SET_WIDTH, height= SET_HEIGHT)
photo = PIL.ImageTk.PhotoImage(image=PIL.Image.fromarray(img))
image_on_canvas = canvas.create_image(0, 0, anchor=tkinter.NW, image=photo)
canvas.pack()

# Buttons to control playback
btn = tkinter.Button(window, text="<< previous (fast)", width=50,
command=partial(play, -25))
btn.pack()

btn = tkinter.Button(window, text="<< previous (slow)", width=50,
command=partial(play, -2))
btn.pack()

btn = tkinter.Button(window, text=" Next (slow)>>", width=50,
command=partial(play, 2))
btn.pack()

btn = tkinter.Button(window, text=" Next (fast)>>", width=50,
command=partial(play, 25))
btn.pack()

btn = tkinter.Button(window, text=" Give Out", width=50,command= out)
btn.pack()

btn = tkinter.Button(window, text="  Give Not Out", width=50,command= not_out)
btn.pack()
window.mainloop() 