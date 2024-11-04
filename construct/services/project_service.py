from models.project_model import ProjectModel

class ProjectService:
    @staticmethod
    def create_project(name, location, timeline, material_cost, labor_cost, equipment_cost):
        ProjectModel.create_project(name, location, timeline, material_cost, labor_cost, equipment_cost)
