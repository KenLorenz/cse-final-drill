from faker import Faker
from random import randrange
from db import mysqli


def CreateManufacturer():
    sql = mysqli()
    
    sql_connection = sql.connect()
    sql_cursor = sql_connection.cursor()
    
    fake = Faker()
    
    for x in range(1,21):
        
        name = fake.company()
        details = fake.sentence()
        
        query = f"INSERT INTO Manufacturer(name,details)VALUES('{name}','{details[:45]}');"
        sql_cursor.execute(query)
        
        sql_connection.commit()
        print(f'A New row is created. {x}')
    sql_cursor.close()

if __name__ == "__main__":
    CreateManufacturer()