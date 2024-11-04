import tkinter as tk
from services.auth_service import AuthService
from ui.dashboard_ui import DashboardUI

class LoginUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        
        tk.Label(self.frame, text="Username:").grid(row=0, column=0)
        self.username_entry = tk.Entry(self.frame)
        self.username_entry.grid(row=0, column=1)

        tk.Label(self.frame, text="Password:").grid(row=1, column=0)
        self.password_entry = tk.Entry(self.frame, show="*")
        self.password_entry.grid(row=1, column=1)

        tk.Button(self.frame, text="Login", command=self.login).grid(row=2, column=1)
        
        tk.Button(self.frame, text="Register", command=self.open_register_window).grid(row=3, column=1)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()
        if AuthService.login(username, password):
            print("Login successful")
            self.frame.destroy()
            DashboardUI(self.master)
        else:
            print("Login failed")

    def open_register_window(self):
        self.frame.destroy()
        from ui.register_ui import RegisterUI
        RegisterUI(self.master)
