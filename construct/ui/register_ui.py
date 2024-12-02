import tkinter as tk
from services.auth_service import AuthService
from tkinter import messagebox
from ui.login_ui import LoginUI

class RegisterUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        
        tk.Label(self.frame, text="New Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="New Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        
        tk.Button(self.frame, text="Register", command=self.register).grid(row=2, column=1)

    def register(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        
        
        if len(username) < 4 or len(password) < 6:
            messagebox.showerror("Invalid Input", "Username must be at least 4 characters and password 6 characters long.")
            return
        
        try:
            AuthService.register(username, password)
            messagebox.showinfo("Success", "Registration successful! Please log in.")
            self.frame.destroy()  
            LoginUI(self.master)  
        except Exception as e:
            messagebox.showerror("Error", str(e))
