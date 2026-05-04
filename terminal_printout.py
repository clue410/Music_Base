import subprocess
import tkinter as tk
import os
import re

# class ScrollableTextWindow:
#
#     def __init__(self, root):
#         root = root
#         root.title("Terminal Output")
#         root.geometry("1000x300")
#
#         root.config(background="#060A13")
#
#         frame = tk.Frame(root, bg="#060A13")
#         frame.pack(fill=tk.BOTH, expand=True)
#
#         scrollbar = tk.Scrollbar(frame)
#         scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
#         scrollbar.config(background="#F7F01E", highlightbackground="#FF5F57")
#         scrollbar.pack_forget()

weld_ascii_banner = [" █████   ███   █████          ████      █████",
                     "░░███   ░███  ░░███          ░░███     ░░███",
                     " ░███   ░███   ░███   ██████  ░███   ███████ ",
                     " ░███   ░███   ░███  ███░░███ ░███  ███░░███ ",
                     " ░░███  █████  ███  ░███████  ░███ ░███ ░███ ",
                     "  ░░░█████░█████░   ░███░░░   ░███ ░███ ░███ ",
                     "    ░░███ ░░███     ░░██████  █████░░████████",
                     "     ░░░   ░░░       ░░░░░░  ░░░░░  ░░░░░░░░ "]

# flac_album_ascii_banner =


def add_text(text_widget, message, type):
    print(type)
    if type == "error":
        color = "#FF5F57"  # Red
        print("error")
    elif type == "running":
        color = "#626977"  # Grey
        print("running")
    elif type == "status":
        color = "#F7F01E"  # Yellow
        print("status")
    elif type == "flag":
        color = "#27FEFF"  # Blue
        print("flag")
    else:
        color = '#3C4456'  # Default dark color
        print("default")

    text.config(state=tk.NORMAL)
    start_index = text.index("end-1c")
    text_widget.insert(tk.END, message + '\n')
    end_index = text_widget.index(tk.END)

    unique_tag = f"{color}_{start_index}"
    text_widget.tag_config(unique_tag, foreground=color)
    text_widget.tag_add(unique_tag, start_index, end_index)

    text_widget.config(state=tk.DISABLED)
    text_widget.yview_moveto(1)


def print_banner(text_widget, banner):
    print(banner)
    print_message = ""
    if banner == "weld":
        color = "#FF5F57"  # Red
        print("weld")
        print_message = weld_ascii_banner
    elif banner == "album_weld":
        color = "#626977"  # Grey
        print("weld album")
    elif banner == "flac_2_mp3":
        color = "#F7F01E"  # Yellow
        print("flac 2 mp3")
    else:
        color = '#3C4456'  # Default dark color
        print("logo")
    #     ascii art banners

    text.config(state=tk.NORMAL)
    start_index = text.index("end-1c")
    for line in weld_ascii_banner:
        text_widget.insert(tk.END, line + '\n')
    end_index = text_widget.index(tk.END)

    unique_tag = f"{color}_{start_index}"
    text_widget.tag_config(unique_tag, foreground=color)
    text_widget.tag_add(unique_tag, start_index, end_index)

    text_widget.config(state=tk.DISABLED)
    text_widget.yview_moveto(1)


root = tk.Tk()
root.title("Terminal Output")
root.geometry("1000x300")
root.config(background="#060A13")

frame = tk.Frame(root, bg="#060A13")
frame.pack(fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
scrollbar.config(background="#F7F01E", highlightbackground="#FF5F57")
scrollbar.pack_forget()
text = tk.Text(frame, wrap=tk.WORD, yscrollcommand=scrollbar.set, height=10, state=tk.DISABLED,
               bg="#060A13", fg="white")
text.pack(fill=tk.BOTH, expand=True)

scrollbar.config(command=text.yview)

root.bind('<q>', lambda event: add_text(text, "Status", "status"))
root.bind('<w>', lambda event: add_text(text, "Error", "error"))
root.bind('<e>', lambda event: add_text(text, "Running", "running"))
root.bind('<r>', lambda event: add_text(text, "Flag", "flag"))

root.bind('<a>', lambda event: print_banner(text, "weld"))
root.bind('<s>', lambda event: print_banner(text, "album_weld"))
root.bind('<d>', lambda event: print_banner(text, "flac_2_mp3"))
root.bind('<f>', lambda event: print_banner(text, "logo"))

root.mainloop()
