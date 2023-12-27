from flask import Flask, make_response, jsonify, request
import mysql.connector # flask-mysqldb doesnt work, probably because I use percona
import jwt # security
import xmltodict
from dict2xml import dict2xml
from query import *
from verify import *
# Manufacturer can't be deleted if related to model, model can't be deleted if related to cars, cars can be deleted immediately.

app = Flask(__name__)
app.config["MYSQL_HOST"] = "localhost"
app.config["MYSQL_PORT"] = "3306"
app.config["MYSQL_USER"] = "ren"
app.config["MYSQL_PASSWORD"] = "122846"
app.config["MYSQL_DB"] = "cseCars"

sql = mysql.connector.connect(
    host=app.config["MYSQL_HOST"],
    port=app.config["MYSQL_PORT"],
    user=app.config["MYSQL_USER"],
    password=app.config["MYSQL_PASSWORD"],
    database=app.config["MYSQL_DB"]
    )

@app.route("/<string:table>/add",methods=["POST"])
def create(table): 
    
    # phase 1: get format and data in accordance to input
    format = request.args.get('format',default="json")
    info = format_get(format) # input request

    if str(info).__contains__("400 BAD REQUEST"):
        return info
    
    # table input validation
    mysql_cursor = sql.cursor()
    
    # checks if table refers to existing table.
    query_values = fetch_all("show tables;") # returns tuples
    query_values_list = list()
    for x in query_values:
        query_values_list.append(x[0])
        
    if table not in query_values_list: # if url value not in available tables
        mysql_cursor.close()
        
        return query_fail_response(format, "Unknown URL, double check. ",404)
    
    # phase 2: execute query
    mysql_cursor.execute(create_query(table,info))
    
    # phase 3: apply query and return response
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected,201,400)

@app.route("/<string:table>/read",methods=["GET"])
def read(table):
    
    page = request.args.get('page', default=1)
    column = request.args.get('field',default="")
    search = request.args.get('search',default="")
    
    mysql_cursor = sql.cursor()
    
    # check inputs
    
    # checks table
    query_values = fetch_all("show tables;") # returns tuples
    query_values_list = list()
    for x in query_values:
        query_values_list.append(x[0])
        
    if table not in query_values_list: # if url value not in available tables  
        return query_fail_response(format, "Unknown URL, double check. ",404)
    
    # checks column
    if column != "":
        query_values = fetch_all(f"DESCRIBE {table};") # tuple
        query_values_list = list()
        for x in query_values:
            query_values_list.append(x[0])
        
        if column not in query_values_list:
            mysql_cursor.close()
            return query_fail_response(format,"Invalid Field Name.",400)
        
    elif column == "" and search != "":
        return query_fail_response(format, "Tried to search but no specified field.",400)
    
    # checks page
    if(int(page) < 1):
        page = 1
        
    offset = (int(page) - 1) * 20
    
    query_results = fetch_all(read_query(table,column,search,offset))
    
    mysql_cursor.close()
    return make_response(jsonify(query_results),200)

@app.route("/<string:table>/update",methods=["POST"])
def update(table):
    id = request.args.get('id')

    format = request.args.get('format',default="json")
    info = format_get(format) # input request

    if str(info).__contains__("400 BAD REQUEST"):
        return info
    
    if id == None:
        return query_fail_response(format, "ID was not specified",400)
    
    mysql_cursor = sql.cursor()
    
    query_values = fetch_all("show tables;") # returns tuples
    query_values_list = list()
    for x in query_values:
        query_values_list.append(x[0])
        
    if table not in query_values_list:
        mysql_cursor.close()
        
        return query_fail_response(format, "Unknown URL, double check. ",404)
    
    id_query = fetch_all(f"DESCRIBE {table};")
    id_name = id_query[0][0] # assumes the primary id name is always first
    
    mysql_cursor.execute(update_query(table,info,id,id_name))
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected,200,400)

@app.route("/<string:table>/delete",methods=["GET"])
def delete(table):
    id = request.args.get('id',default="")
    
    if id == "":
        return query_fail_response(format, "ID was not specified",400)
    
    mysql_cursor = sql.cursor()
    
    query_values = fetch_all("show tables;") # returns tuples
    query_values_list = list()
    for x in query_values:
        query_values_list.append(x[0])
        
    if table not in query_values_list:
        mysql_cursor.close()
        
        return query_fail_response(format, "Unknown URL, double check. ",404)
    
    id_query = fetch_all(f"DESCRIBE {table};")
    id_name = id_query[0][0] # assumes the primary id name is always first
    
    mysql_cursor.execute(delete_query(table,id,id_name))
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected,200,400)

""" -- Misc -- """

@app.route("/")
def project_intro():
    return "<p>CSE Final Drill Project, add to url: /cars/, /models/, /manufacturer/</p>"

def fetch_all(query): # fetches all values from a query
    mysql_cursor = sql.cursor()
    mysql_cursor.execute(query)
    
    results = mysql_cursor.fetchall()
    
    mysql_cursor.close()
    return results

def format_response():
    return make_response(
        jsonify(
            {"message": "Format error. xml and json are the only ones available"} 
        ),
        400)

def query_fail_response(format,message,code_fail): # add parameter message
    if format == "json":
        response = make_response(
            jsonify(
                {"message": f"{message}"}
                ),
            code_fail)
    else:
        response = make_response(
            dict2xml(
                {"message": f"{message}"}
                ),
            code_fail)
        
    return response

def rows_affected_response(rows_affected,code_success,code_fail):
    if rows_affected < 1: 
        response = make_response(
            jsonify(
                {"message": "Action Failed.", "rows_affected": rows_affected}
                ),
            code_success)
    else:
        response = make_response(
            jsonify(
                {"message": "Action Successful.", "rows_affected": rows_affected}
                ),
            code_fail)
    return response


def format_get(format):
    if(format == 'json'):
        query_info = request.get_json()
        info = {'request': None}
        info['request'] = query_info
    elif (format == "xml"):
        info = request.data # xml
        info = xmltodict.parse(info)
    else:
        return format_response()
    
    return info

""" -- Misc -- """



if __name__ == "__main__":
    app.run(debug=True)