import tkinter as tk
import customtkinter as ctk
from tkinter import ttk, messagebox, filedialog
import yt_dlp
# As of July 24th 2024, Pytube doesn't work so yt_dlp has to be installed to continue project
# from pytube import YouTube


#global variable to store video location
download_location = ""
#This is the main function responsible for downloading the video
def download_video():
    try:
        #grabs the link from the linkEntry widget
        ytUrl = linkEntry.get()
        ydl_opts = {
            'format': 'best',
            'outtmpl': f'{download_location}/%(title)s.%(ext)s',
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([ytUrl])
        messagebox.showinfo("Success", "Download Complete")
    except Exception as e:
        messagebox.showerror("Error", f"Youtube link is invalid: {str(e)}")
    print("Download complete")

    
def chooseFile():
    global download_location
    download_location = filedialog.askdirectory()
    if download_location:
        location_label.config(text=f"Download Location: {download_location}")
    else:
        location_label.config(text="No location selected")

#System Settings
ctk.set_appearance_mode("system")

#Creating the Window
window = ctk.CTk()
window.title('Youtube Downloader')
window.geometry('500x500')

#Creating UI widgets
label = ttk.Label(master=window, text='Youtube Downloader', font="Arial 24", padding=5)
label.pack() 

#The entry box where the link is pasted
linkEntry = ctk.CTkEntry(master=window)
linkEntry.pack()

#Button to choose location
fileLocationButton = ctk.CTkButton(master=window, text="Choose File", command=chooseFile)
fileLocationButton.pack(pady=5)

#When the button is clicked the download_video function is called
download_button = ctk.CTkButton(master=window, text="Download", command=download_video)
download_button.pack(pady=10)



#The method that runs the App
window.mainloop()