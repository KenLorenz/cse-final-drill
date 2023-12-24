from flask import Flask, make_response, jsonify, request
import mysql.connector # flask-mysqldb doesnt work, probably because I use percona
import jwt # security
import xmltodict
from dict2xml import dict2xml
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

""" -- Misc -- """

@app.route("/")
def hello_world():
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

def query_fail_response(format):
    msg = {"message": "Query error, json must contain all columns"}
    if format == "json":
        response = make_response(
            jsonify(
                msg
                ),
            400)
    else:
        response = make_response(
            dict2xml(
                msg
                ),
            400)
        
    return response

def rows_affected_response(rows_affected):
    if rows_affected < 1: 
        response = make_response(
            jsonify(
                {"message": "Action Failed.", "rows_affected": rows_affected}
                ),
            400)
    else:
        response = make_response(
            jsonify(
                {"message": "Action Successful.", "rows_affected": rows_affected}
                ),
            200)
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

""" -- Manufacturers -- """

@app.route("/manufacturers/add",methods=["POST"]) # CREATE, POST
def add_models(): 
    mysql_cursor = sql.cursor()
    
    format = request.args.get('format',default="json")
    info = format_get(format)

    if str(info).__contains__("400 BAD REQUEST"):
        return info
    
    try:
        mysql_cursor.execute(
            f"""
            INSERT INTO Manufacturer(name,details)
            VALUES(
                "{info['request']['name']}",
                "{info['request']['details']}"
            );
            """
        )
    except:
        return query_fail_response(format)
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected)

@app.route("/manufacturers",methods=["GET"]) # READ ALL
def get_cars():
    page = request.args.get('page', default=1)
    
    if(int(page) < 1):
        page = 1
        
    offset = (int(page) - 1) * 20
    
    query_results = fetch_all(f"SELECT * FROM Manufacturer LIMIT 20 OFFSET {offset};")
    return make_response(jsonify(query_results),200)

@app.route("/manufacturers/search",methods=["GET"]) # name search
def search_cars():
    search = request.args.get('license',default="")
    
    mysql_cursor = sql.cursor()
    
    query_results = fetch_all(f"SELECT * FROM Manufacturer WHERE name LIKE '%{search}%';")
    mysql_cursor.close()
    
    return make_response(jsonify(query_results),200)
    

@app.route("/manufacturers/update", methods=["POST"]) # UPDATE
def update_cars():
    id = request.args.get('id') # ?id=<int>
    
    mysql_cursor = sql.cursor()
    
    format = request.args.get('format',default="json")
    info = format_get(format)

    if str(info).__contains__("400 BAD REQUEST"):
        return info
    
    try:
        mysql_cursor.execute(
            f"""
            UPDATE Manufacturer SET
            name = {info['request']['name']},
            details = "{info['request']['details']}"
            WHERE idManufacturer = {id};
            """
        )
    except:
        return query_fail_response(format)
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected)


@app.route("/manufacturers/delete", methods=["GET"])
def delete_cars():
    id = request.args.get('id', default=0)
    mysql_cursor = sql.cursor()
    mysql_cursor.execute(f"DELETE FROM Manufacturer where idManufacturer = {id} ")
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    rows_affected_response(rows_affected)
    
""" -- Manufacturers -- """


""" -- Models -- """

@app.route("/models/add",methods=["POST"]) # CREATE, POST
def add_models(): 
    mysql_cursor = sql.cursor()
    
    format = request.args.get('format',default="json")
    info = format_get(format)

    if str(info).__contains__("400 BAD REQUEST"):
        return info
    
    try:
        mysql_cursor.execute(
            f"""
            INSERT INTO model(Manufacturer_idManufacturer,model_code,daily_hire_rate,name)
            VALUES(
                {info['car_data']['Manufacturer_idManufacturer']},
                "{info['car_data']['model_code']}",
                {info['car_data']['daily_hire_rate']},
                "{info['car_data']['name']}"
            );
            """
        )
    except:
        return query_fail_response(format)
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected)

@app.route("/models",methods=["GET"]) # READ ALL
def get_cars():
    page = request.args.get('page', default=1)
    
    if(int(page) < 1):
        page = 1
        
    offset = (int(page) - 1) * 20
    
    query_results = fetch_all(f"SELECT * FROM model LIMIT 20 OFFSET {offset};")
    return make_response(jsonify(query_results),200)

@app.route("/models/search",methods=["GET"]) # name search
def search_cars():
    search = request.args.get('license',default="")
    
    mysql_cursor = sql.cursor()
    
    query_results = fetch_all(f"SELECT * FROM model WHERE name LIKE '%{search}%';")
    mysql_cursor.close()
    
    return make_response(jsonify(query_results),200)
    

@app.route("/models/update", methods=["POST"]) # UPDATE
def update_cars():
    id = request.args.get('id') # ?id=<int>
    
    mysql_cursor = sql.cursor()
    
    format = request.args.get('format',default="json")
    info = format_get(format)

    if str(info).__contains__("400 BAD REQUEST"):
        return info
    
    try:
        mysql_cursor.execute(
            f"""
            UPDATE model SET
            Manufacturer_idManufacturer = {info['request']['Manufacturer_idManufacturer']},
            model_code = "{info['request']['model_code']}",
            daily_hire_rate = {info['request']['daily_hire_rate']},
            name = {info['request']['name']}
            WHERE idmodel = {id};
            """
        )
    except:
        return query_fail_response(format)
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected)


@app.route("/models/delete", methods=["GET"])
def delete_cars():
    id = request.args.get('id', default=0)
    mysql_cursor = sql.cursor()
    mysql_cursor.execute(f"DELETE FROM model where idmodel = {id} ")
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    rows_affected_response(rows_affected)
    
""" -- Models -- """


""" -- Cars -- """

@app.route("/cars/add",methods=["POST"]) # CREATE, POST
def add_cars(): 
    mysql_cursor = sql.cursor()
    
    format = request.args.get('format',default="json")
    info = format_get(format)

    if str(info).__contains__("400 BAD REQUEST"):
        return info
    
    try:
        mysql_cursor.execute(
            f"""
            INSERT INTO car(model_idmodel,license_num,cur_mileage,engine_size,other_car_details)
            VALUES(
                {info['request']['model_idmodel']},
                "{info['request']['license_num']}",
                {info['request']['cur_mileage']},
                {info['request']['engine_size']},
                "{info['request']['other_car_details']}"
            );
            """
        )
    except:
        return query_fail_response(format)
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected)

@app.route("/cars",methods=["GET"]) # READ ALL
def get_cars():
    page = request.args.get('page', default=1)
    
    if(int(page) < 1):
        page = 1
        
    offset = (int(page) - 1) * 20
    
    query_results = fetch_all(f"SELECT * FROM car LIMIT 20 OFFSET {offset};")
    return make_response(jsonify(query_results),200)

@app.route("/cars/search",methods=["GET"]) # license num search
def search_cars():
    search = request.args.get('license',default="")
    
    mysql_cursor = sql.cursor()
    
    query_results = fetch_all(f"SELECT * FROM car WHERE license_num LIKE '%{search}%';")
    mysql_cursor.close()
    
    return make_response(jsonify(query_results),200)
    


@app.route("/cars/update", methods=["POST"]) # UPDATE
def update_cars():
    id = request.args.get('id') # ?id=<int>
    
    mysql_cursor = sql.cursor()
    
    format = request.args.get('format',default="json")
    info = format_get(format)

    if str(info).__contains__("400 BAD REQUEST"):
        return info
    
    try:
        mysql_cursor.execute(
            f"""
            UPDATE car SET
            model_idmodel = {info['request']['model_idmodel']},
            license_num = "{info['request']['license_num']}",
            cur_mileage = {info['request']['cur_mileage']},
            engine_size = {info['request']['engine_size']},
            other_car_details = "{info['request']['other_car_details']}"
            WHERE idcar = {id};
            """
        )
    except:
        return query_fail_response(format)
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    return rows_affected_response(rows_affected)


@app.route("/cars/delete", methods=["GET"])
def delete_cars():
    id = request.args.get('id', default=0)
    mysql_cursor = sql.cursor()
    mysql_cursor.execute(f"DELETE FROM car where idcar = {id} ")
    
    sql.commit()
    rows_affected = mysql_cursor.rowcount
    mysql_cursor.close()
    
    rows_affected_response(rows_affected)
    
""" -- Cars -- """

if __name__ == "__main__":
    app.run(debug=True)