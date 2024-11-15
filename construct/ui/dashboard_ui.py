import tkinter as tk
from ui.project_ui import ProjectUI
from ui.view_projects_ui import ViewProjectsUI
class DashboardUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()
        
        tk.Label(self.frame, text="Welcome to the Construction Cost Tracker Dashboard!").grid(row=0, column=0, padx=10, pady=10)
        
        tk.Button(self.frame, text="Create New Project", command=self.open_project_window).grid(row=1, column=0, padx=10, pady=10)
        
        tk.Button(self.frame, text="View Existing Projects", command=self.view_projects).grid(row=2, column=0, padx=10, pady=10)

        tk.Button(self.frame, text="Log Out", command=self.logout).grid(row=3, column=0, padx=10, pady=10)

    def open_project_window(self):
        self.frame.destroy()
        ProjectUI(self.master)

    def view_projects(self):
        self.frame.destroy()
        ViewProjectsUI(self.master)

    def logout(self):
        self.frame.destroy()
        from ui.login_ui import LoginUI
        LoginUI(self.master)
