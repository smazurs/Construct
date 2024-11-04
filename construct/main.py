from ui.main_ui import MainUI
from services.auth_service import AuthService
from ui.login_ui import LoginUI
from ui.register_ui import RegisterUI
from models.initialize_db import initialize_database
import tkinter as tk

if __name__ == "__main__":
    initialize_database()

    root = tk.Tk()
    root.title("Construct")

    if AuthService.has_users():
        LoginUI(root)
    else:
        RegisterUI(root)

    root.mainloop()
