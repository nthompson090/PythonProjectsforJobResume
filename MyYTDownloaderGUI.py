"""
Want to download YouTube videos but can't afford premium?
This GUI application allows you to download YouTube videos easily.
Author: Nicholas Thompson
"""
from tkinter import StringVar, filedialog, messagebox
from tkinter.ttk import *
import customtkinter
from yt_dlp import YoutubeDL
import os

# Set appearance mode and color theme
customtkinter.set_appearance_mode("System")

# Create the main application window
app = customtkinter.CTk()
app.geometry("450x350")
app.title("YouTube Video Downloader")

# Create and place widgets
yturl_title = customtkinter.CTkLabel(app, text="YouTube Video URL:")
yturl_title.pack(pady=10)

# Entry for YouTube URL
yturl_entry = customtkinter.CTkEntry(app, width=400, height=30,
                                     placeholder_text="Enter YouTube video URL")
yturl_entry.pack()

# Function to handle video download
def download_video():
    ytLink = yturl_entry.get()
    download_folder = filedialog.askdirectory(title="Select Download Folder")
    finishLabel.configure(text="Downloading...")
    yt = {
        'format': 'bestvideo+bestaudio/best',
        'outtmpl': os.path.join(download_folder, '%(title)s.%(ext)s')
    }
    video = YoutubeDL(yt) # Create YoutubeDL object
    video.add_progress_hook(progress_hook) # Add progress hook
    video.download([ytLink]) # Start download
    if not error_check():
        messagebox.showerror(title="Error", message=error_check())
        return
    finishLabel.configure(text="Download Complete")

# Progress bar
bar = Progressbar(app, orient="horizontal", length=500, mode="determinate")
bar.pack(pady=30)

# Label to show download percentage
percent = StringVar()
percent.set("0%")
download_video.status_label = customtkinter.CTkLabel(app, textvariable=percent)
download_video.status_label.pack()

# Download button
download_button = customtkinter.CTkButton(app, text="DOWNLOAD",
                                          command=download_video, width=150, height=40, 
                                          fg_color="#FF0000", hover_color="#CC0000", 
                                          font=("Times New Roman", 16, "bold"))
download_button.pack(pady=10)

# Refresh button to clear status label, reset percentage and progress bar
refresh_button = customtkinter.CTkButton(app, text="REFRESH",
                                         command=lambda: finishLabel.configure(text="") or percent.set("0%") or bar.configure(value=0) or yturl_entry.delete(0, 'end'),
                                         width=150, height=40, fg_color="#008000", hover_color="#006600", 
                                         font=("Times New Roman", 16, "bold"))
refresh_button.pack(pady=10)

# Label to show download status
finishLabel = customtkinter.CTkLabel(app, text="")
finishLabel.pack(pady=20)

# Progress hook to update the progress bar
def progress_hook(d):
    if d['status'] == 'downloading':
        percent.set(d.get('_percent_str', '0%'))
        bar['value'] = float(percent.get()[:-1])  # Remove '%' and convert to float
        app.update_idletasks()
    elif d['status'] == 'finished':
        bar['value'] = 100
        app.update_idletasks()
        percent.set("100%")

# Function to check for valid URL input
def error_check():
    if not yturl_entry.get():
        finishLabel.configure(text="Please enter a valid URL")
        return False
    return True

app.mainloop()