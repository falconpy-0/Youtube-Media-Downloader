import subprocess
from tkinter import *
from tkinter import filedialog, ttk
from PIL import Image, ImageTk

# --- Download Function ---
def get_vid():
    link = url_entry.get()
    format_selected = format_var.get()
    directory = filedialog.askdirectory()

    if not link or not directory:
        return

    output_template = f"{directory}/%(title)s.%(ext)s"

    if format_selected == "MP4":
        command = ["yt-dlp", "-f", "bestvideo+bestaudio", "-o", output_template, link]
    elif format_selected == "MP3":
        command = [
            "yt-dlp", "-f", "bestaudio",
            "--extract-audio", "--audio-format", "mp3",
            "-o", output_template, link
        ]
    else:
        print("❌ Unknown format.")
        return

    try:
        subprocess.run(command, check=True)
        print("✅ Download complete.")
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {e}")

# --- Setup Window ---
window = Tk()
window.title("Media Downloader")
window.geometry("500x400")
window.resizable(False, False)
window.config(bg="#1a1a1a")

# --- Background Frame Image (optional) ---
try:
    frame_img = Image.open("C:\\Users\\LENOVO\\Desktop\\projects.tkinter\\Media Downloader\\frame.png")
    frame_photo = ImageTk.PhotoImage(frame_img)
    main_frame = Label(window, image=frame_photo)
    main_frame.pack()
    main_frame.image = frame_photo
except:
    pass  # In case the image is missing, skip it

# --- Main Box Frame ---
main_box = Frame(window, bg="#1f1f1f", bd=0, relief=FLAT)
main_box.place(x=80, y=80, width=340, height=230)

title_label = Label(main_box, text="Media Downloader", font=("Poppins", 16, "bold"),
                    fg="white", bg="#1f1f1f")
title_label.pack(pady=(20, 10))

# --- URL Entry ---
url_entry = Entry(main_box, width=32, font=("Poppins", 10),
                  bg="#2a2a2a", fg="white", insertbackground="white", relief=FLAT)
url_entry.pack(pady=(0, 15), ipady=6)

# --- Format + Button Frame ---
action_frame = Frame(main_box, bg="#1f1f1f")
action_frame.pack()

format_var = StringVar(value="MP4")
format_menu = ttk.Combobox(action_frame, textvariable=format_var, values=["MP4", "MP3"], state="readonly", width=10)
format_menu.pack(side=LEFT, padx=(0, 20), ipady=4)

# Combobox Style
style = ttk.Style()
style.theme_use('clam')
style.configure("TCombobox",
                fieldbackground="#2a2a2a",
                background="#2a2a2a",
                foreground="white",
                arrowcolor="white")

# --- Download Button ---
download_btn = Button(action_frame, text="Download", font=("Poppins", 10, "bold"),
                      bg="#6c45aa", fg="white", activebackground="#5a3790",
                      padx=20, pady=5, relief=FLAT, cursor="hand2", command=get_vid)
download_btn.pack(side=LEFT)

# --- Run ---
window.mainloop()
