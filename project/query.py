def create_query(table, info): # query constructor
    query = f"INSERT INTO {table}("
    
    column = list(info.keys)
    row = list(info.values)
    
    for x in range(0,len(column)-1): # column
        query += column[x]
        
        if(x != len(column) - 1):
            query += ","
        else:
            query += ")"
            
    query += "VALUES("
    for x in range(0,len(row)-1):
        
        
        if(type(row).__contains__('str')): # adds quotes if str else don't.
            query += f'"{row[x]}"'
        else:
            query += row[x]
            
        if(x != len(column) - 1):
            query += ","
        else:
            query += ");"
        
    return query

def update_query(table,info,id,id_name):
    query = f"INSERT {table} SET "
    
    column = list(info.keys)
    row = list(info.values)
    
    for x in range(0,len(column)-1):
        
        if(type(row).__contains__('str')): # adds quotes if str else don't.
            query += f'{column[x]} = "{row[x]}"'
        else:
            query += f'{column[x]} = {row[x]}'
        
        if(x != len(column) - 1):
            query += ","
            
    if type(id).__contains__('str'):
        query += f"WHERE {id_name} = '{id}';"
    else:
        query += f"WHERE {id_name} = {id};"
        
    return query
    
    
    
    
    """ for x in range(0,len(column)-1): # column
        query += column[x]
        
        if(x != len(column) - 1):
            query += ","
        else:
            query += ")"
            
    query += "VALUES("
    for x in range(0,len(row)-1):
        
        
        if(type(row).__contains__('str')): # adds quotes if str else don't.
            query += f'"{row[x]}"'
        else:
            query += row[x]
            
        if(x != len(column) - 1):
            query += ","
        else:
            query += ");"
         """
    return query