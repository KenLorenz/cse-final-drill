from faker import Faker
from random import randrange
from db import mysqli

#  mysql-connector-python
            
def CreateCars():
    sql = mysqli()
    
    sql_connection = sql.connect()
    sql_cursor = sql_connection.cursor()
    
    fake = Faker()
    
    for x in range(1,20):
        
        sql_cursor.execute('SELECT idmodel from model')
        idmodel_list = sql_cursor.fetchall()
        try:
            random_id = fake.random_int(0,len(idmodel_list)-1)
        except:
            print('models table does not have any instances!, run create_model first!')
            exit()
        
        model_idmodel = idmodel_list[random_id][0]
        
        license_num = fake.bothify(text='???###')
        
        cur_mileage = fake.random_int(1,100000)
        
        engine_size = fake.random_int(100,1000)
        
        other_car_details = fake.sentence()
        
        query = f"INSERT INTO car(model_idmodel,license_num,cur_mileage,engine_size,other_car_details)VALUES('{model_idmodel}','{license_num}','{cur_mileage}','{engine_size}','{other_car_details[:45]}');"
        sql_cursor.execute(query)
        
        sql_connection.commit()
        print(f'A New row is created. {x}')
        


if __name__ == "__main__":
    CreateCars()