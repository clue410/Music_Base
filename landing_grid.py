import time
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
from PIL import Image, ImageTk

def click_tool(tool_name):
    print(f"clicked: {tool_name}")


def say_happy_birthday(event=None):
    overlay = tk.Frame(root, bg="#060A13", width=root_width, height=root_height, borderwidth=5, relief="raised")
    overlay.place(x=(row_width / 2), y=(row_height / 2) + 150)
    overlay.lift()

    heading = tk.Frame(overlay, width=950, height=75, bg="#060A13")
    heading.pack(side="top")
    heading_text = tk.Label(heading, text="Say Happy Birthday!", pady=26, font=("Arial", 32, "bold"), bg="#060A13",
                            fg="white")
    heading_text.pack(fill="both", side="top")

    text = tk.Frame(overlay, bg="#C6307B", width=675, height=275)
    text.pack(side="left")
    body_text = tk.Label(text, text="Pretty Hate Machine (Nine Inch Nails) released 29 years ago today!",
                         wraplength=625, pady=26, font=("Arial", 20, "bold"), bg="#060A13",
                         fg="white")
    body_text.pack(fill="x", side="top")

    overlay.update()
    text_length = body_text.winfo_width()
    body_text.config(padx=(625 - text_length) / 2)

    album = tk.Frame(overlay, bg="#2ABF02", width=275, height=275)
    album.pack(side="right")

    original_image = Image.open("assets/temp_styling_files/Nine_Inch_Nails_-_Pretty_Hate_Machine.png")
    resized_image = original_image.resize((276, 276), Image.LANCZOS)
    tk_image = ImageTk.PhotoImage(resized_image)
    img_label = tk.Label(album, image=tk_image, bg="#ffcc7a")
    img_label.image = tk_image
    img_label.place(relx=0.5, rely=0.5, anchor="center")

    close_btn = tk.Button(overlay, text="Say Happy Birthday and Close", font=("Arial", 14, "bold"),
                          activebackground="blue", bg="#C6307B", fg="black", bd=0, cursor="hand2",
                          command=overlay.place_forget)
    close_btn.place(x=row_width - (row_width / 2) + close_btn.winfo_width(), y=row_height + 120)
    close_btn.lift()


root = tkinterdnd2.Tk()
# tool_rack_root = tkinterdnd2.Tk()
# tool_rack_root.withdraw()

root.bind()
root.title("RIPPER")
# root.attributes("-fullscreen", False)
root.attributes("-fullscreen", True)
# root.geometry("1920x1080")
print(f"root state: {root.state()}, root fullscreen: {root.attributes('-fullscreen')}")
# root.resizable(False, False)
root.configure(bg='#060A13')

popup_host = tk.Toplevel(root)
popup_host.withdraw()

root.update()
root_width = root.winfo_width()
root_height = root.winfo_height()
root.grid_rowconfigure(0, weight=1)

print(root_height)
print(root_width)

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
# sq = int(row_height)
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

label1 = (tk.Label(tool_1, image=weld_tool_icon, bg="#ffcc7a"))
label1.place(relx=0.5, rely=0.5, anchor="center")
label1.bind("<Button-1>", lambda e: click_tool("weld"))

label2 = (tk.Label(tool_2, image=flac_album_weld_icon, bg="#ffcc7a"))
label2.place(relx=0.5, rely=0.5, anchor="center")
label2.bind("<Button-1>", lambda e: click_tool("flac album"))

label3 = (tk.Label(tool_3, image=mp3_album_weld_icon, bg="#ffcc7a"))
label3.place(relx=0.5, rely=0.5, anchor="center")
label3.bind("<Button-1>", lambda e: click_tool("mp3 album"))

label4 = (tk.Label(tool_4, image=view_entry_icon, bg="#ffcc7a"))
label4.place(relx=0.5, rely=0.5, anchor="center")
label4.bind("<Button-1>", lambda e: click_tool("view entry data"))

label5 = (tk.Label(tool_5, image=flac_2_mp3_icon, bg="#ffcc7a"))
label5.place(relx=0.5, rely=0.5, anchor="center")
label5.bind("<Button-1>", lambda e: click_tool("flac 2 mp3s"))

label6 = (tk.Label(tool_6, image=bulk_flac_2_mp3_icon, bg="#ffcc7a"))
label6.place(relx=0.5, rely=0.5, anchor="center")
label6.bind("<Button-1>", lambda e: click_tool("flacs 2 mp3s"))

label7 = (tk.Label(tool_7, image=sandpit_icon, bg="#ffcc7a"))
label7.place(relx=0.5, rely=0.5, anchor="center")
label7.bind("<Button-1>", lambda e: click_tool("sandpit"))

label8 = (tk.Label(tool_8, image=equaliser_icon, bg="#ffcc7a"))
label8.place(relx=0.5, rely=0.5, anchor="center")
label8.bind("<Button-1>", lambda e: click_tool("equaliser"))

label9 = (tk.Label(tool_9, image=help_icon, bg="#ffcc7a"))
label9.place(relx=0.5, rely=0.5, anchor="center")
label9.bind("<Button-1>", lambda e: click_tool("help"))

label10 = (tk.Label(tool_10, image=album_entires_icon, bg="#ffcc7a"))
label10.place(relx=0.5, rely=0.5, anchor="center")
label10.bind("<Button-1>", lambda e: click_tool("view albums"))

label11 = (tk.Label(tool_11, image=append_album_icon, bg="#ffcc7a"))
label11.place(relx=0.5, rely=0.5, anchor="center")
label11.bind("<Button-1>", lambda e: click_tool("add album"))

label12 = (tk.Label(tool_12, image=raw_files_icon, bg="#ffcc7a"))
label12.place(relx=0.5, rely=0.5, anchor="center")
label12.bind("<Button-1>", lambda e: click_tool("view raw directory"))

print(sq)
# TODO abort fullscreen evil evil
# nevermind were so back
say_happy_birthday()
root.mainloop()
