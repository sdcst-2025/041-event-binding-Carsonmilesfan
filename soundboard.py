
import tkinter as tk
import playsound as p



def playsound(event):
    print(event)
    p.playsound("ytmp3free.cc_vine-boom-sound-effect-youtubemp3free.org.mp3", block=False)


def sound(fella):
    print(fella)
    p.playsound("ytmp3free.cc_scooby-doo-laugh-rehehehe-sound-effect-youtubemp3free.org.mp3", block=False)


def aysound(miles):
    print(miles)
    p.playsound("brr-brr-patapim.mp3", block=False)

def superman(batman):
    print(batman)
    p.playsound("ytmp3free.cc_kanye-west-monster-edit-audio-slowedreverb-youtubemp3free.org.mp3", block=False)

def monster(frank):
    print(frank)
    p.playsound("ytmp3free.cc_taco-bell-bong-sound-effect-hd-youtubemp3free.org.mp3", block=False)

def cherokee(grand):
    print(grand)
    p.playsound("mrbeast-button.mp3", block=False)

def miles(sanders):
    print(sanders)
    p.playsound("g2.mp3", block=False)

def pool(pooly):
    print(pooly)
    p.playsound("car-crash_OwBDipR.mp3", block=False)

def monopoly(money):
    print(money)
    p.playsound("truth-detector-buzzer.mp3", block=False)

def trala(lelo):
    print(lelo)
    p.playsound("wrong-answer-sound-effect.mp3", block = False)



win = tk.Tk()
win.attributes('-topmost',True)

a1 = tk.Button(win, text = '| vine boom |')
a1.bind("<Button>", playsound)
a2 = tk.Button(win, text = '|   laugh   |')
a2.bind("<Button>", sound)
a3 = tk.Button(win, text = '|  italian  |')
a3.bind("<Button>", aysound)
a4 = tk.Button(win, text = '|   sigma   |')
a4.bind("<Button>", superman)
a5 = tk.Button(win, text = '|    taco   |')
a5.bind("<Button>", monster)
a6 = tk.Button(win, text = '|  mrbeast  |')
a6.bind("<Button>", cherokee)
a7 = tk.Button(win, text = '|  gangsta  |')
a7.bind("<Button>", miles)
a8 = tk.Button(win, text = '|   crash   |')
a8.bind("<Button>", pool)
a9 = tk.Button(win, text = '|   right   |')
a9.bind("<Button>", monopoly)
a10 = tk.Button(win, text = '|   wrong   |')
a10.bind("<Button>", trala)

a1.grid(row = 1, column = 1)
a2.grid(row = 1, column = 3)
a3.grid(row = 3, column = 1)
a4.grid(row = 3, column = 3)
a5.grid(row = 5, column = 1)
a6.grid(row = 5, column = 3)
a7.grid(row = 7, column = 1)
a8.grid(row = 7, column = 3)
a9.grid(row = 9, column = 1)
a10.grid(row = 9, column = 3)


win.mainloop()