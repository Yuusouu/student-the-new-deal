# main.py
import tkinter as tk
from tkinter import messagebox
from login import Login
from studentgui import StudentGUI

class MainApplication:
    def __init__(self, master):
        self.master = master
        self.master.title("Login")

        # Set window size
        self.master.geometry("300x200")
        
        # Add padding
        self.master.config(padx=10, pady=10)

        self.login_window()

    def login_window(self):
        self.title_label = tk.Label(self.master, text="Login", font=("Arial", 16))
        self.title_label.grid(row=0, column=0, columnspan=2, pady=10)

        self.label_username = tk.Label(self.master, text="Username:")
        self.label_username.grid(row=1, column=0, sticky="e", pady=5)
        self.entry_username = tk.Entry(self.master)
        self.entry_username.grid(row=1, column=1, pady=5)

        self.label_password = tk.Label(self.master, text="Password:")
        self.label_password.grid(row=2, column=0, sticky="e", pady=5)
        self.entry_password = tk.Entry(self.master, show="*")
        self.entry_password.grid(row=2, column=1, pady=5)

        self.button_login = tk.Button(self.master, text="Login", width=20, command=self.login)
        self.button_login.grid(row=3, column=0, columnspan=2, pady=10)

    def login(self):
        username = self.entry_username.get()
        password = self.entry_password.get()

        login = Login()
        if login.authenticate(username, password):
            messagebox.showinfo("Login Success", "You are logged in!")
            self.master.destroy()  
            self.open_student_gui()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    def open_student_gui(self):
        student_window = tk.Tk()
        app = StudentGUI(student_window)
        student_window.mainloop()

if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

