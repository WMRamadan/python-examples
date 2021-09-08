import os
import tkinter as tk
from tkinter.constants import HORIZONTAL

from numpy import frexp
import play_sine

freq_val = 40
amp_val = 0.0

class FrequencyFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.create_frequency_frame()

    def create_frequency_frame(self):
        tk.Label(self, text="Frequency: ").grid(column=0, row=0, sticky=tk.W)
        self.freq = tk.Scale(self, from_=40, to=20000, length=700, width=50, tickinterval=3960, command=self.set_freq_value, orient=HORIZONTAL)
        self.freq.focus()
        self.freq.grid(column=1, row=0, sticky=tk.W)
    
    def set_freq_value(self, val):
        global freq_val
        freq_val = val

class AmplitudeFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.create_amplitude_frame()

    def create_amplitude_frame(self):
        tk.Label(self, text="Amplitude: ").grid(column=0, row=0, sticky=tk.W)
        self.amp = tk.Scale(self, from_=0, to=1, length=700, width=25, digits=2, resolution=0.1, tickinterval=1, command=self.set_amp_value, orient=HORIZONTAL)
        self.amp.focus()
        self.amp.grid(column=1, row=0, sticky=tk.W)

    def set_amp_value(self, val):
        global amp_val
        amp_val = val

class PlayFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.create_play_frame()
        self.psound = None

    def create_play_frame(self):
        self.play_button = tk.Button(self)
        self.play_button["text"] = "Play"
        self.play_button["command"] = self.play_message
        self.play_button["bg"] = "green"
        self.play_button.pack(side="top")

    def play_message(self):
        global freq_val
        global amp_val
        if not self.psound:
            self.psound = play_sine.play(frequency=int(freq_val), amplitude=amp_val)
        if self.play_button["text"] == "Play":
            print("message from play button!")
            self.psound.start()
            self.play_button["text"] = "Stop"
            self.play_button["bg"] = "red"
        elif self.play_button["text"] == "Stop":
            print("message from stop button!")
            self.psound.stop()
            self.psound.close()
            self.psound = None
            self.play_button["text"] = "Play"
            self.play_button["bg"] = "green"
        else:
            print("stopping audio!")
            self.psound.stop()
            self.psound.close()
            self.psound = None
            self.play_button["text"] = "Play"
            self.play_button["bg"] = "green"

class QuitFrame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.columnconfigure(0, weight=1)
        self.create_quit_frame()

    def create_quit_frame(self):
        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.grid(column=0, row=0, sticky=tk.W)

def create_main_window():
    root = tk.Tk(className="Pyfreq")
    os_name = os.name
    if os_name == "nt":
        root.iconbitmap(bitmap = "/ico/pyfreq_icon.ico")
    else:
        img = tk.PhotoImage(file="./ico/pyfreq_icon.gif")
        root.call("wm", "iconphoto", root._w, img)
    root.title("Pyfreq")
    root.minsize(1200,400)
    root.columnconfigure(0, weight=1)
    root.columnconfigure(1, weight=1)

    frequency_frame = FrequencyFrame(master=root)
    frequency_frame.grid(column=0, row=0)
    frequency_frame.freq.set(400)

    amplitude_frame = AmplitudeFrame(master=root)
    amplitude_frame.grid(column=0, row=1)
    amplitude_frame.amp.set(0.5)

    play_frame = PlayFrame(master=root)
    play_frame.grid(column=1, row=0)

    quit_frame = QuitFrame(master=root)
    quit_frame.grid(column=1, row=1)

    root.mainloop()

if __name__ == "__main__":
    create_main_window()
