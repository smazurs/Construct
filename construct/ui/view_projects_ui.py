import tkinter as tk
from models.project_model import ProjectModel
from services.forecast_service import ForecastService
from tkinter import messagebox

class ViewProjectsUI:
    def __init__(self, master):
        self.master = master
        self.frame = tk.Frame(self.master)
        self.frame.pack()

        tk.Label(self.frame, text="Select Forecast Period:").grid(row=0, column=0, padx=10, pady=5)
        self.time_range_var = tk.StringVar(value="1 Year")
        time_options = ["3 Months", "6 Months", "1 Year", "2 Years"]
        self.time_dropdown = tk.OptionMenu(self.frame, self.time_range_var, *time_options)
        self.time_dropdown.grid(row=0, column=1, padx=10, pady=5)
        
        tk.Button(self.frame, text="Update Forecast", command=self.update_forecast).grid(row=0, column=2, padx=10, pady=5)

        tk.Label(self.frame, text="Existing Projects").grid(row=1, column=0, columnspan=7, padx=10, pady=10)

        headers = ["Project Name", "Location", "Timeline", "Material Cost", "Labor Cost", "Equipment Cost", "Forecasted Cost"]
        for col, header in enumerate(headers):
            tk.Label(self.frame, text=header, borderwidth=1, relief="solid").grid(row=2, column=col)

        self.display_projects()

    def display_projects(self):
        projects = ProjectModel.get_all_projects()
        row_offset = 3
        for i, project in enumerate(projects, start=row_offset):
            project_name, location, timeline, material_cost, labor_cost, equipment_cost = project
            forecasted_cost = self.calculate_forecast(material_cost, labor_cost, equipment_cost)

            for col, value in enumerate([project_name, location, timeline, material_cost, labor_cost, equipment_cost, round(forecasted_cost, 2)]):
                tk.Label(self.frame, text=value, borderwidth=1, relief="solid").grid(row=i, column=col)

        tk.Button(self.frame, text="Back to Dashboard", command=self.back_to_dashboard).grid(row=i + 1, column=0, columnspan=7, pady=10)

    def calculate_forecast(self, material_cost, labor_cost, equipment_cost):
        time_range = self.time_range_var.get()
        if time_range == "3 Months":
            growth_rate = 0.05
            duration = 0.25
        elif time_range == "6 Months":
            growth_rate = 0.05
            duration = 0.5
        elif time_range == "1 Year":
            growth_rate = 0.05
            duration = 1
        elif time_range == "2 Years":
            growth_rate = 0.05
            duration = 2
        else:
            growth_rate = 0.05
            duration = 1

        return ForecastService.forecast_project_cost(material_cost, labor_cost, equipment_cost, growth_rate, duration)

    def update_forecast(self):
        for widget in self.frame.winfo_children():
            widget.destroy()
        self.__init__(self.master)

    def back_to_dashboard(self):
        self.frame.destroy()
        from ui.dashboard_ui import DashboardUI
        DashboardUI(self.master)
