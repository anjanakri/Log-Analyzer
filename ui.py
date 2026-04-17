from tkinter import *
import customtkinter as ctk

app=ctk.CTk()   #main window
app.title("Log File Analyzer")
app.geometry("600x400")

#window widget
label=ctk.CTkLabel(app, text="Log File Analyzer", font=("Ariel", 24))
label.pack(pady=20)

button=ctk.CTkButton(app, text="Browse file")
button.pack(pady=10)
app.mainloop()