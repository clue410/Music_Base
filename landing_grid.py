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


def label_click(item_id):
    print(f"LABEL CLICK {item_id}")


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
root.update()
root_width = root.winfo_width()
root_height = root.winfo_height()
root.grid_rowconfigure(0, weight=1)
print(root_height)

action_rack = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=(root_width / 2),
                       height=root_height - 35)
welder_logo_frame = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=(root_width / 2),
                             height=root_height)
welder_logo_frame.grid_rowconfigure(0, weight=1)
welder_logo_frame.grid_columnconfigure(1, weight=1)
# album_art_frame = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=400, height=750)
# action_rack.configure(width=root_width/2, height=root_height)
# welder_logo.configure(width=root_width/2, height=root_height)
action_rack.grid_propagate(0)
welder_logo_frame.grid_propagate(0)

action_rack.grid(column=2, row=0, columnspan=1, rowspan=1, sticky="nse")
welder_logo_frame.grid(column=1, row=0, columnspan=1, rowspan=1, sticky="ne")

welder_logo = tk.Frame(welder_logo_frame, bg="#2ABF02", width=(root_width / 2) - 30, height=root_height - 35)
welder_logo.grid(column=1, row=0, sticky="")

total_height = root_height - 35
pad = 17.4
row_height = (total_height - (pad * 3)) // 4

row_width = (root_width // 2) - 30

rack_item_1_frame = tk.Frame(action_rack, bg="#060A13", width=row_width, height=row_height)
rack_item_2_frame = tk.Frame(action_rack, bg="#060A13", width=row_width, height=row_height)
rack_item_3_frame = tk.Frame(action_rack, bg="#060A13", width=row_width, height=row_height)
rack_item_4_frame = tk.Frame(action_rack, bg="#060A13", width=row_width, height=row_height)

rack_item_1_frame.place(x=15, y=pad)
rack_item_2_frame.place(x=15, y=pad + (row_height + pad))
rack_item_3_frame.place(x=15, y=pad + (row_height + pad) * 2)
rack_item_4_frame.place(x=15, y=pad + (row_height + pad) * 3)

sq = int(row_height)
y_pos = 0
x_left = 0
x_mid = (row_width - sq) // 2
x_right = row_width - sq

tool_1 = tk.Frame(rack_item_1_frame, bg="#ffcc7a", width=sq, height=sq)
tool_1.place(x=x_left, y=y_pos)
tool_2 = tk.Frame(rack_item_1_frame, bg="#ffcc7a", width=sq, height=sq)
tool_2.place(x=x_mid, y=y_pos)
tool_3 = tk.Frame(rack_item_1_frame, bg="#ffcc7a", width=sq, height=sq)
tool_3.place(x=x_right, y=y_pos)

tool_4 = tk.Frame(rack_item_2_frame, bg="#ffcc7a", width=sq, height=sq)
tool_4.place(x=x_left, y=y_pos)
tool_5 = tk.Frame(rack_item_2_frame, bg="#ffcc7a", width=sq, height=sq)
tool_5.place(x=x_mid, y=y_pos)
tool_6 = tk.Frame(rack_item_2_frame, bg="#ffcc7a", width=sq, height=sq)
tool_6.place(x=x_right, y=y_pos)

tool_7 = tk.Frame(rack_item_3_frame, bg="#ffcc7a", width=sq, height=sq)
tool_7.place(x=x_left, y=y_pos)
tool_8 = tk.Frame(rack_item_3_frame, bg="#ffcc7a", width=sq, height=sq)
tool_8.place(x=x_mid, y=y_pos)
tool_9 = tk.Frame(rack_item_3_frame, bg="#ffcc7a", width=sq, height=sq)
tool_9.place(x=x_right, y=y_pos)

tool_10 = tk.Frame(rack_item_4_frame, bg="#ffcc7a", width=sq, height=sq)
tool_10.place(x=x_left, y=y_pos)
tool_11 = tk.Frame(rack_item_4_frame, bg="#ffcc7a", width=sq, height=sq)
tool_11.place(x=x_mid, y=y_pos)
tool_12 = tk.Frame(rack_item_4_frame, bg="#ffcc7a", width=sq, height=sq)
tool_12.place(x=x_right, y=y_pos)

raw_files_icon = tk.PhotoImage(file="assets/tool_covers/raw_files_tool_icon.png")
help_icon = tk.PhotoImage(file="assets/tool_covers/help_tool_icon.png")
flac_album_weld_icon = tk.PhotoImage(file="assets/tool_covers/flac_album_weld_tool_icon.png")
album_entires_icon = tk.PhotoImage(file="assets/tool_covers/album_entries_tool_icon.png")
append_album_icon = tk.PhotoImage(file="assets/tool_covers/append_album_tool_icon.png")
bulk_flac_2_mp3_icon = tk.PhotoImage(file="assets/tool_covers/bulk_flac_2_mp3_tool_icon.png")
equaliser_icon = tk.PhotoImage(file="assets/tool_covers/equaliser_tool_icon.png")
flac_2_mp3_icon = tk.PhotoImage(file="assets/tool_covers/flac_2_mp3_tool_icon.png")
flac_album_weld_icon = tk.PhotoImage(file="assets/tool_covers/flac_album_weld_tool_icon.png")
mp3_album_weld_icon = tk.PhotoImage(file="assets/tool_covers/mp3_album_weld_tool_icon.png")
sandpit_icon = tk.PhotoImage(file="assets/tool_covers/sandpit_tool_icon.png")
view_entry_icon = tk.PhotoImage(file="assets/tool_covers/view_entry_data_tool_icon.png")
weld_tool_icon = tk.PhotoImage(file="assets/tool_covers/weld_tool_icon.png")

tk.Label(tool_1, image=weld_tool_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(tool_2, image=flac_album_weld_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(tool_3, image=mp3_album_weld_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")

tk.Label(tool_4, image=view_entry_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(tool_5, image=flac_2_mp3_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(tool_6, image=bulk_flac_2_mp3_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")

tk.Label(tool_7, image=sandpit_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(tool_8, image=equaliser_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(tool_9, image=help_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")

tk.Label(tool_10, image=album_entires_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(tool_11, image=append_album_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")
tk.Label(tool_12, image=raw_files_icon, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")

print(sq)
root.mainloop()
