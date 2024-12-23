from db import fields
from db.connect import Database

from db.fields import Field

class BaseModel:

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        cursor = Database.cursor()

        columns = list(self.__dict__.keys())
        values = list(self.__dict__.values())

        if hasattr(self, "id") and self.id:
            set_clause = ", ".join([f"{column} = %s" for column in columns])
            query = f"UPDATE {self.__class__.__name__.lower()} SET {set_clause} WHERE id = %s"
            values.append(self.id) # id append for where clause
            cursor.execute(query, tuple(values))
            Database.commit()
        else:
            data = ", ".join(["%s"]* len(self.__dict__))

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
        return data
    
    


class Ship(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    name = fields.CharField(null=False)
    type = fields.CharField(null=False)
    weight = fields.DecimalField(null=False)
    flag = fields.CharField(null=False)
    capacity = fields.Integer(null=False)
    arrival_date = fields.DateField(null=False)
    departure_date = fields.DateField()
    status = fields.CharField()

class Cargo(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    cargo_type = fields.CharField(null=False)
    weight = fields.DecimalField(null=False)
    origin = fields.CharField(null=False)
    destination = fields.CharField(null=False)
    storage_zone = fields.CharField(null=False)
    ship_id = fields.ForeignField(to=Ship, to_field="id")
    status = fields.CharField(null=False)

class Passenger(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    name = fields.CharField(null=False)
    age = fields.Integer(null=False)
    passport_no = fields.CharField(null=False)
    boarding_date = fields.DateField(null=False)
    disembark_date = fields.DateField(null=False)
    gender = fields.CharField(null=False)
    origin = fields.CharField(null=False)
    destination = fields.CharField(null=False)
    ship_id = fields.ForeignField(to=Ship, to_field="id")
    status = fields.CharField(null=False)

class Crew(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    name = fields.CharField(null=False)
    age = fields.Integer(null=False)
    role = fields.CharField(null=False)
    origin = fields.CharField(null=False)
    start_date = fields.DateField(null=False)
    end_date  = fields.DateField()
    ship_id = fields.ForeignField(to=Ship, to_field="id")

class DockingSchedule(BaseModel):
    id = fields.Integer(primary_key=True, auto_increment=True)
    arrival_date = fields.DateField(null=False)
    status = fields.CharField(null=False)
    departure_date = fields.DateField()
    ship_id = fields.ForeignField(to=Ship, to_field="id")
