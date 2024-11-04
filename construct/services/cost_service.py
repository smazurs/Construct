from models.cost_model import CostModel

class CostService:
    @staticmethod
    def calculate_total_cost(project_id):
        # Retrieve and sum all costs for the project
        costs = CostModel.get_costs_by_project(project_id)
        return sum(cost['material_cost'] + cost['labor_cost'] + cost['equipment_cost'] for cost in costs)
    
    @staticmethod
    def forecast_cost(project_id, months):
        total_cost = CostService.calculate_total_cost(project_id)
        return total_cost * (1.05 ** months)  # Simple 5% growth rate per month
