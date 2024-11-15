import tkinter as tk
from models.project_model import ProjectModel

class ViewProjectsUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        tk.Label(self.frame, text="Existing Projects").grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        headers = ["Project Name", "Location", "Timeline", "Material Cost", "Labor Cost", "Equipment Cost"]
        for col, header in enumerate(headers):
            tk.Label(self.frame, text=header, borderwidth=1, relief="solid").grid(row=1, column=col)

        projects = ProjectModel.get_all_projects()
        for i, project in enumerate(projects, start=2):
            for col, value in enumerate(project):
                tk.Label(self.frame, text=value, borderwidth=1, relief="solid").grid(row=i, column=col)

        tk.Button(self.frame, text="Back to Dashboard", command=self.back_to_dashboard).grid(row=i + 1, column=0, columnspan=4, pady=10)

    def back_to_dashboard(self):
        self.frame.destroy()
        from ui.dashboard_ui import DashboardUI
        DashboardUI(self.master)
