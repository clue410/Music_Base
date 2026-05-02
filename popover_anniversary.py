import tkinter as tk
import customtkinter
from tkinter import messagebox as mb
import tkinterdnd2
from PIL import Image, ImageTk

# TODO ponder on it, dont think  i need this anymo
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

root_grid.grid_propagate(0)

heading = tk.Frame(root, width=950, height=75)
heading.pack(side="top")
heading_text = tk.Label(heading, text="Say Happy Birthday!", pady=26,font=("Arial", 32, "bold"), bg="#060A13")
heading_text.pack(fill="both", side="top")

text = tk.Frame(root, bg="#C6307B", width=675, height=275)
text.pack(side="left")
body_text = tk.Label(text, text="The Downward Spiral (Nine Inch Nails) released 29 years ago today!", wraplength=625, pady=26,font=("Arial", 16, "bold"))
body_text.pack(fill="x", side="top")

root.update()
print(body_text.winfo_width())
text_length = body_text.winfo_width()
body_text.config(padx= (625-text_length)/2)

album = tk.Frame(root, bg="#2ABF02", width=275, height=275)
album.pack(side="right")

original_image = Image.open("assets/temp_styling_files/Nine_Inch_Nails_-_Pretty_Hate_Machine.png")
resized_image = original_image.resize((276, 276), Image.LANCZOS)
tk_image = ImageTk.PhotoImage(resized_image)
tk.Label(album, image=tk_image, bg="#ffcc7a").place(relx=0.5, rely=0.5, anchor="center")





root.bind("<c>", print_values)

root.mainloop()
