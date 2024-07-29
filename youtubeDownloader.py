import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
import yt_dlp
from PIL import Image, ImageTk
# As of July 24th 2024, Pytube doesn't work so yt_dlp has to be installed to continue project
# from pytube import YouTube


#global variable to store video location
download_location = ""
download_format = "video"
#This is the main function responsible for downloading the video
def download_video():
    try:
        if not download_location:
            messagebox.showwarning("Warning", "Please select a download location.")
            return
        
        ytUrl = linkEntry.get()
        ydl_opts = {
            'outtmpl': f'{download_location}/%(title)s.%(ext)s',
            'progress_hooks': [progress_hook],
            'ffmpeg_location': '/path/to/ffmpeg',  # Update this to the location of your ffmpeg
        }
        if download_format == "audio":
            ydl_opts['format'] = 'bestaudio/best'
            ydl_opts['postprocessors'] = [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }]
        else:
            ydl_opts['format'] = 'best'

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytUrl])
        messagebox.showinfo("Success", "Download Complete")
    except Exception as e:
        messagebox.showerror("Error", f"Youtube link is invalid: {str(e)}")
    print("Download complete")



def progress_hook(d):
    if d['status'] == 'downloading':
        # Ensure the percentage string is processed correctly
        try:
            p = d['_percent_str'].replace('%', '').strip()
            p = float(p)
            progress.set(p)
            window.update_idletasks()
        except ValueError:
            # Handle the case where percentage string is not a valid float
            print("Could not parse percentage:", d['_percent_str'])
    elif d['status'] == 'finished':
        progress.set(100)
        print("Download complete")

    
def chooseFile():
    global download_location
    download_location = filedialog.askdirectory()
    if download_location:
        location_label.config(text=f"Download Location: {download_location}")
    else:
        location_label.config(text="No location selected")

def set_format():
    global download_format
    download_format = format_var.get()


#System Settings
ctk.set_appearance_mode("system")

#Creating the Window
window = ctk.CTk()
window.title('Youtube Downloader')
window.geometry('500x500')

#Creating UI widgets
# Load and resize the image
original_img = Image.open("YouTube_Logo_2017.svg.png")  # Replace with your image file path
resized_img = original_img.resize((440, 150), Image.LANCZOS)  # Adjust the size as needed
img = ImageTk.PhotoImage(resized_img)
label = ttk.Label(master=window, image=img, font="Arial 24", padding=5)
label.pack() 

#The entry box where the link is pasted
linkLabel = ctk.CTkLabel(master=window, text="Enter Valid Youtube URL here")
linkLabel.pack()
linkEntry = ctk.CTkEntry(master=window)
linkEntry.pack()

# Radio buttons to choose download format
format_var = tk.StringVar(value="video")
video_radio = ctk.CTkRadioButton(master=window, text="Video", variable=format_var, value="video", command=set_format)
audio_radio = ctk.CTkRadioButton(master=window, text="Audio", variable=format_var, value="audio", command=set_format)
video_radio.pack(pady=5)
audio_radio.pack(pady=5)

#Button to choose location
fileLocationButton = ctk.CTkButton(master=window, text="Choose File", command=chooseFile)
fileLocationButton.pack(pady=5)

#When the button is clicked the download_video function is called
download_button = ctk.CTkButton(master=window, text="Download", command=download_video)
download_button.pack(pady=10)

#Progress bar to show the download progress of the video
progress = tk.DoubleVar()
progress_bar = ttk.Progressbar(master=window, variable=progress, maximum=100)
progress_bar.pack(pady=10, fill=tk.X)



#The method that runs the App
window.mainloop()