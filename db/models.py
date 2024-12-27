from db import fields
from db.connect import Database
from db.fields import Field

class BaseModel:

    # This constructor is for insert purpose
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    # This class method is for insert purpose
    def save(self):
        cursor = Database.cursor()

        
        columns = ", ".join(self.__dict__.keys())
        data = ", ".join(["%s"]* len(self.__dict__.values()))

        query = f"INSERT INTO {self.__class__.__name__.lower()} ({columns}) VALUES ({data})"
        cursor.execute(query, tuple(self.__dict__.values()))
        Database.commit()



    # This class method is for migration of the database
    @classmethod
    def get_query(cls):
        columns = []
        for attribute_name, attribute_value in cls.__dict__.items():
            if isinstance(attribute_value, Field):
                column_name = attribute_name
                column_definition = attribute_value.get_sql()
                columns.append(f"{column_name} {column_definition}")
        columns_sql = ", ".join(columns)
        return f"CREATE TABLE IF NOT EXISTS {cls.__name__.lower()} ({columns_sql})"
    









    @classmethod
    def get(cls, **kwargs):
        cursor = Database.cursor()
        if kwargs == {}:
            query = f"SELECT * FROM {cls.__name__.lower()}"
            cursor.execute(query)
        else:
            where_clause = " AND".join([f"{key}= %s" for key in kwargs.keys()])
            query = f"SELECT * FROM {cls.__name__.lower()} WHERE {where_clause}"
            cursor.execute(query, tuple(kwargs.values()))
        data = cursor.fetchall()
        # data = tuple(data)
        return data
    
    @classmethod
    def update_by_id(cls, id, **updated_data):
        cursor = Database.cursor()
        set_clause = ", ".join(f"{key}=%s" for key in updated_data.keys())

        where_clause = f"id=%s"

        query = f"UPDATE {cls.__name__.lower()} SET {set_clause} WHERE {where_clause}"
        cursor.execute(query, tuple(updated_data.values()) + (id,))
        Database.commit()
    
    @classmethod
    def delete_by_id(cls, id):
        cursor = Database.cursor()
        query = f"DELETE FROM {cls.__name__.lower()} WHERE id=%s"

        cursor.execute(query, (id,))

class Ship(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    name = fields.CharField(null=False)
    weight = fields.DecimalField(null=False)
    flag = fields.CharField(null=False)
    capacity = fields.Integer(null=False)
    arrival_date = fields.DateField(null=False)
    departure_date = fields.DateField()
    status = fields.CharField()

class StorageZone(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    name = fields.CharField(null=False)
    max_capacity = fields.Integer(null=False)

class Container(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    weight = fields.DecimalField(null=False)
    storage_zone_id = fields.ForeignField(to=StorageZone,name="storage_zone_id", to_field="id")
    ship_id = fields.ForeignField(to=Ship,name="ship_id", to_field="id")

class DockingSchedule(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    schedule_date = fields.DateField(null=False)
    status = fields.CharField(null=False)
    ship_id = fields.ForeignField(to=Ship,name="ship_id", to_field="id")

