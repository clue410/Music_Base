import tkinter as tk
import customtkinter
from tkinter import messagebox as mb
import tkinterdnd2


# make as class later

def print_values(event):
    print(root.winfo_width())
    print(root.winfo_height())


root = tkinterdnd2.Tk()
tool_rack_root = tkinterdnd2.Tk()
tool_rack_root.withdraw()

root.bind()
root.title("POPOVER")
root.geometry("950x350")
root.resizable(True, True)
# root.resizable(False, False)
root.configure(bg='#060A13')
root_width = root.winfo_width()
root_height = root.winfo_height()


heading_frame = tk.Frame(root,bg="#060A13", highlightbackground="#0854ff", relief="sunken", width=root_width,
                     height=50)

root_grid = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=root_width,
                     height=root_height - 50)

#
# album_cover_frame = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=(root_width / 2),
#                        height=root_height)
# text_frame = tk.Frame(root, bg="#060A13", highlightbackground="#FBF300", relief="flat", width=(root_width / 2),
#                              height=root_height)

# text_frame.grid_columnconfigure(0, weight=1)
# album_cover_frame.grid_rowconfigure(1, weight=1)
# root_grid.grid_columnconfigure(0, weight=1)
# root_grid.grid_columnconfigure(1, weight=1)

# text_frame.grid_propagate(0)
# album_cover_frame.grid_propagate(1)
root_grid.grid_propagate(0)
#
# text_frame.grid(column=1, row=0, columnspan=1, rowspan=1, sticky="ne")
# album_cover_frame.grid(column=2, row=0, columnspan=1, rowspan=1, sticky="ne")

# album_from_JSON = tk.Frame(album_cover_frame, bg="#2ABF02", width=root.winfo_width(), height=root.winfo_height())
# album_from_JSON.grid(column=1, row=0, sticky="")
#
# texttext = tk.Frame(text_frame, bg="#C6307B", width=root.winfo_width(), height=root.winfo_height())
# texttext.grid(column=2, row=0, sticky="")


#

heading = tk.Frame(root, width=950, height=75)
heading.pack(side="top")
heading_text = tk.Label(heading, text="Say Happy Birthday!", pady=26,font=("Arial", 16, "bold"))
heading_text.pack(fill="both", side="top")

text = tk.Frame(root, bg="#C6307B", width=675, height=275)
text.pack(side="left")

album = tk.Frame(root, bg="#2ABF02", width=275, height=275)
album.pack(side="right")





root.bind("<c>", print_values)

root.mainloop()
