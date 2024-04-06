# -*- coding: utf-8 -*-
"""
Created on Sat Apr  6 12:45:10 2024

@author: Home
"""

import os
import tkinter as tk
from tkinter import ttk
import easygui
import glob
import datetime
from PIL import Image, ImageFile
from tkinter import *
from tkinter import font
from PIL import ImageTk, Image 
import time


w=Tk()

#Using piece of code from old splash screen
width_of_window = 427
height_of_window = 250
screen_width = w.winfo_screenwidth()
screen_height = w.winfo_screenheight()
x_coordinate = (screen_width/2)-(width_of_window/2)
y_coordinate = (screen_height/2)-(height_of_window/2)
w.geometry("%dx%d+%d+%d" %(width_of_window,height_of_window,x_coordinate,y_coordinate))
# w.configure(bg='#ED1B76')
w.overrideredirect(1) #for hiding titlebar

#new window to open
def new_win():
    q=Tk()
    q.title('main window')
    q.mainloop()

Frame(w, width=800, height=250, bg='black').place(x=0,y=0)
label1=Label(w, text='ImageFormatConversion\nBy Anas Odeh', fg='orange', bg='black') 
label1.configure(font=("Arial", 24, "bold"))
label1.place(x=20,y=60)

label2=Label(w, text='Loading...', fg='orange', bg='black')
label2.configure(font=("Arial", 20))
label2.place(x=160,y=180)

#making animation

image_a=ImageTk.PhotoImage(Image.open('Group 2.png'))
image_b=ImageTk.PhotoImage(Image.open('Group 1.png'))


for i in range(5): #5loops
    l1=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=180, y=160)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=160)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=160)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=160)
    w.update_idletasks()
    time.sleep(0.07)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=160)
    l2=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=200, y=160)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=160)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=160)
    w.update_idletasks()
    time.sleep(0.07)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=160)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=160)
    l3=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=220, y=160)
    l4=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=240, y=160)
    w.update_idletasks()
    time.sleep(0.07)

    l1=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=180, y=160)
    l2=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=200, y=160)
    l3=Label(w, image=image_b, border=0, relief=SUNKEN).place(x=220, y=160)
    l4=Label(w, image=image_a, border=0, relief=SUNKEN).place(x=240, y=160)
    w.update_idletasks()
    time.sleep(0.07)

w.destroy()



class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master, bg='black')
        self.master = master
        self.master.title('Image Format Conversion')
        self.master.configure(bg='black')
        self.pack()
        self.create_widgets()
        self.main_folder = None

    def create_widgets(self):
        self.select_button = tk.Button(self, bg='orange', fg='black', font=('Arial Bold', 18))
        self.select_button["text"] = "Select Your Folder Of Images"
        self.select_button["command"] = self.select_folder
        self.select_button.pack(side="top", pady=20)

        self.format_message_label = tk.Label(self, text="Please choose the desired image format:", anchor='w', font=('Arial Bold', 18), bg='black', fg='orange')
        self.format_message_label.pack(side="top", pady=10)

        self.file_type_var = tk.StringVar(self)
        self.file_type_var.set("png")  # default value

        self.file_type_option_menu = ttk.Combobox(self, textvariable=self.file_type_var, values=["png", "jpg", "tif"])
        self.file_type_option_menu.pack()

        self.progress_label = tk.Label(self, text="Progress: 0%", anchor='w', font=('Arial Bold', 18), bg='black', fg='orange')
        self.progress_label.pack(side="top", pady=20)

        self.progress = ttk.Progressbar(self, orient="horizontal", length=500, mode="determinate")
        self.progress.pack(side="top", pady=10)

        self.start_analysis_button = tk.Button(self, bg='orange', fg='black', font=('Arial Bold', 18))
        self.start_analysis_button["text"] = "Start Analysis"
        self.start_analysis_button["command"] = self.process_files
        self.start_analysis_button.pack(side="top", pady=20)

        self.developer_label = tk.Label(self, text="©\u00A0This App was developed by Anas Odeh.", bg='orange', fg='black', font=('Arial Bold', 18))
        self.developer_label.pack(side="bottom", pady=10)

    def select_folder(self):
        self.main_folder = easygui.diropenbox(title='Please select your main folder')

    def show_custom_messagebox(self):
        message_window = tk.Toplevel(self.master)
        message_window.title('Success')
        message_window.configure(bg='black')
        message_window.geometry('600x300')

        success_message = tk.Label(message_window, text='All images converted successfully!\nGood Luck with your next task :)', padx=20, pady=20, bg='black', fg='orange', font=('Arial Bold', 18))
        success_message.pack()

        close_button = tk.Button(message_window, text='Close', command=message_window.destroy, bg='orange', fg='black', font=('Arial Bold', 18))
        close_button.pack(pady=20)

    def process_files(self):
        if not self.main_folder:
            tk.messagebox.showerror("Error", "Please select your input folder first.")
            return

        Image.MAX_IMAGE_PIXELS = None
        ImageFile.LOAD_TRUNCATED_IMAGES = True

        current_datetime = datetime.datetime.now()
        datetime_str = current_datetime.strftime("%d-%m-%Y_%H-%M-%S")
        output_folder = os.path.join(self.main_folder, f"Converted Images {datetime_str}")
        os.makedirs(output_folder, exist_ok=True)

        supported_formats = ['*.png', '*.jpg', '*.jpeg', '*.tif', '*.bmp', '*.gif']
        image_files = []
        for fmt in supported_formats:
            image_files.extend(glob.glob(os.path.join(self.main_folder, f"**/{fmt}"), recursive=True))

        total_files = len(image_files)
        if total_files == 0:
            tk.messagebox.showinfo("Info", "No image files found in the selected directory.")
            return

        processed_files = 0
        output_format = self.file_type_var.get()

        for image_file_path in image_files:
            try:
                img = Image.open(image_file_path)
                file_name = os.path.basename(image_file_path)
                file_name_without_extension = os.path.splitext(file_name)[0]
                output_file_name = f"{file_name_without_extension}.{output_format}"
                output_path = os.path.join(output_folder, output_file_name)

                img.save(output_path)

                processed_files += 1
                percent_done = int((processed_files / total_files) * 100)
                self.progress['value'] = percent_done
                self.progress_label['text'] = f"Progress: {percent_done}%"
                self.master.update_idletasks()
            except Exception as e:
                tk.messagebox.showerror("Error", f"Failed to convert {image_file_path}: {str(e)}")
                continue

        self.progress['value'] = 0
        self.progress_label['text'] = "Progress: 0%"
        if processed_files == total_files:
            self.show_custom_messagebox()
        else:
            tk.messagebox.showinfo("Info", "Conversion completed with some errors.")

    def run(self):
        self.mainloop()

root = tk.Tk()
root.geometry('600x500')
root.configure(bg='black')
app = Application(master=root)
app.run()
