# TODO V moved from old ripper, redo ui, clean funcs etc etc, get rid of bloat etc etc and then frankenstein back together
# import tkinter as tk
# from tkinter import messagebox as mb
#
# from tinytag import TinyTag
# from tkinterdnd2 import DND_FILES, TkinterDnD
# from PIL import Image, ImageTk  # Import Pillow for image handling
# import tkinterdnd2
# from tkinter import ttk, messagebox, filedialog
# import threading
# import colorsys
# from matplotlib import image as img
# from scipy.cluster.vq import whiten, kmeans
# import pandas as pd
# import numpy as np
# from PIL import ImageDraw
# import json
# import os
#
#
# class Album_Brains:
#     def __init__(self, data):
#         self.data = data
#
#
# genre_textual = (
#     "A Cappella", "Abstract", "Acid Jazz", "Acid Punk", "Acid", "Acoustic", "Afro-Punk", "Alt. Rock", "Alternative",
#     "Ambient",
#     "Anime", "Art Rock", "Audio Theatre", "Audiobook", "Avantgarde", "Ballad", "Baroque", "Bass", "Beat", "Bebop",
#     "Bhangra", "Big Band",
#     "Big Beat", "Black Metal", "Bluegrass", "Blues", "Booty Bass", "Breakbeat", "BritPop", "Cabaret", "Celtic",
#     "Chamber Music",
#     "Chanson", "Chillout", "Chorus", "Christian Gangsta Rap", "Christian Rap", "Christian Rock", "Classic Rock",
#     "Classical",
#     "Club", "Club-House", "Comedy", "Contemporary Christian", "Country", "Crossover", "Cult", "Dance Hall", "Dance",
#     "Darkwave",
#     "Death Metal", "Disco", "Downtempo", "Dream", "Drum & Bass", "Drum Solo", "Dub", "Dubstep", "Duet",
#     "Easy Listening",
#     "EBM",
#     "Eclectic", "Electro", "Electroclash", "Electronic", "Emo", "Ethnic", "Euro-House", "Euro-Techno", "Eurodance",
#     "Experimental",
#     "Fast-Fusion", "Folk", "Folk-Rock", "Folklore", "Freestyle", "Funk", "Fusion", "G-Funk", "Game", "Gangsta Rap",
#     "Garage Rock",
#     "Garage", "Global", "Goa", "Gospel", "Gothic Rock", "Gothic", "Grunge", "Hard Rock", "Hardcore", "Heavy Metal",
#     "Hip-Hop", "House",
#     "Humour", "IDM", "Illbient", "Indie Rock", "Indie", "Industrial", "Industro-Goth", "Instrumental Pop",
#     "Instrumental Rock",
#     "Instrumental", "Jam Band", "Jazz", "Jazz+Funk", "JPop", "Jungle", "Krautrock", "Latin", "Leftfield", "Lo-Fi",
#     "Lounge",
#     "Math Rock",
#     "Meditative", "Merengue", "Metal", "Musical", "National Folk", "Native American", "Neoclassical",
#     "Neue Deutsche Welle",
#     "New Age",
#     "New Romantic", "New Wave", "Noise", "None", "Nu-Breakz", "Oldies", "Opera", "Other", "Podcast", "Polka",
#     "Polsk Punk",
#     "Pop",
#     "Pop-Folk", "Pop/Funk", "Porn Groove", "Post-Punk", "Post-Rock", "Power Ballad", "Pranks", "Primus",
#     "Progressive Rock",
#     "Psybient",
#     "Psychedelic Rock", "Psychedelic", "Psytrance", "Punk Rock", "Punk", "R&B", "Rap", "Rave", "Reggae", "Retro",
#     "Revival",
#     "Rhythmic Soul", "Rock & Roll", "Rock", "Salsa", "Samba", "Satire", "Shoegaze", "Showtunes", "Ska", "Slow Jam",
#     "Slow Rock",
#     "Sonata", "Soul", "Sound Clip", "Soundtrack", "Southern Rock", "Space Rock", "Space", "Speech", "Swing",
#     "Symphonic Rock",
#     "Symphony", "Synthpop", "Tango", "Techno", "Techno-Industrial", "Terror", "Thrash Metal", "Top ", "Trailer",
#     "Trance",
#     "Tribal",
#     "Trip-Hop", "Trop Rock", "Vocal", "World Music")
# genre_numerical = (
#     123, 148, 74, 73, 34, 99, 133, 40, 20, 26, 145, 149, 184, 183, 90, 116, 150, 41, 135, 85, 151, 96, 152, 138, 89, 0,
#     107,
#     153, 132, 65, 88,
#     104, 102, 154, 97, 136, 61, 141, 1, 32, 112, 128, 57, 140, 2, 139, 58, 125, 3, 50, 22, 4, 155, 55, 127, 122, 156,
#     189,
#     120, 98, 157, 158,
#     159, 160, 52, 161, 48, 124, 25, 54, 162, 84, 80, 81, 115, 119, 5, 30, 188, 36, 59, 190, 163, 164, 126, 38, 91, 49,
#     6,
#     79, 129, 137, 7, 35,
#     100, 165, 166, 187, 131, 19, 167, 46, 47, 33, 168, 8, +29, 146, 63, 169, 86, 170, 71, 171, 172, 45, 142, 9, 77, 82,
#     64,
#     182, 185, 10, 173,
#     66, 39, 255, 174, 11, 103, 12, 186, 75, 134, 13, 53, 62, 109, 175, 176, 117, 23, 108, 92, 191, 93, 67, 177, 121, 43,
#     14,
#     15, 68, 16, 76, 87,
#     118, 78, 17, 143, 114, 110, 178, 69, 21, 111, 95, 105, 42, 37, 24, 56, 179, 44, 101, 83, 94, 106, 147, 113, 18, 51,
#     130,
#     144, 4060, 70, 31, 72,
#     27, 180, 28, 181)
#
# album_art_file_reference = ":P"
#
# order_entries = []
# drop_song_entries = []
# drop_title_entries = []
#
# entry_triplets = []  # (drop_entry, title_entry, order_entry)
#
# populated_entries = 0;
#
# output_directory = "bacon bacon bacon"
#
# file_path = "albums.json"
# # Load existing data if the file exists
# if os.path.exists(file_path):
#     with open(file_path, "r") as file:
#         try:
#             albums = json.load(file)
#         except json.JSONDecodeError:
#             albums = []  # If file is empty or corrupted, start fresh
# else:
#     albums = []
#
#
# def on_select(event):
#     selected_option = genre_dropdown.get()
#     genre_index = genre_textual.index(selected_option)
#     print(f"Selected: {selected_option} -> {genre_numerical[genre_index]}({genre_textual[genre_index]})")
#
#
# def dropSong(event):
#     print("dropped")
#     widget = event.widget
#     path = event.data.strip("{}").strip("'")  # Clean the file path
#     print(f"Dropped SONG path: {path}")
#     if path.lower().endswith(('mp3')) or path.lower().endswith(('flac')):
#     # if path.lower().endswith(('mp3')):
#         print("nice")
#
#         # here
#         filename = os.path.basename(path)
#         for drop_entry, title_entry, order_entry in entry_triplets:
#             if drop_entry == widget:
#                 drop_entry.delete(0, "end")
#                 drop_entry.insert(0, path)
#
#                 title_entry.delete(0, "end")
#                 cleaned_string = filename.replace("_"," ")
#                 cleaned_string2 = cleaned_string.replace("-"," ")
#                 if(path.lower().endswith(('mp3'))):
#                     title_entry.insert(0, cleaned_string2[:-4])
#                 if(path.lower().endswith(('flac'))):
#                     title_entry.insert(0, cleaned_string2[:-5])
#                 # title_entry.insert(0, filename[:-4])
#                 break
#         extract_metadata(path)
#
#     else:
#         mb.showerror(title="Nuh uh", message="Not an mp3 or flac dumbass")
#         # mb.showerror(title="Nuh uh", message="Not an mp3 dumbass")
#
#
# collected_duration = 0
#
#
# def extract_metadata(file_path):
#     audio = TinyTag.get(file_path)
#     global populated_entries
#     global collected_duration
#     populated_entries = 0
#     metadata = audio.as_dict()
#     print(metadata)
#     output = str(metadata["title"]).replace("['", "").replace("']", "")
#     duration = int(metadata["duration"])
#
#     collected_duration += duration
#     minutes, remaining_seconds = divmod(duration, 60)
#     print(f"{minutes}:{remaining_seconds:.0f}")
#     for triplet in entry_triplets:
#         # (drop_entry, title_entry, order_entry)
#         if (triplet[1].get() != "" and triplet[2].get() != ""):
#             print(f"file : {triplet[0].get()}")
#             print(f"title : {triplet[1].get()}")
#             print(f"order : {triplet[2].get()}")
#             # populated_entries +=1
#             populated_entries = populated_entries + 1
#         # global populated_entries populated_entries +1;
#
#     song_count_label_static.config(state="normal")  # allow editing
#     song_count_label_static.delete(0, "end")
#     song_count_label_static.insert(0, populated_entries)
#     song_count_label_static.config(state="readonly")
#
#     runtime_label_static.config(state="normal")  # allow editing
#     runtime_label_static.delete(0, "end")
#     minutes, remaining_seconds = divmod(collected_duration, 60)
#     print(f"{minutes}:{remaining_seconds:.0f}")
#     runtime_label_static.insert(0, f"{minutes} minutes, {remaining_seconds:.0f} seconds")
#     print(populated_entries)
#     runtime_label_static.config(state="readonly")
#
#
# #
# #     print("MOEW")
# # except:
# #     # title_entry.insert(0, "nan")
# #     print("An exception occurred : No valid title")
#
#
# def dropArt(event):
#     art_path = event.data.strip("{}").strip("'")  # Clean the file path
#     print(f"Dropped image path: {art_path}")
#
#     if art_path.lower().endswith(('.png', '.jpg', '.jpeg')):
#         try:
#             # Open and resize the image to fit the frame (400x400)
#             image = Image.open(art_path)
#             image = image.resize((396, 396), Image.LANCZOS)
#             photo = ImageTk.PhotoImage(image)
#             image.save("album_art.jpg")
#
#             # Replace image in label
#             album_cover_label.config(image=photo)
#             album_cover_label.image = photo  # Keep a reference to avoid garbage collection
#
#             # Optionally update reference field
#             art_ref.config(state="normal")
#             art_ref.delete(0, tk.END)
#             art_ref.insert(0, art_path)
#             art_ref.config(state="readonly")
#
#
#             print("Image successfully loaded and displayed.")
#
#             start_spinner()
#             # threading.Thread(target=lambda: get_dominant_colours(art_path), daemon=True).start()
#
#             # Start background thread for color extraction
#             threading.Thread(target=lambda: get_dominant_colours(art_path), daemon=True).start()
#             order_entry_alpha.delete(0, 'end')
#             order_entry_alpha.insert(0, 1)
#
#         except Exception as e:
#             print(f"Error loading image: {e}")
#             mb.showerror("Image Error", f"Could not load image: {e}")
#
#     else:
#         mb.showerror(title="Nuh uh", message="Not an image dummy")
#
#
# spinner_frames = []
# spinner_label = None
# spinner_animating = False
#
#
# def generate_spinner_frames(size=64, dot_radius=6, frame_count=12):
#     global spinner_frames
#     spinner_frames = []
#     center = size // 2
#
#     for i in range(frame_count):
#         image = Image.new("RGBA", (size, size), (0, 0, 0, 0))
#         draw = ImageDraw.Draw(image)
#
#         angle = 2 * np.pi * i / frame_count
#         x = center + int(center * 0.7 * np.cos(angle))
#         y = center + int(center * 0.7 * np.sin(angle))
#
#         draw.ellipse((x - dot_radius, y - dot_radius, x + dot_radius, y + dot_radius), fill=(255, 255, 255, 255))
#         spinner_frames.append(ImageTk.PhotoImage(image))
#
#
# # TODO kill if it takes more than 3 (?) minutes
# def get_dominant_colours(image_path, num_colours=6):
#     print("Extracting dominant colours...")
#
#     # Load and optionally downsample image
#     image_data = img.imread(image_path)
#     if image_data.shape[0] > 200 or image_data.shape[1] > 200:
#         image_data = image_data[::2, ::2, :]  # downsample for speed
#     # TODO put in a try-catch becoz of VVV
#
#     # File "/Users/maril/Desktop/music_ripper/read_on_mass_from_csv.py", line 215, in get_dominant_colours
#     # image_data = image_data[::2, ::2, :]  # downsample for speed
#     #   ~~~~~~~~~~^^^^^^^^^^^^^
#     # IndexError: too many indices for array: array is 2-dimensional, but 3 were indexed
#
#     pixels = []
#     for row in image_data:
#         for pixel in row:
#             r, g, b = pixel[:3]
#             if max(r, g, b) <= 1.0:
#                 r, g, b = [int(c * 255) for c in (r, g, b)]
#             else:
#                 r, g, b = int(r), int(g), int(b)
#             pixels.append([r, g, b])
#
#     pixels = np.array(pixels)
#     df = pd.DataFrame(pixels, columns=['red', 'green', 'blue'])
#
#     # Normalize for clustering
#     df['scaled_red'] = whiten(df['red'])
#     df['scaled_green'] = whiten(df['green'])
#     df['scaled_blue'] = whiten(df['blue'])
#
#     # KMeans clustering
#     cluster_centers, _ = kmeans(df[['scaled_red', 'scaled_green', 'scaled_blue']], num_colours)
#
#     red_std, green_std, blue_std = df[['red', 'green', 'blue']].std()
#
#     # Unwhiten cluster centers
#     unwhitened = [
#         (
#             int(c[0] * red_std),
#             int(c[1] * green_std),
#             int(c[2] * blue_std)
#         ) for c in cluster_centers
#     ]
#
#     def brightness(rgb):
#         r, g, b = rgb
#         return 0.2126 * r + 0.7152 * g + 0.0722 * b
#
#     def vibrance(rgb):
#         r, g, b = [x / 255 for x in rgb]
#         h, s, v = colorsys.rgb_to_hsv(r, g, b)
#         return s  # Saturation
#
#     # 1. Get background color (darkest)
#     unwhitened_sorted = sorted(unwhitened, key=brightness)
#     bg_color = unwhitened_sorted[0]
#
#     # 2. Filter out background and select vibrant ones
#     remaining_colors = [c for c in unwhitened if c != bg_color]
#
#     contrast_threshold = 50  # Minimum brightness diff from background
#
#     def has_contrast(c):
#         return abs(brightness(c) - brightness(bg_color)) > contrast_threshold
#
#     # Filter by vibrance and contrast
#     contrasty_vibrant = [
#         c for c in sorted(remaining_colors, key=vibrance, reverse=True)
#         if has_contrast(c)
#     ]
#
#     # If fewer than 3, manually brighten the top vibrant ones
#     while len(contrasty_vibrant) < 3:
#         needed = 3 - len(contrasty_vibrant)
#         candidates = [c for c in sorted(remaining_colors, key=vibrance, reverse=True) if c not in contrasty_vibrant]
#         for c in candidates[:needed]:
#             # Convert to HLS and boost lightness
#             r, g, b = [x / 255 for x in c]
#             h, l, s = colorsys.rgb_to_hls(r, g, b)
#             l = min(1.0, l + 0.3)  # brighten
#             r_b, g_b, b_b = colorsys.hls_to_rgb(h, l, s)
#             brightened = (int(r_b * 255), int(g_b * 255), int(b_b * 255))
#             contrasty_vibrant.append(brightened)
#
#     accent_colors = contrasty_vibrant[:3]
#     final_palette = [bg_color] + accent_colors
#     print("Palette:", final_palette)
#     remake_pallete(final_palette)
#     stop_spinner()
#
#
# def start_spinner():
#     global spinner_animating
#     spinner_animating = True
#     spinner_label.lift()
#     animate_spinner(0)
#
#
# def stop_spinner():
#     global spinner_animating
#     spinner_animating = False
#     spinner_label.lower()
#
#
# def animate_spinner(frame_index):
#     if not spinner_animating:
#         return
#     frame = spinner_frames[frame_index]
#     spinner_label.config(image=frame)
#     spinner_label.image = frame
#     root.after(100, lambda: animate_spinner((frame_index + 1) % len(spinner_frames)))
#
#
# def remake_pallete(final_palette):
#     print("remake pallete")
#     darkest_colour = final_palette[0]
#     text_editable = final_palette[1]
#     text_static = final_palette[2]
#     accent = final_palette[3]
#
#     darkest_colour_hex = f"#{darkest_colour[0]:02X}{darkest_colour[1]:02X}{darkest_colour[2]:02X}"
#     text_editable_hex = f"#{text_editable[0]:02X}{text_editable[1]:02X}{text_editable[2]:02X}"
#     text_static_hex = f"#{text_static[0]:02X}{text_static[1]:02X}{text_static[2]:02X}"
#     accent_hex = f"#{accent[0]:02X}{accent[1]:02X}{accent[2]:02X}"
#
#     root.update()
#     root.config(bg=darkest_colour_hex)
#     album_art_frame.config(bg=darkest_colour_hex)
#     entry_frame.config(bg=darkest_colour_hex)
#     year_label_static.config(fg=text_editable_hex, bg=darkest_colour_hex)
#     album_label_static.config(fg=text_editable_hex, bg=darkest_colour_hex)
#     artist_label_static.config(fg=text_editable_hex, bg=darkest_colour_hex)
#     song_count_label_static.config(fg=text_editable_hex, bg=darkest_colour_hex)
#     volume_to_equalise.config(fg=text_editable_hex, bg=darkest_colour_hex)
#     runtime_label_static.config(fg=text_static_hex, bg=darkest_colour_hex)
#     album_art.config(bg=accent_hex)
#     button_row.config(bg=darkest_colour_hex)
#     execute_button.config(fg=text_static_hex)
#     clear_button.config(fg=text_static_hex)
#     clear_songs_button.config(fg=text_static_hex)
#     move_directories_button.config(fg=text_static_hex)
#     genre_dropdown.config(foreground=accent_hex)
#     spinner_label.config(bg=darkest_colour_hex)
#     art_ref.config(bg=darkest_colour_hex, fg=darkest_colour_hex)
#     album_cover_label.config(bg=darkest_colour_hex)  # or accent_hex if you want
#
#     directory_static.config(fg=accent_hex, bg=darkest_colour_hex)
#
#     for x in range(0, 15):
#         order_label_pallete = entry_frame.nametowidget(f"order_label-{x}")
#         order_entry_pallete = entry_frame.nametowidget(f"order_entry-{x}")
#         title_label_pallete = entry_frame.nametowidget(f"title-label-{x}")
#         title_entry_pallete = entry_frame.nametowidget(f"title_entry-{x}")
#         drop_song_pallete = entry_frame.nametowidget(f"drop_song-{x}")
#
#         order_label_pallete.config(fg=text_editable_hex, bg=darkest_colour_hex)
#         title_entry_pallete.config(fg=text_editable_hex, bg=darkest_colour_hex, highlightbackground=text_static_hex)
#         order_entry_pallete.config(fg=text_editable_hex, bg=darkest_colour_hex, highlightbackground=text_static_hex)
#         title_label_pallete.config(fg=text_editable_hex, bg=darkest_colour_hex)
#         drop_song_pallete.config(fg=text_editable_hex, bg=darkest_colour_hex, highlightbackground=accent_hex)
#
#
# class MockEvent:
#     album_art_reference: str
#
#     def __init__(self, data):
#         self.data = data
#
#
# class DropdownPopup(tk.Toplevel):
#     def __init__(self, master, options, album_dict, artist_entry, year_entry, album_entry):
#         super().__init__(master)
#         self.title("Select an Option")
#         self.geometry("600x75")
#
#         self.album_dict = album_dict  # Store reference to original data
#         self.artist_entry = artist_entry
#         self.year_entry = year_entry
#         self.album_entry = album_entry
#
#         self.combobox = ttk.Combobox(self, values=list(album_dict.keys()))
#         self.combobox.pack(padx=20, pady=20)
#         self.combobox.bind("<<ComboboxSelected>>", self.on_select)
#         self.combobox.config(width=400, height=50)
#         self.combobox.focus()
#
#     """On Tab : When Album Selected, Populate Fields with Selected Details"""
#
#     def on_select(self, event):
#         selected_option = self.combobox.get()
#         album_data = self.album_dict.get(selected_option)
#         # print(str(album_data["uses"]) + " <-- USES ")
#         # save_frequent_cover(album_data["album_name"], album_data["artist"])
#
#         if album_data:
#             # Populate fields
#             self.artist_entry.delete(0, tk.END)
#             self.artist_entry.insert(0, album_data["artist"])
#
#             self.year_entry.delete(0, tk.END)
#             self.year_entry.insert(0, album_data["year"])
#
#             self.album_entry.delete(0, tk.END)
#             self.album_entry.insert(0, album_data["album_name"])
#
#             print(album_data["genre_code"])
#             index_of_genre = genre_numerical.index(album_data["genre_code"])
#             print(index_of_genre)
#             genre_dropdown.set(genre_textual[index_of_genre])
#         self.destroy()
#
#
# def on_tab(root, albums, artist_entry, year_entry, album_entry):
#     artist = artist_entry.get().strip()
#     year = year_entry.get().strip()
#     album_name = album_entry.get().strip()
#
#     filtered_albums = filter_albums(albums, artist, year, album_name)
#     album_dict = format_albums(filtered_albums)
#
#     if album_dict:
#         DropdownPopup(root, album_dict, album_dict, artist_entry, year_entry, album_entry)
#     else:
#         mb.showerror(title="None Found", message="No matching albums found :-(")
#
#
# def format_albums(album_list):
#     """Convert JSON album entries to formatted strings and return a dictionary mapping."""
#     formatted_options = {}
#     for album in album_list:
#         formatted_text = f"{album['album_name']} ({album['artist']}) {album['year']}"
#         formatted_options[formatted_text] = album  # Map formatted text to original JSON
#     return formatted_options
#
#
# """Filter for albums that match entered fields"""
#
#
# def filter_albums(albums, artist, year, album_name):
#     return [
#         album for album in albums
#         if (not artist or artist.lower() in album['artist'].lower()) and
#            (not year or year == album['year']) and
#            (not album_name or album_name.lower() in album['album_name'].lower())
#     ]
#
#
# def on_entry_change(*args):
#     # new_value = element.get()
#     new_value = order_entry_alpha.get()
#     print("New value :", new_value)
#     counter = int(new_value) + 1
#
#     for x in range(1, len(entry_triplets)):
#         entry_triple = entry_triplets[x]
#         order_entry = entry_triple[2]
#         # for drop_entry, title_entry, order_entry in entry_triplets:
#         order_entry.delete(0, 'end')
#         order_entry.insert(0, f"{counter}")
#         counter = counter + 1
#
#     # for i, entry in enumerate(order_entries, start=0):
#     #     entry.delete(0, 'end')
#     #     entry.insert(0, f"{counter}")
#     #     counter = counter + 1
#
#
# # import terminal_output as terminal
#
#
# # TODO metadata flacs with metaflac cli
#
# def execute_affirmative():
#     print("all good, go ahead on execute")
#
#     # Collect all valid entries
#     valid_entries = []
#     for triplet in entry_triplets:
#         # (drop_entry, title_entry, order_entry)
#         song_file_path = triplet[0].get()
#         name = triplet[1].get()
#         order = triplet[2].get()
#
#         if song_file_path and name and order:
#             try:
#                 valid_entries.append((song_file_path, name, int(order)))
#             except ValueError:
#                 print(f"Invalid order number: {order}")
#                 continue
#
#     # Sort by track number (the third element)
#     valid_entries.sort(key=lambda x: x[2])
#
#     total_tracks = len(valid_entries)
#     print(total_tracks)
#
#     # Now process in correct order
#     for song_file_path, name, order in valid_entries:
#         album_art_to_execute = "album_art.jpg"
#         artist_to_execute = artist_label_static.get()
#         volume_to_execute = volume_to_equalise.get()
#         album_to_execute = album_label_static.get()
#
#         genre_from_dropdown = genre_dropdown.get()
#         genre_textual_index = genre_textual.index(genre_from_dropdown)
#         genre_to_execute = genre_textual[genre_textual_index]
#
#         year_to_execute = year_label_static.get()
#         output_file_path = directory_static.get()
#
#         mode = target_device.get()
#         # TODO MODE MODE MODE
#
#         print(song_file_path)
#         print(album_art_to_execute)
#         print(name)
#         print(artist_to_execute)
#         print(volume_to_execute)
#         print(album_to_execute)
#         print(genre_to_execute)
#         print(year_to_execute)
#         print(order)
#         print(output_file_path)
#
#         # terminal.open_terminal_view(song_file_path, "pluh", name,
#         #                             artist_to_execute,
#         #                             volume_to_execute, album_to_execute, genre_to_execute, year_to_execute,
#         #                             str(order),  # Convert back to string
#         #                             output_file_path, total_tracks,mode)
#
#         # Delay to ensure filesystem writes in order
#         import time
#         # time.sleep(0)
# # def execute_affirmative():
# #     print("all good, go ahead on execute")
# #     for triplet in entry_triplets:
# #         # (drop_entry, title_entry, order_entry)
# #         song_file_path_to_execute = triplet[0].get()
# #         # album_art_to_execute = art_ref.get();
# #         album_art_to_execute = "album_art.jpg";
# #         name_to_execute = triplet[1].get()
# #         artist_to_execute = artist_label_static.get()
# #         volume_to_execute = volume_to_equalise.get()
# #         album_to_execute = album_label_static.get()
# #
# #         genre_from_dropdown = genre_dropdown.get()
# #         genre_textual_index = genre_textual.index(genre_from_dropdown)
# #         genre_to_execute = genre_textual[genre_textual_index]
# #
# #         year_to_execute = year_label_static.get()
# #         order_to_execute = triplet[2].get()
# #         output_file_path = directory_static.get()
# #         if (triplet[0].get() != "" and triplet[1].get() != "" and triplet[2].get() != ""):
# #             print(song_file_path_to_execute)
# #             print(album_art_to_execute)
# #             print(name_to_execute)
# #             print(artist_to_execute)
# #             print(volume_to_execute)
# #             print(album_to_execute)
# #             print(genre_to_execute)
# #             print(year_to_execute)
# #             print(order_to_execute)
# #             print(output_file_path)
# #
# #             terminal.open_terminal_view(song_file_path_to_execute, "pluh", name_to_execute,
# #                                         artist_to_execute,
# #                                         volume_to_execute, album_to_execute, genre_to_execute, year_to_execute,
# #                                         order_to_execute,
# #                                         output_file_path)
#
#
# def execute_album():
#     print("execute")
#     print("========")
#     print(f"Album Name : {album_label_static.get()}")
#     print(f"Artist : {artist_label_static.get()}")
#     print(f"Year : {year_label_static.get()}")
#     genre_from_dropdown = genre_dropdown.get()
#     genre_textual_index = genre_textual.index(genre_from_dropdown)
#     genre_to_execute = genre_textual[genre_textual_index]
#     print(f"Genre : {genre_to_execute}")
#     print(f"Volume : {volume_to_equalise.get()}")
#     print(f"Output : {directory_static.get()}")
#     print(f"-----Songs-------")
#     for triplet in entry_triplets:
#         # (drop_entry, title_entry, order_entry)
#         if (triplet[1].get() != "" and triplet[2].get() != ""):
#             print(f"file : {triplet[0].get()}")
#             print(f"title : {triplet[1].get()}")
#             print(f"order : {triplet[2].get()}")
#     print(f"------------")
#     print("========")
#     if (volume_to_equalise.get() != "Equalise Volume (0.0 -> 1.0)" and directory_static.get() != "Directory"):
#         print("woohoo")
#         execute_affirmative();
#     else:
#         mb.showerror(title="Missing info", message="Missing valid Volume and or Directory data")
#
#
# def clear_all():
#     print("clear all")
#     order_entry_alpha.delete(0, 'end')
#     drop_song_alpha.delete(0, 'end')
#     title_entry_alpha.delete(0, 'end')
#
#     for drop_entry, title_entry, order_entry in entry_triplets:
#         order_entry.delete(0, 'end')
#         drop_entry.delete(0, 'end')
#         title_entry.delete(0, 'end')
#     fake_event_file_path = os.getcwd() + "/happy_logo.png"
#     fake_event = MockEvent(data=f"{{'{fake_event_file_path}'}}")  # Use f-string to insert the file path
#     dropArt(fake_event)
#
#     genre_dropdown.set(genre_textual[127])
#     album_label_static.delete(0, 'end')
#     album_label_static.insert(0, "Album Name")
#
#     artist_label_static.delete(0, 'end')
#     artist_label_static.insert(0, "Artist")
#
#     year_label_static.delete(0, 'end')
#     year_label_static.insert(0, "Year (dd-mm-yyyy)")
#
#     song_count_label_static.delete(0, 'end')
#     song_count_label_static.insert(0, "Song Count")
#
#     volume_to_equalise.delete(0, 'end')
#     volume_to_equalise.insert(0, "Equalise Volume (0.0 -> 1.0)")
#
#     target_device.config(state="normal")  # allow editing
#     target_device.delete(0, tk.END)  # clear prev text
#     target_device.insert(0, "Target Device : [0] (title) / [1] (order + title)")  # Insert new text
#
#     global output_directory
#     output_directory = ""
#
#     directory_static.config(state="normal")  # allow editing
#     directory_static.delete(0, tk.END)  # clear prev text
#     directory_static.insert(0, "Directory")  # Insert new text
#     directory_static.config(state="readonly")
#
#
# def continue_album():
#     print("continue album")
#     last_triple = entry_triplets[-1]
#     new_value = last_triple[2].get()
#     counter = int(new_value)
#     order_entry_alpha.delete(0, 'end')
#     order_entry_alpha.insert(0, f"{counter}")
#     counter = counter + 1
#
#     drop_song_alpha.delete(0, 'end')
#     title_entry_alpha.delete(0, 'end')
#     for drop_entry, title_entry, order_entry in entry_triplets:
#         order_entry.delete(0, 'end')
#         order_entry.insert(0, f"{counter}")
#         counter = counter + 1
#
#         drop_entry.delete(0, 'end')
#         title_entry.delete(0, 'end')
#
#
# def move_directories():
#     print("move directories")
#     folder_selected = filedialog.askdirectory()
#     if folder_selected:  # If the user selects a folder
#         # label.config(text=f"Selected Folder:\n{folder_selected}")
#         print(f"Selected Folder:\n{folder_selected}")
#         global output_directory;
#         output_directory = folder_selected
#         print(output_directory)
#         directory_static.config(state="normal")  # allow editing
#         directory_static.delete(0, tk.END)  # clear prev text
#         directory_static.insert(0, output_directory)  # Insert new text
#         directory_static.config(state="readonly")  # back to read only Lock it again
#
#
# root = tkinterdnd2.Tk()
#
# root.bind("<Tab>", lambda event: on_tab(root, albums, artist_label_static, year_label_static, album_label_static))
# root.title("Album Maker")
# root.geometry("1101x775")
# # root.geometry("1101x725")
# root.resizable(False, False)
# root.configure(bg='#060A13')
#
# # TODO album art, album name, artist, order, genre, year, disc (?)
#
# # START UI CREATION
# album_art_frame = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=400, height=800)
# # album_art_frame = tk.Frame(root, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=400, height=750)
# album_art_frame.configure(height=album_art_frame["height"], width=album_art_frame["width"])
# album_art_frame.grid_propagate(0)
#
# entry_frame = tk.Frame(root, borderwidth=5, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=700,
#                        height=775)
# # entry_frame = tk.Frame(root, borderwidth=5, bg="#060A13", highlightbackground="#0854ff", relief="flat", width=700,
# #                        height=750)
# entry_frame.configure(height=entry_frame["height"], width=entry_frame["width"])
# entry_frame.grid_propagate(0)
#
# album_art_frame.grid(column=2, row=0, columnspan=1, rowspan=1, sticky="ne")
# entry_frame.grid(column=1, row=0, columnspan=1, rowspan=1, sticky="nw")
#
# album_art = tk.Frame(album_art_frame, bg="#060A13", relief="raised", width=400, height=400)
# album_art.configure(height=album_art["height"], width=album_art["width"])
# album_art.grid_propagate(0)
# album_art.grid(column=1, row=1, columnspan=1, sticky="nsew")
# album_art.drop_target_register(DND_FILES)
# album_art.dnd_bind("<<Drop>>", dropArt)
#
# # album_cover_frame = tk.Frame(root, relief=tk.SUNKEN, bd=0, bg="#060A13", highlightbackground="#060A13")
# # album_cover_frame.drop_target_register(DND_FILES)
# # album_cover_frame.dnd_bind("<<Drop>>", dropArt)
# # album_cover_frame.grid(row=0, column=0, sticky="nsew", padx=1, pady=1)
# album_cover_label = tk.Label(album_art, fg="#FFFFFF", bg="#101a30")
# album_cover_label.grid(column=2, row=2, columnspan=1, rowspan=1, sticky="nsew")
#
# generate_spinner_frames()
#
# spinner_label = tk.Label(album_art, bg="#060A13")
#
# spinner_label.grid(column=2, row=2)
# spinner_label.lower()  # Initially hidden
#
# # album_cover_label.pack(expand=True, fill="both")
#
# album_label_static = tk.Entry(album_art_frame, text="Album Name From Entry", bg="#060A13", fg="#27FEFF")
#
# # Set the trace method to call on_entry_change() when the value changes
# artist_label_static = tk.Entry(album_art_frame, text="Artist Name From Entry", bg="#060A13", fg="#27FEFF")
#
# year_label_static = tk.Entry(album_art_frame, text="Year From Entry", bg="#060A13", fg="#27FEFF")
#
# genre_options = genre_textual
# genre_dropdown = ttk.Combobox(album_art_frame, values=genre_options, state="readonly")
# # genre_dropdown.grid(row=4, column=1, sticky="ew", padx=5, pady=2)
# genre_dropdown.configure(foreground="#FF5F57", background="#FF5F57")
# genre_dropdown.set(genre_textual[127])
# genre_dropdown.bind("<<ComboboxSelected>>", on_select)
#
# # genre_label_static = tk.Entry(album_art_frame, text="Genre From Entry", bg="#060A13", fg="#27FEFF")
#
#
# song_count_label_static = tk.Entry(album_art_frame, state="readonly", text="Song Count From Entry", bg="#060A13",
#                                    fg="#27FEFF")
# volume_to_equalise = tk.Entry(album_art_frame, text="Equalise", bg="#060A13", fg="#27FEFF")
# target_device = tk.Entry(album_art_frame, text="Target Device (car/ player)", bg="#060A13", fg="#27FEFF")
# runtime_label_static = tk.Entry(album_art_frame, state="readonly", text="Runtime From Entry", bg="#060A13",
#                                 fg="#FF5F57")
# art_ref = tk.Entry(album_art_frame, state="readonly", text="Art Ref", bg="#060A13", fg="#FF5F57")
# art_ref.place_forget()
#
# directory_static = tk.Entry(album_art_frame, state="readonly", text="Directory", bg="#060A13", fg="#FF5F57")
# album_label_static.grid(column=1, row=2, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# artist_label_static.grid(column=1, row=3, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# year_label_static.grid(column=1, row=4, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# genre_dropdown.grid(column=1, row=5, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# # genre_label_static.grid(column=1, row=5, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# song_count_label_static.grid(column=1, row=6, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# runtime_label_static.grid(column=1, row=7, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# volume_to_equalise.grid(column=1, row=8, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# directory_static.grid(column=1, row=9, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
# target_device.grid(column=1, row=10, columnspan=1, rowspan=1, padx=50, pady=4, sticky="nsew")
#
# # art_ref.grid(column=1, row=9, columnspan=1, rowspan=1, padx=50, pady=3, sticky="nsew")
#
# button_row = tk.Frame(album_art_frame, bg="#060A13")
# button_row.grid(column=1, row=11, padx=6, pady=6, sticky="ew")
# # button_row.grid(column=1, row=10, padx=6, pady=6, sticky="ew")
#
# execute_button = tk.Button(button_row, text="Execute", bg="#060A13", fg="#060A13", command=execute_album)
# clear_button = tk.Button(button_row, text="Clear All", bg="#060A13", fg="#FF5F57", command=clear_all)
# clear_songs_button = tk.Button(button_row, text="Cont. Album", bg="#060A13", fg="#FF5F57", command=continue_album)
# move_directories_button = tk.Button(button_row, text="Move", bg="#060A13", fg="#FF5F57", command=move_directories)
#
# execute_button.pack(side="left", padx=5)
# clear_button.pack(side="left", padx=5)
# clear_songs_button.pack(side="left", padx=5)
# move_directories_button.pack(side="left", padx=5)
#
# order_label = tk.Label(entry_frame, text="Order", bg="#060A13", fg="#FF5F57", name=f"order_label-{0}")
# order_label._name = f"order_label-{0}"
#
# entry_var = tk.StringVar()
# order_entry_alpha = tk.Entry(entry_frame, name=f"order_entry-{0}", textvariable=entry_var)
# order_entry_alpha._name = f"order_entry-{0}"
# order_entry_alpha.configure(bg="#101a30", fg="#27FEFF", highlightbackground="#273044")
# entry_var.trace("w", on_entry_change)
#
# order_entry_alpha.delete(0, 'end')
# order_entry_alpha.insert(0, 1)
#
# title_label = tk.Label(entry_frame, text="Title", bg="#060A13", fg="#FF5F57", name=f"title-label-{0}")
# title_label._name = f"title-label-{0}"
# title_entry_alpha = tk.Entry(entry_frame, name=f"title_entry-{0}")
# title_entry_alpha._name = f"title_entry-{0}"
# title_entry_alpha.configure(bg="#101a30", fg="#27FEFF", highlightbackground="#273044")
#
# drop_song_alpha = tk.Entry(entry_frame, name=f"drop_song-{0}")
# drop_song_alpha._name = f"drop_song-{0}"
# drop_song_alpha.configure(bg="#101a30", fg="#27FEFF", highlightbackground="#273044")
# drop_song_alpha.drop_target_register(DND_FILES)
# drop_song_alpha.dnd_bind("<<Drop>>", dropSong)
#
# entry_triplets.append((drop_song_alpha, title_entry_alpha, order_entry_alpha))
#
# order_label.grid(column=1, row=0, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
# order_entry_alpha.grid(column=2, row=0, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
# title_label.grid(column=3, row=0, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
# title_entry_alpha.grid(column=4, row=0, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
# drop_song_alpha.grid(column=5, row=0, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
#
# entry_frame.grid_columnconfigure(1, weight=1, uniform="uniform")
# entry_frame.grid_columnconfigure(2, weight=1, uniform="uniform")
# entry_frame.grid_columnconfigure(3, weight=1, uniform="uniform")
# entry_frame.grid_columnconfigure(4, weight=8, uniform="uniform")
# entry_frame.grid_columnconfigure(5, weight=1, uniform="uniform")
#
# for x in range(1, 16):
#     order_label = tk.Label(entry_frame, text="Order", bg="#060A13", fg="#FF5F57", name=f"order_label-{x}")
#     order_label._name = f"order_label-{x}"
#
#     order_entry = tk.Entry(entry_frame, name=f"order_entry-{x}")
#     order_entry._name = f"order_entry-{x}"
#     order_entry.configure(bg="#101a30", fg="#27FEFF", highlightbackground="#273044")
#     # order_entries.append(order_entry)
#
#     order_entry.delete(0, 'end')
#     order_entry.insert(0, f"{x + 1}")
#
#     title_label = tk.Label(entry_frame, text="Title", bg="#060A13", fg="#FF5F57", name=f"title-label-{x}")
#     title_label._name = f"title-label-{x}"
#     title_entry = tk.Entry(entry_frame, name=f"title_entry-{x}")
#     title_entry._name = f"title_entry-{x}"
#     title_entry.configure(bg="#101a30", fg="#27FEFF", highlightbackground="#273044")
#     # drop_title_entries.append(title_entry)
#
#     drop_song = tk.Entry(entry_frame, name=f"drop_song-{x}")
#     drop_song._name = f"drop_song-{x}"
#     drop_song.configure(bg="#101a30", fg="#27FEFF", highlightbackground="#273044")
#     drop_song.drop_target_register(DND_FILES)
#     drop_song.dnd_bind("<<Drop>>", dropSong)
#     # drop_song_entries.append(drop_song)
#
#     entry_triplets.append((drop_song, title_entry, order_entry))
#
#     order_label.grid(column=1, row=x, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
#     order_entry.grid(column=2, row=x, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
#     title_label.grid(column=3, row=x, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
#     title_entry.grid(column=4, row=x, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
#     drop_song.grid(column=5, row=x, columnspan=1, rowspan=1, padx=3, pady=10, sticky="nsew")
#
#     entry_frame.grid_columnconfigure(1, weight=1, uniform="uniform")
#     entry_frame.grid_columnconfigure(2, weight=1, uniform="uniform")
#     entry_frame.grid_columnconfigure(3, weight=1, uniform="uniform")
#     entry_frame.grid_columnconfigure(4, weight=8, uniform="uniform")
#     entry_frame.grid_columnconfigure(5, weight=1, uniform="uniform")
#
# # END UI CREATION
#
# album_label_static.config(state="normal")  # allow editing
# album_label_static.delete(0, tk.END)  # clear prev text
# album_label_static.insert(0, "Album Name")  # Insert new text
#
# artist_label_static.config(state="normal")  # allow editing
# artist_label_static.delete(0, tk.END)  # clear prev text
# artist_label_static.insert(0, "Artist")  # Insert new text
#
# year_label_static.config(state="normal")  # allow editing
# year_label_static.delete(0, tk.END)  # clear prev text
# year_label_static.insert(0, "Year (dd-mm-yyyy)")  # Insert new text
# #
# # genre_label_static.config(state="normal")  # allow editing
# # genre_label_static.delete(0, tk.END)  # clear prev text
# # genre_label_static.insert(0,"Genre dropdown")  # Insert new text
#
# song_count_label_static.config(state="normal")  # allow editing
# song_count_label_static.delete(0, tk.END)  # clear prev text
# song_count_label_static.insert(0, "Song Count")  # Insert new text
#
# volume_to_equalise.config(state="normal")  # allow editing
# volume_to_equalise.delete(0, tk.END)  # clear prev text
# volume_to_equalise.insert(0, "Equalise Volume (0.0 -> 1.0)")  # Insert new text
#
#
# target_device.config(state="normal")  # allow editing
# target_device.delete(0, tk.END)  # clear prev text
# target_device.insert(0, "Target Device : [0] (title) / [1] (order + title)")  # Insert new text
#
# runtime_label_static.config(state="normal")  # allow editing
# runtime_label_static.delete(0, tk.END)  # clear prev text
# runtime_label_static.insert(0, "Calculate Runtime")  # Insert new text
# runtime_label_static.config(state="readonly")
#
# directory_static.config(state="normal")  # allow editing
# directory_static.delete(0, tk.END)  # clear prev text
# directory_static.insert(0, "Directory")  # Insert new text
# directory_static.config(state="readonly")
#
# root.mainloop()
