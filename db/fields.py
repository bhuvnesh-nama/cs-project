


class Field:
    def __init__(self,primary_key=False, unique=False, null=True, **kwargs):
        self.null = null
        self.primary_key = primary_key
        self.unique = unique
        self.extra_args = kwargs
    
    def get_sql():
        raise NotImplementedError("Not implemented 'get_sql' in subclasses")



class Integer(Field):
    def __init__(self,auto_increment=False, **kwargs):
        super().__init__(**kwargs)
        self.auto_increment = auto_increment
    def get_sql(self):
        sql = "INT"
        if self.primary_key:
            sql += " PRIMARY KEY"
        elif self.unique:
            sql += " UNIQUE"
        if not self.null:
            sql += " NOT NULL"
        if self.auto_increment:
            sql += " AUTO_INCREMENT"
        return sql

class CharField(Field):
    def __init__(self, max_length=255, **kwargs):
        super().__init__(**kwargs)
        self.max_length = max_length

    def get_sql(self):
        sql = f"VARCHAR({self.max_length})"

        if self.unique:
            sql= " UNIQUE"
        if not self.null:
            sql += " NOT NULL"
        return sql
class DecimalField(Field):
    def __init__(self, max_digits=10, decimal_places=2, **kwargs):
        super().__init__(**kwargs)
        self.max_digits = max_digits
        self.decimal_places = decimal_places

    def get_sql(self):
        
        sql = f"DECIMAL({self.max_digits}, {self.decimal_places})"
        if self.unique:
            sql += " UNIQUE"
        if not self.null:
            sql += " NOT NULL"
        if 'default' in self.extra_args:
            sql += f" DEFAULT {self.extra_args['default']}"
        return sql


class Boolean(Field):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)  # Pass all kwargs to the parent class

    def get_sql(self):
        sql = "BOOLEAN"
        if not self.null:
            sql += " NOT NULL"
        
        # Example of using a custom argument from kwargs
        if 'default' in self.extra_args:
            sql += f" DEFAULT {self.extra_args['default']}"
        return sql

class ForeignField(Field):
    def __init__(self,to, to_field="id", **kwargs):
        super().__init__(**kwargs)
        self.to = to
        self.to_field = to_field

    def get_sql(self):
        sql = "INT"
        if not self.null:
            sql += " NOT NULL"
        if self.unique:
            sql += " UNIQUE"
        sql += f", FOREIGN KEY ({self.to_field}) REFERENCES {self.to.__name__.lower()}({self.to_field})"
        return sql

class DateField(Field):
    def get_sql(self):
        sql = "DATE"
        if not self.null:
            sql += " NOT NULL"
        return sql