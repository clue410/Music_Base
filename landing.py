import tkinter as tk
import customtkinter


from tkinter import messagebox as mb

# import tinytag
# from tkinterdnd2 import DND_FILES, TkinterDnD
# from PIL import Image, ImageTk  # Import Pillow for image handling
import tkinterdnd2
from tkinter import ttk, messagebox, filedialog
import threading
import colorsys
# from matplotlib import image as img
# from scipy.cluster.vq import whiten, kmeans
# import pandas as pd
# import numpy as np
# from PIL import ImageDraw
import json
import os



root = tkinterdnd2.Tk()
tool_rack_root = tkinterdnd2.Tk()
tool_rack_root.withdraw()

root.bind()
root.title("RIPPER")
root.attributes("-fullscreen", True)
# root.geometry("1920x1080")
root.state('zoomed')
root.resizable(False, False)
root.configure(bg='#060A13')
root_width = root.winfo_width()
root_height = root.winfo_height()

print(root_height)

# customtkinter.set_appearance_mode("dark")  # Modes: system (default), light, dark
# customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green
# root.iconbitmap('images/codemy.ico')

def swap_layouts(event):
    print(f"The '{event.char}' key was pressed.")
    # if landing_page_state == "action_rack":
    #     landing_page_state = "tool_rack"

def is_an_anniversary_today():
    print("say happy birthday")
#     check if anniversary today, if yes make anniversary popup +/ make effects (?)


def label_click(item_id):
    print(f"LABEL CLICK {item_id}")




action_rack = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=(root_width / 2),
                       height=root_height)
welder_logo_frame = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=(root_width / 2),
                             height=root_height)
welder_logo_frame.grid_rowconfigure(0, weight=1)
welder_logo_frame.grid_columnconfigure(1, weight=1)
# album_art_frame = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=400, height=750)
# action_rack.configure(width=root_width/2, height=root_height)
# welder_logo.configure(width=root_width/2, height=root_height)
action_rack.grid_propagate(1)
welder_logo_frame.grid_propagate(0)

action_rack.grid(column=2, row=0, columnspan=1, rowspan=1, sticky="ne")
welder_logo_frame.grid(column=1, row=0, columnspan=1, rowspan=1, sticky="ne")

welder_logo = tk.Frame(welder_logo_frame, bg="#2ABF02", width=(root_width / 2) - 30, height=root_height - 35)
welder_logo.grid(column=1, row=0, sticky="")

rack_item_1_frame = tk.Frame(action_rack, bg="#30B5EB", width=root_width / 2, height=root_height / 12)
rack_item_2_frame = tk.Frame(action_rack, bg="#CF458E", width=root_width / 2, height=root_height / 12)
rack_item_3_frame = tk.Frame(action_rack, bg="#30B5EB", width=root_width / 2, height=root_height / 12)
rack_item_4_frame = tk.Frame(action_rack, bg="#CF458E", width=root_width / 2, height=root_height / 12)
rack_item_5_frame = tk.Frame(action_rack, bg="#30B5EB", width=root_width / 2, height=root_height / 12)
rack_item_6_frame = tk.Frame(action_rack, bg="#CF458E", width=root_width / 2, height=root_height / 12)
rack_item_7_frame = tk.Frame(action_rack, bg="#30B5EB", width=root_width / 2, height=root_height / 12)
rack_item_8_frame = tk.Frame(action_rack, bg="#CF458E", width=root_width / 2, height=root_height / 12)
rack_item_9_frame = tk.Frame(action_rack, bg="#30B5EB", width=root_width / 2, height=root_height / 12)
rack_item_10_frame = tk.Frame(action_rack, bg="#CF458E", width=root_width / 2, height=root_height / 12)
rack_item_11_frame = tk.Frame(action_rack, bg="#30B5EB", width=root_width / 2, height=root_height / 12)
rack_item_12_A_frame = tk.Frame(action_rack, bg="#CF458E", width=root_width / 4, height=root_height / 12)
rack_item_12_B_frame = tk.Frame(action_rack, bg="#B0A1EE", width=root_width / 4, height=root_height / 12)

#
rack_item_1_frame.grid(column=2, row=0, columnspan=1, rowspan=1, sticky="ne")
rack_item_2_frame.grid(column=2, row=1, columnspan=1, rowspan=1, sticky="ne")
rack_item_3_frame.grid(column=2, row=2, columnspan=1, rowspan=1, sticky="ne")
rack_item_4_frame.grid(column=2, row=3, columnspan=1, rowspan=1, sticky="ne")
rack_item_5_frame.grid(column=2, row=4, columnspan=1, rowspan=1, sticky="ne")
rack_item_6_frame.grid(column=2, row=5, columnspan=1, rowspan=1, sticky="ne")
rack_item_7_frame.grid(column=2, row=6, columnspan=1, rowspan=1, sticky="ne")
rack_item_8_frame.grid(column=2, row=7, columnspan=1, rowspan=1, sticky="ne")
rack_item_9_frame.grid(column=2, row=8, columnspan=1, rowspan=1, sticky="ne")
rack_item_10_frame.grid(column=2, row=9, columnspan=1, rowspan=1, sticky="ne")
rack_item_11_frame.grid(column=2, row=10, columnspan=1, rowspan=1, sticky="ne")
rack_item_12_A_frame.grid(column=2, row=11, columnspan=1, rowspan=1, sticky="ne")
rack_item_12_B_frame.grid(column=2, row=11, columnspan=1, rowspan=1, sticky="nw")

rack_item_1 = tk.Label(action_rack, text="Append Album", bg="#30B5EB", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_1.config(font=("Courier", 40))
rack_item_1.grid(column=2, row=0, columnspan=1, rowspan=1, sticky="ne")

rack_item_2 = tk.Label(action_rack, text="Entry Data", bg="#CF458E", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_2.config(font=("Courier", 40))
rack_item_2.grid(column=2, row=1, columnspan=1, rowspan=1, sticky="ne")

rack_item_3 = tk.Label(action_rack, text="Flac to MP3", bg="#30B5EB", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_3.config(font=("Courier", 40))
rack_item_3.grid(column=2, row=2, columnspan=1, rowspan=1, sticky="ne")

rack_item_4 = tk.Label(action_rack, text="FlacS to MP3S", bg="#CF458E", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_4.config(font=("Courier", 40))
rack_item_4.grid(column=2, row=3, columnspan=1, rowspan=1, sticky="ne")

rack_item_5 = tk.Label(action_rack, text="MetaWeld", bg="#30B5EB", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_5.config(font=("Courier", 40))
rack_item_5.grid(column=2, row=4, columnspan=1, rowspan=1, sticky="ne")

rack_item_6 = tk.Label(action_rack, text="Album Weld", bg="#CF458E", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_6.config(font=("Courier", 40))
rack_item_6.grid(column=2, row=5, columnspan=1, rowspan=1, sticky="ne")

rack_item_7 = tk.Label(action_rack, text="Classic Flac2Mp3 Album Weld", bg="#30B5EB", fg="#2ABF02", relief="flat",
                       pady=15, padx=15)
rack_item_7.config(font=("Courier", 40))
rack_item_7.grid(column=2, row=6, columnspan=1, rowspan=1, sticky="ne")

rack_item_8 = tk.Label(action_rack, text="Classic Mp3 Album Weld", bg="#CF458E", fg="#2ABF02", relief="flat", pady=15,
                       padx=15)
rack_item_8.config(font=("Courier", 40))
rack_item_8.grid(column=2, row=7, columnspan=1, rowspan=1, sticky="ne")

rack_item_9 = tk.Label(action_rack, text="Album Directory", bg="#30B5EB", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_9.config(font=("Courier", 40))
rack_item_9.grid(column=2, row=8, columnspan=1, rowspan=1, sticky="ne")

rack_item_10 = tk.Label(action_rack, text="Visualiser", bg="#CF458E", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_10.config(font=("Courier", 40))
rack_item_10.grid(column=2, row=9, columnspan=1, rowspan=1, sticky="ne")

rack_item_11 = tk.Label(action_rack, text="Sandpit", bg="#30B5EB", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_11.config(font=("Courier", 40))
rack_item_11.grid(column=2, row=10, columnspan=1, rowspan=1, sticky="ne")

rack_item_12_A = tk.Label(action_rack, text="Help", bg="#CF458E", fg="#2ABF02", relief="flat", pady=15, padx=15)
rack_item_12_A.config(font=("Courier", 40))
rack_item_12_A.grid(column=2, row=11, columnspan=1, rowspan=1, sticky="ne")

rack_item_12_B = tk.Label(action_rack, text="Raw Files", bg="#B0A1EE", fg="#2ABF02", pady=15, padx=15)
rack_item_12_B.config(font=("Courier", 40))
rack_item_12_B.grid(column=2, row=11, columnspan=1, rowspan=1, sticky="nw")

rack_item_1_frame.bind("<Button-1>", lambda event: label_click("1"))
rack_item_2_frame.bind("<Button-1>", lambda event: label_click("2"))
rack_item_3_frame.bind("<Button-1>", lambda event: label_click("3"))
rack_item_4_frame.bind("<Button-1>", lambda event: label_click("4"))
rack_item_5_frame.bind("<Button-1>", lambda event: label_click("5"))
rack_item_6_frame.bind("<Button-1>", lambda event: label_click("6"))
rack_item_7_frame.bind("<Button-1>", lambda event: label_click("7"))
rack_item_8_frame.bind("<Button-1>", lambda event: label_click("8"))
rack_item_9_frame.bind("<Button-1>", lambda event: label_click("9"))
rack_item_10_frame.bind("<Button-1>", lambda event: label_click("10"))
rack_item_11_frame.bind("<Button-1>", lambda event: label_click("11"))
rack_item_12_A_frame.bind("<Button-1>", lambda event: label_click("12A"))
rack_item_12_B_frame.bind("<Button-1>", lambda event: label_click("12B"))

# Load album to directory
# View and or clear entry data
# Flac to MP3 one, Flac to MP3 many
# weld one, weld album
# Help, Directory
# Visualiser
# Classic Flac Album to Metadated MP3's album
# Classic MP3's album to Metadated MP3 Ablum


root.mainloop()
