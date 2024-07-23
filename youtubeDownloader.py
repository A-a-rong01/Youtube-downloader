import tkinter as tk
from tkinter import ttk


def button_func():
    print("it works")

#Creating the Window
window = tk.Tk()
window.title('Youtube Downloader')
window.geometry('500x500')

#Creating widgets
label = ttk.Label(master=window, text='Youtube Downloader', font="Arial 24", padding=5)
label.pack() 

entry = ttk.Entry(master=window)
entry.pack()

button = ttk.Button(master=window, text="Download", command=button_func)
button.pack()



#The method that runs the App
window.mainloop()