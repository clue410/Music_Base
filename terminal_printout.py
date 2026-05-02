import subprocess
import tkinter as tk
import os
import re

class ScrollableTextWindow:

    def __init__(self, root):
        self.root = root
        self.root.title("Terminal Output")
        self.root.geometry("1000x300")

        self.root.config(background="#060A13")

        frame = tk.Frame(self.root, bg="#060A13")
        frame.pack(fill=tk.BOTH, expand=True)

        self.scrollbar = tk.Scrollbar(frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.scrollbar.config(background="#F7F01E", highlightbackground="#FF5F57")
        self.scrollbar.pack_forget()