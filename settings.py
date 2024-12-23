DATABASE = {
    "host": "localhost",
    "user": "root",
    "password": "0141",
    "database": "test"
}

from db.connect import Database
from db.models import BaseModel
# migrations.py

class MigrationManager:
    @staticmethod
    def run():
        # Ensure the database connection is established
        cursor = Database.cursor()
        for model_cls in BaseModel.__subclasses__():
            try:
                query = model_cls.get_query()
                print(query)
                cursor.execute(query)

            except Exception as e:
                print(f"Error creating table for {model_cls.__name__}: {e}")
                continue

        Database.commit()
        cursor.close()
        print("All tables created successfully.")

