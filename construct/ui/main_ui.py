import tkinter as tk
from ui.login_ui import LoginUI
from services.auth_service import AuthService

class MainUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Construction Cost Tracker")
        
    def run(self):
        LoginUI(self.root)
        self.root.mainloop()