import sys
import tkinter as tk
class EntryPanel():
    def __init__(self, master, title, text_button, from_=-100, to=100, state = tk.DISABLED, resolution = 1):
        self.value = tk.IntVar()
        self.title = title

        self.text_button = text_button

        self.box = tk.LabelFrame(master, text=self.title)
        self.entry = tk.Scale(self.box, from_=from_, to=to, resolution = resolution, orient=tk.HORIZONTAL)
        self.entry.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.button = tk.Button(self.box, text=self.text_button, state=state)
        self.button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.box.pack(fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)

    def enable(self):
        self.button.config(state=tk.NORMAL)

class TwoEntryPanel():
    def __init__(self, master, title, text_button, from_=-100, to=100, state = tk.DISABLED, resolution = 1):
        self.value = tk.IntVar()
        self.title = title

        self.text_button = text_button

        self.box = tk.LabelFrame(master, text=self.title)
        self.entry1 = tk.Scale(self.box, from_=from_, to=to, resolution = resolution, orient=tk.HORIZONTAL)
        self.entry1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.entry2 = tk.Scale(self.box, from_=from_, to=to, resolution = resolution, orient=tk.HORIZONTAL)
        self.entry2.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.button = tk.Button(self.box, text=self.text_button, state=state)
        self.button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.box.pack(fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)

    def enable(self):
        self.button.config(state=tk.NORMAL)

class ThreeEntryPanel():
    def __init__(self, master, title, text_button, from_=-100, to=100, state = tk.DISABLED, resolution = 1):
        self.value = tk.IntVar()
        self.title = title

        self.text_button = text_button

        self.box = tk.LabelFrame(master, text=self.title)
        self.entry1 = tk.Scale(self.box, from_=from_, to=to, resolution = resolution, orient=tk.HORIZONTAL)
        self.entry1.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.entry2 = tk.Scale(self.box, from_=from_, to=to, resolution = resolution, orient=tk.HORIZONTAL)
        self.entry2.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.entry3 = tk.Scale(self.box, from_=0, to=100, resolution = 1, orient=tk.HORIZONTAL)
        self.entry3.pack(side=tk.TOP, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.button = tk.Button(self.box, text=self.text_button, state=state)
        self.button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.box.pack(fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)

    def enable(self):
        self.button.config(state=tk.NORMAL)

class ButtonPanel():
    def __init__(self, master, title, text_button, state = tk.DISABLED):
        self.value = tk.IntVar()
        self.title = title

        self.text_button = text_button

        self.box = tk.LabelFrame(master, text=self.title)
        self.button = tk.Button(self.box, text=self.text_button, state=state)
        self.button.pack(side=tk.BOTTOM, fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)
        self.box.pack(fill=tk.BOTH, expand=tk.TRUE, pady=5, padx=5)

    def enable(self):
        self.button.config(state=tk.NORMAL)