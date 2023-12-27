def create_query(table, info): # query constructor
    query = f"INSERT INTO {table}("
    
    column = list()
    row = list()
    for keys, values in info['request'].items():
        column.append(keys)
        row.append(values)

    for x in range(0,len(column)): # column
        query += column[x]
        
        if(x != len(column) - 1):
            query += ","
            
    query += ")"
            
    query += "VALUES("
    for x in range(0,len(row)):
        
        # row_type = f"{type(row[x])}"
        """ if('str' in row_type): # adds quotes if str else don't.
            query += f'"{row[x]}"'
        else:
            query += f'"{row[x]}"' """
        
        query += f'"{row[x]}"'
            
        if(x != len(column) - 1):
            query += ","
            
    query += ");"
    return query

def read_query(table,column,search,offset):
    if column != "":
        query = f"SELECT * FROM {table} WHERE {column} LIKE '%{search}%' LIMIT 20 OFFSET {offset};"
    else:
        query = f"SELECT * FROM {table} LIMIT 20 OFFSET {offset};"
    return query

def update_query(table,info,id,id_name):
    query = f"UPDATE {table} SET "
    
    column = list()
    row = list()
    for keys, values in info['request'].items():
        column.append(keys)
        row.append(values)
    
    for x in range(0,len(column)):
        
        """ if(type(row).__contains__('str')): # adds quotes if str else don't.
            query += f'{column[x]} = "{row[x]}"'
        else:
            query += f'{column[x]} = {row[x]}' """
            
        query += f'{column[x]} = "{row[x]}"'
        
        if(x != len(column) - 1):
            query += ","
            
    """ if type(id).__contains__('str'):
        query += f"WHERE {id_name} = '{id}';"
    else:
        query += f"WHERE {id_name} = {id};" """
        
    query += f' WHERE {id_name} = "{id}";'
    
    return query

def delete_query(table,id,id_name):
    #"DELETE FROM Manufacturer where idManufacturer = {id} "
    return f"DELETE FROM {table} WHERE {id_name} = '{id}'"