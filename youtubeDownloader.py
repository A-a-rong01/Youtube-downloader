import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
from pytube import YouTube


#This is the main function responsible for downloading the video
def download_video():
    #grabs the link from the linkEntry widget
    ytUrl = linkEntry.get()
    print(ytUrl)

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
linkEntry = ttk.Entry(master=window)
linkEntry.pack()
#When the button is clicked the download_video function is called
download_button = ttk.Button(master=window, text="Download", command=download_video)
download_button.pack(pady=10)



#The method that runs the App
window.mainloop()