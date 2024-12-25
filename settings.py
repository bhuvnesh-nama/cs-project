from db.connect import Database
from db.models import BaseModel

class MigrationManager:
    @staticmethod
    def run():
        cursor = Database.cursor()
        for model_cls in BaseModel.__subclasses__():
            try:
                query = model_cls.get_query()
                cursor.execute(query)

            except Exception as e:
                print(f"Error creating table for {model_cls.__name__}: {e}")
                continue

        Database.commit()
        cursor.close()
        print("All tables created successfully.")
        return True

