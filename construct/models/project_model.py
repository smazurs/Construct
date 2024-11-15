from . import get_db_connection

class ProjectModel:
    @staticmethod
    def create_project(name, location, timeline, material_cost, labor_cost, equipment_cost):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO Project (name, location, timeline)
            VALUES (?, ?, ?)
        ''', (name, location, timeline))
        project_id = cursor.lastrowid
        cursor.execute('''
            INSERT INTO Cost (project_id, material_cost, labor_cost, equipment_cost)
            VALUES (?, ?, ?, ?)
        ''', (project_id, material_cost, labor_cost, equipment_cost))
        conn.commit()
        conn.close()

    @staticmethod
    def get_all_projects():
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            SELECT p.name, p.location, p.timeline, c.material_cost, c.labor_cost, c.equipment_cost
            FROM Project p
            JOIN Cost c ON p.id = c.project_id
        ''')
        projects = cursor.fetchall()
        conn.close()
        return projects

