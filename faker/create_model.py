from faker import Faker
from random import randrange
from db import mysqli

def CreateModels():
    
    sql = mysqli()
    
    sql_connection = sql.connect()
    sql_cursor = sql_connection.cursor()
    
    fake = Faker()
    
    for x in range(1,21):
        
        sql_cursor.execute('SELECT idManufacturer from Manufacturer')
        idManufacturer_list = sql_cursor.fetchall()
        
        try:
            random_id = fake.random_int(0,len(idManufacturer_list)-1)
        except:
            print('models table does not have any instances!, run create_manufacturer first!')
            exit()
        
        Manufacturer_idManufacturer = idManufacturer_list[random_id][0]
        
        model_code = fake.bothify(text='???###')
        
        daily_hire_rate = fake.random_int(50,10000)
        
        name = fake.bothify(text="??????")
        query = f"INSERT INTO model(Manufacturer_idManufacturer,model_code,daily_hire_rate,name) VALUES('{Manufacturer_idManufacturer}','{model_code}','{daily_hire_rate}','{name}');"
        sql_cursor.execute(query)
        
        sql_connection.commit()
        print(f'A New row is created. {x}')

if __name__ == "__main__":
    CreateModels()