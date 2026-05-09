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

flac_album_ascii_banner = [
    "888~~  888          e       e88~-_             e      888     888~~\\  888   |      e    e      ",
    "888___ 888         d8b     d888   \\           d8b     888     888   | 888   |     d8b  d8b     ",
    "888    888        /Y88b    8888              /Y88b    888     888 _/  888   |    d888bdY88b    ",
    "888    888       /  Y88b   8888             /  Y88b   888     888  \\  888   |   / Y88Y Y888b   ",
    "888    888      /____Y88b  Y888   /        /____Y88b  888     888   | Y88   |  /   YY   Y888b  ",
    "888    888____ /      Y88b  \"88_ -        /      Y88b 888____ 888__ / \"88__/  /          Y888b ", ]

mp3_album_ascii_banner = [
    r'  __   __  ___   _______  ___       ________            __      ___       _______   ____  ____  ___      ___ ',
    r' |"  |/  \|  "| /"     "||"  |     |"      "\          /""\    |"  |     |   _  "\ ("  _||_ " ||"  \    /"  |',
    r" |'  /    \:  |(: ______)||  |     (.  ___  :)        /    \   ||  |     (. |_)  :)|   (  ) : | \   \  //   |",
    r" |: /'        | \/    |  |:  |     |: \   ) ||       /' /\  \  |:  |     |:     \/ (:  |  | . ) /\\  \/.    |",
    r"  \//  /\'    | // ___)_  \  |___  (| (___\ ||      //  __'  \  \  |___  (|  _  \\  \\ \__/ // |: \.        |",
    r"  /   /  \\   |(:      \"|( \_|:  \ |:       :)     /   /  \\  \( \_|:  \ |: |_)  :) /\\ __ //\ |.  \    /:  |",
    r' |___/    \___| \_______) \_______)(________/     (___/    \___)\_______)(_______/ (__________)|___|\__/|___|',
]

flac_2_mp3_ascii_banner = [r'    ________    ___   ______   ___      __  _______ _____',
                           r'   / ____/ /   /   | / ____/  |__ \    /  |/  / __ \__  /',
                           r'  / /_  / /   / /| |/ /       __/ /   / /|_/ / /_/ //_ < ',
                           r' / __/ / /___/ ___ / /___    / __/   / /  / / ____/__/ / ',
                           r'/_/   /_____/_/  |_\____/   /____/  /_/  /_/_/   /____/  ']

bulk_flac_2_mp3_ascii_banner = [
    r'     ____  __  ____    __ __    ________    ___   ______   ___      __  _______ _____',
    r'    / __ )/ / / / /   / //_/   / ____/ /   /   | / ____/  |__ \    /  |/  / __ \__  /',
    r'   / __  / / / / /   / ,<     / /_  / /   / /| |/ /       __/ /   / /|_/ / /_/ //_ < ',
    r'  / /_/ / /_/ / /___/ /| |   / __/ / /___/ ___ / /___    / __/   / /  / / ____/__/ / ',
    r' /_____/\____/_____/_/ |_|  /_/   /_____/_/  |_\____/   /____/  /_/  /_/_/   /____/  ']

entry_data_ascii_banner = [
    '                                                                                                                   ',
    '                                                                         _______                                   ',
    "        __.....__        _..._                                           \\  ___ `\'.                                ",
    "    .-\'\'         \'.    .\'     \'.                .-.          .-           \' |--.\\  \\                               ",
    '   /     .-\'\'\"\'-.  `. .   .-.   .     .|  .-,.--.\\ \\        / /           | |    \\  \'               .|             ',
    "  /     /________\\   \\|  \'   \'  |   .\' |_ |  .-. |\\ \\      / /            | |     |  \'    __      .\' |_     __     ",
    "  |                  ||  |   |  | .\'     || |  | | \\ \\    / /             | |     |  | .:--.\'.  .\'     | .:--.\'.   ",
    "  \\    .-------------\'|  |   |  |\'--.  .-\'| |  | |  \\ \\  / /              | |     \' .\'/ |   \\ |\'--.  .-\'/ |   \\ |  ",
    "   \\    \'-.____...---.|  |   |  |   |  |  | |  \'-    \\ `  /               | |___.\' /\' `\" __ | |   |  |  `\" __ | |  ",
    "    `.             .\' |  |   |  |   |  |  | |         \\  /               /_______.\'/   .\'.\'\'| |   |  |   .\'.\'\'| |  ",
    "      `\'\'-...... -\'   |  |   |  |   |  \'.\'| |         / /                \\_______|/   / /   | |_  |  \'.\'/ /   | |_ ",
    "                      |  |   |  |   |   / |_|     |`-\' /                              \\ \\._,\\ \'/  |   / \\ \\._,\\ \'/ ",
    "                      \'--\'   \'--\'   `\'-\'           \'..\'                                `--\'  `\"   `'-'   `--\'  `\"  "]

success_ascii_banner = ["  _____ _____ _____ _____ _____ _____ _____ ",
                        " |   __|  |  |     |     |   __|   __|   __|",
                        " |__   |  |  |   --|   --|   __|__   |__   |",
                        " |_____|_____|_____|_____|_____|_____|_____|"]

#
completed_ascii_banner = [
    " _____ _____ _____ _____ _____ _____ _____    _____ _____ _____ _____ __    _____ _____ _____ ",
    "|  _  | __  |     |     |   __|   __|   __|  |     |     |     |  _  |  |  |   __|_   _|   __|",
    "|   __|    -|  |  |   --|   __|__   |__   |  |   --|  |  | | | |   __|  |__|   __| | | |   __|",
    "|__|  |__|__|_____|_____|_____|_____|_____|  |_____|_____|_|_|_|__|  |_____|_____| |_| |_____|"]

failure_ascii_banner = [" _____ _____ _____ __    _____ _____ _____ ",
                        "|   __|  _  |     |  |  |  |  | __  |   __|",
                        "|   __|     |-   -|  |__|  |  |    -|   __|",
                        "|__|  |__|__|_____|_____|_____|__|__|_____|"]

welcome_ascii_banner = [
    "   _____                ______    ____              _____           _____         ______  _______        ______   ",
    "  |\\    \\   _____   ___|\\     \\  |    |         ___|\\    \\     ____|\\    \\       |      \\/       \\   ___|\\     \\  ",
    "  | |    | /    /| |     \\     \\ |    |        /    /\\   \\ \\   /     /\\    \\     /          /\\     \\ |     \\     \\ ",
    "  \\/     / |    || |     ,_____/||    |       |    |  |    | /     /  \\    \\   /     /\\   / /\\     ||     ,_____/|",
    "  /     /_  \\   \\/ |     \\--\'\\_|/|    |  ____ |    |  |____||     |    |    | /     /\\ \\_/ / /    /||     \\--\'\\_|/",
    " |     // \\  \\   \\ |     /___/|  |    | |    ||    |   ____ |     |    |    ||     |  \\|_|/ /    / ||     /___/|  ",
    " |    |/   \\ |    ||     \\____|\\ |    | |    ||    |  |    ||\\     \\  /    /||     |       |    |  ||     \\____|\\ ",
    " |\\ ___/\\   \\|   /||____ \'     /||____|/____/||\\ ___\\/    /|| \\_____\\/____/ ||\\____\\       |____|  /|____ \'     /|",
    " | |   | \\______/ ||    /_____/ ||    |     ||| |   /____/ | \\ |    ||    | /| |    |      |    | / |    /_____/ |",
    "  \\|___|/\\ |    | ||____|     | /|____|_____|/ \\|___|    | /  \\|____||____|/  \\|____|      |____|/  |____|     | /",
    "     \\(   \\|____|/   \\( |_____|/   \\(    )/      \\( |____|/      \\(    )/        \\(          )/       \\( |_____|/ ",
    "      \'      )/       \'    )/       \'    \'        \'   )/          \'    \'          \'          \'         \'    )/    ",
    "             \'             \'                          \'                                                     \'     "]


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
    elif banner == "flac_album_weld":
        color = "#626977"  # Grey
        print_message = flac_album_ascii_banner
        print("weld flac album")
    elif banner == "album_weld":
        color = "#626977"  # Grey
        print_message = mp3_album_ascii_banner
        print("weld album")
    elif banner == "flac_2_mp3":
        color = "#F7F01E"  # Yellow
        print_message = flac_2_mp3_ascii_banner
        print("flac 2 mp3")
    elif banner == "bulk_flac_2_mp3":
        color = "#F7F01E"  # Yellow
        print_message = bulk_flac_2_mp3_ascii_banner
        print("flac 2 mp3")
    elif banner == "entry_data":
        color = "#FF5F57"  # Red
        print("weld")
        print_message = entry_data_ascii_banner
    elif banner =="welcome":
        color = "#27FEFF"
        print("welcome")
        print_message = welcome_ascii_banner
    else:
        color = '#3C4456'  # Default dark color
        print("logo")
    #     ascii art banners

    text.config(state=tk.NORMAL)
    start_index = text.index("end-1c")
    for line in print_message:
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
root.bind('<d>', lambda event: print_banner(text, "flac_album_weld"))
root.bind('<f>', lambda event: print_banner(text, "flac_2_mp3"))
root.bind('<g>', lambda event: print_banner(text, "logo"))
root.bind('<h>', lambda event: print_banner(text, "bulk_flac_2_mp3"))
root.bind('<j>', lambda event: print_banner(text, "entry_data"))
root.bind('<k>', lambda event: print_banner(text, "welcome"))

root.mainloop()
