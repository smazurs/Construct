# Basic test of price tracking and forecasting.
# User input and computer output within terminal.

import datetime

class Project:
    def __init__(self, name, material_cost, labor_cost, start_date, end_date):
        self.name = name
        self.material_cost = material_cost
        self.labor_cost = labor_cost
        self.start_date = start_date
        self.end_date = end_date
        self.total_cost = 0
        self.estimated_cost = 0
        self.forecasted_cost = 0

    def calculate_estimated_cost(self):
        self.total_cost = self.material_cost + self.labor_cost
        print(f"Total Estimated Cost for {self.name}: ${self.total_cost}")
        return self.total_cost

    def forecast_cost(self):
        duration_months = (self.end_date.year - self.start_date.year) * 12 + (self.end_date.month - self.start_date.month)
        forecast_increase = 1.05 ** duration_months
        self.forecasted_cost = self.total_cost * forecast_increase
        print(f"Forecasted Cost for {self.name} (in {duration_months} months): ${self.forecasted_cost:.2f}")
        return self.forecasted_cost


def main():
    print("Welcome to Construct!")
    
    # User input
    project_name = input("Enter the project name: ")
    material_cost = float(input("Enter the material cost ($): "))
    labor_cost = float(input("Enter the labor cost ($): "))
    start_date_str = input("Enter the project start date (YYYY-MM-DD): ")
    end_date_str = input("Enter the project end date (YYYY-MM-DD): ")

    start_date = datetime.datetime.strptime(start_date_str, "%Y-%m-%d")
    end_date = datetime.datetime.strptime(end_date_str, "%Y-%m-%d")

    project = Project(project_name, material_cost, labor_cost, start_date, end_date)

    project.calculate_estimated_cost()

    project.forecast_cost()

if __name__ == "__main__":
    main()
