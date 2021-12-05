from tkinter import *
from pygame import mixer
import datetime, time

def goOff(sound)-> None:
    mixer.init()

    mixer.music.load(sound)

    mixer.music.set_volume(0.5)

    mixer.music.play()

def stop():
    mixer.music.stop()

sounds = {
    "christmas":"Sounds/Christmas-piano-logo.mp3",
    "synth":"Sounds/Synth-music-loop-80-bpm.wav",
    "Purge":"Sounds/The-purge-siren.mp3"
}



def alarm(set_alarm_timer):
    global clicked
    global sounds
    while True:
        time.sleep(1)
        current_time = datetime.datetime.now()
        now = current_time.strftime("%H:%M:%S")
        date = current_time.strftime("%d/%m/%y")
        # print("The Set Date is:", date)
        # print(now)
        if now == set_alarm_timer:
            # print("TIME TO WAKE UP!!")
            goOff(sounds.get(clicked.get()))
            break

def actual_time():
    set_alarm_timer = f"{hour.get()}:{min.get()}:{sec.get()}"
    alarm(set_alarm_timer)

clock = Tk()

clock.title("DataFlair Alarm Clock")

instructions = Label(clock, text=
"Enter time in 24 hour format")
instructions.grid(row=0, column=0, columnspan=4)

hour = StringVar()
min = StringVar()
sec = StringVar()

hourLabel = Label(clock, text="Hour").grid(row=1, column=0, sticky=W)
hourEntry = Entry(clock, textvariable=hour, width=4).grid(row=1, column=1, sticky=W)

minLabel = Label(clock, text="Min").grid(row=2, column=0, sticky=W)
minEntry = Entry(clock, textvariable=min, width=4).grid(row=2, column=1, sticky=W)

secLabel = Label(clock, text="Sec").grid(row=3, column=0, sticky=W)
secEntry = Entry(clock, textvariable=sec, width=4).grid(row=3, column=1, sticky=W)

clicked = StringVar()
clicked.set("none")

drop = OptionMenu(clock, clicked, *sounds.keys()).grid(row=5,column=0, sticky=W)
testButton = Button(clock, text='test sound', command= lambda:goOff(sounds.get(clicked.get())))
testButton.grid(row=6, column=0, sticky=W)

submitButton = Button(clock, text="Set Alarm", command=lambda:actual_time()).grid(row=4,column=0,sticky=W)

stopButton = Button(clock, text='stop', command=stop).grid(row=7,column=0, sticky=W)
clock.mainloop()

