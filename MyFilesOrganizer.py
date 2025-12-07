import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import os
import shutil

# Set up the customtkinter appearance
ctk.set_appearance_mode("auto")
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.geometry("400x250")
app.title("Files Organizer")

# Define paths for common directories
downloads_path = os.path.expanduser("~/Downloads")
desktop_path = os.path.expanduser("~/Desktop")
documents_path = os.path.expanduser("~/Documents")

# Function to organize files by extension
def organize_files(path):
    files_by_extension = {}
    for filename in os.listdir(path):
        file_path = os.path.join(path, filename)
        if os.path.isfile(file_path):
            ext = os.path.splitext(filename)[1]
            if ext not in files_by_extension:
                files_by_extension[ext] = []
            files_by_extension[ext].append(file_path)
    
    for ext, file_paths in files_by_extension.items():
        folder_name = f"{ext[1:].upper()}Files"
        folder_path = os.path.join(path, folder_name)
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        for file_path in file_paths:
            shutil.move(file_path, folder_path)

# Create buttons for organizing files in different directories
button1 = ctk.CTkButton(app, text="Organize Downloads", command=lambda: organize_files(downloads_path))
button1.pack(pady=20)
button2 = ctk.CTkButton(app, text="Organize Desktop", command=lambda: organize_files(desktop_path))
button2.pack(pady=20)
button3 = ctk.CTkButton(app, text="Organize Documents", command=lambda: organize_files(documents_path))
button3.pack(pady=20)

app.mainloop()