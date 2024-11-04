import tkinter as tk
from services.project_service import ProjectService
from tkinter import messagebox

class ProjectUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        tk.Label(self.frame, text="Create New Project").grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        tk.Label(self.frame, text="Project Name:").grid(row=1, column=0)
        self.project_name_entry = tk.Entry(self.frame)
        self.project_name_entry.grid(row=1, column=1)

        tk.Label(self.frame, text="Location:").grid(row=2, column=0)
        self.location_entry = tk.Entry(self.frame)
        self.location_entry.grid(row=2, column=1)

        tk.Label(self.frame, text="Timeline:").grid(row=3, column=0)
        self.timeline_entry = tk.Entry(self.frame)
        self.timeline_entry.grid(row=3, column=1)

        tk.Label(self.frame, text="Material Cost:").grid(row=4, column=0)
        self.material_cost_entry = tk.Entry(self.frame)
        self.material_cost_entry.grid(row=4, column=1)

        tk.Label(self.frame, text="Labor Cost:").grid(row=5, column=0)
        self.labor_cost_entry = tk.Entry(self.frame)
        self.labor_cost_entry.grid(row=5, column=1)

        tk.Label(self.frame, text="Equipment Cost:").grid(row=6, column=0)
        self.equipment_cost_entry = tk.Entry(self.frame)
        self.equipment_cost_entry.grid(row=6, column=1)

        tk.Button(self.frame, text="Save Project", command=self.save_project).grid(row=7, column=0, columnspan=2)

    def save_project(self):
        project_name = self.project_name_entry.get()
        location = self.location_entry.get()
        timeline = self.timeline_entry.get()
        material_cost = float(self.material_cost_entry.get() or 0)
        labor_cost = float(self.labor_cost_entry.get() or 0)
        equipment_cost = float(self.equipment_cost_entry.get() or 0)

        try:
            ProjectService.create_project(project_name, location, timeline, material_cost, labor_cost, equipment_cost)
            messagebox.showinfo("Success", "Project saved successfully!")
            self.frame.destroy()
            from ui.dashboard_ui import DashboardUI
            DashboardUI(self.master)
        except Exception as e:
            messagebox.showerror("Error", str(e))
