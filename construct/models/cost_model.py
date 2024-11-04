from . import get_db_connection

class CostModel:
    @staticmethod
    def add_cost(project_id, material_cost, labor_cost, equipment_cost):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Cost (project_id, material_cost, labor_cost, equipment_cost) VALUES (?, ?, ?, ?)",
                       (project_id, material_cost, labor_cost, equipment_cost))
        conn.commit()
        conn.close()