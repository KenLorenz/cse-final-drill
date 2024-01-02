from project.app import app
import unittest
import warnings
from dict2xml import dict2xml

import requests
class appTest(unittest.TestCase):
    
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()
        
        warnings.simplefilter("ignore", category=DeprecationWarning)
        
    def test_invalid_login_xml(self):
        url = "http://localhost:5000/login?format=xml"

        input = dict2xml({"request":{"www1232@gmail.com":{"password":"123456"}}})
        
        response = self.app.post(url, data=input)
        self.assertEqual(response.status_code,400)
        self.assertEqual(response.data.decode(),"<message>Missing Email or Password</message>")
    
    def test_add(self):
        url = "http://localhost:5000/login"
        
        input = {"email":"kenlorenz420@gmail.com", "password":"122846"}
        response = self.app.post(url, json=input)
        response_str = response.data.decode()
        response_str = response_str.replace('\n','')
        token = response_str.split("\"")[3]

        url = "http://localhost:5000/car/add"
        
        input = {
            "idcar": 999999,
            "model_idmodel": 1,
            "license_num": "ABC123",
            "cur_mileage": 12345,
            "engine_size": 90000,
            "other_car_details": "TESTING123"
        }
        header = {'token-access': f'{token}'}
        response2 = self.app.post(url, json=input, headers=header)

        self.assertTrue('"rows_affected":1' in response2.data.decode())
    
    def test_aupdate(self): # added a to prioritize
        url = "http://localhost:5000/login"
        
        input = {"email":"kenlorenz420@gmail.com", "password":"122846"}
        response = self.app.post(url, json=input)
        response_str = response.data.decode()
        response_str = response_str.replace('\n','')
        token = response_str.split("\"")[3]

        url = "http://localhost:5000/car/update?id=999999"
        
        input = {
            "model_idmodel": 1,
            "license_num": "AAAA",
            "cur_mileage": 1,
            "engine_size": 9,
            "other_car_details": "T"
        }
        
        header = {'token-access': f'{token}'}
        response2 = self.app.post(url, json=input, headers=header)

        self.assertTrue('"rows_affected":1' in response2.data.decode())
        
    def test_read(self):
        url = "http://localhost:5000/login"
        
        input = {"email":"kenlorenz420@gmail.com", "password":"122846"}
        response = self.app.post(url, json=input)
        response_str = response.data.decode()
        response_str = response_str.replace('\n','')
        token = response_str.split("\"")[3]

        url = "http://localhost:5000/car/read?field=other_car_details&search=Snail&page=1"
        
        header = {'token-access': f'{token}'}
        response2 = self.app.get(url, headers=header)
        print(response2.data.decode())
        self.assertEquals(response2.data.decode(), '[[97,10,"XYZ321","54321","15","Snail car"]]\n')
        
    def test_delete(self):
        url = "http://localhost:5000/login"
        
        input = {"email":"kenlorenz420@gmail.com", "password":"122846"}
        response = self.app.post(url, json=input)
        response_str = response.data.decode()
        response_str = response_str.replace('\n','')
        token = response_str.split("\"")[3]
        
        url = "http://localhost:5000/car/delete?id=999999"
        
        header = {'token-access': f'{token}'}
        response2 = self.app.get(url, headers=header)
        
        self.assertTrue('"rows_affected":1' in response2.data.decode())

    def test_add_xml(self):
        url = "http://localhost:5000/login"
        
        input = {"email":"kenlorenz420@gmail.com", "password":"122846"}
        response = self.app.post(url, json=input)
        response_str = response.data.decode()
        response_str = response_str.replace('\n','')
        token = response_str.split("\"")[3]

        url = "http://localhost:5000/car/add?format=xml"
        
        input = {"request":{
            "idcar": 1000000,
            "model_idmodel": 1,
            "license_num": "ABC123",
            "cur_mileage": 12345,
            "engine_size": 90000,
            "other_car_details": "TESTING123"
        }}
        input = dict2xml(input)
        header = {'token-access': f'{token}'}
        
        response2 = self.app.post(url, data=input, headers=header)

        self.assertTrue('"rows_affected":1' in response2.data.decode())

    def test_aupdate_xml(self): # added a to prioritize
        url = "http://localhost:5000/login"
        
        input = {"email":"kenlorenz420@gmail.com", "password":"122846"}
        response = self.app.post(url, json=input)
        response_str = response.data.decode()
        response_str = response_str.replace('\n','')
        token = response_str.split("\"")[3]

        url = "http://localhost:5000/car/update?id=1000000&format=xml"
        
        input = {"request":{
            "model_idmodel": 1,
            "license_num": "ABC123",
            "cur_mileage": 12345,
            "engine_size": 90000,
            "other_car_details": "XMLTESTING"
        }}
        input = dict2xml(input)
        
        header = {'token-access': f'{token}'}
        response2 = self.app.post(url, data=input, headers=header)

        self.assertTrue('"rows_affected":1' in response2.data.decode())
        
    def test_delete_xml(self):
        url = "http://localhost:5000/login"
        
        input = {"email":"kenlorenz420@gmail.com", "password":"122846"}
        response = self.app.post(url, json=input)
        response_str = response.data.decode()
        response_str = response_str.replace('\n','')
        token = response_str.split("\"")[3]
        
        url = "http://localhost:5000/car/delete?id=1000000"
        
        header = {'token-access': f'{token}'}
        response2 = self.app.get(url, headers=header)
        
        self.assertTrue('"rows_affected":1' in response2.data.decode())
        
if __name__=="__main__":
    unittest.main()