from robot.libraries.BuiltIn import BuiltIn
import requests
import json

class TDSlibrary:

    def __init__(self, host='localhost', port=80):
        self.port = port
        self.host = host

    def fetch_testdata(self, tablename):
        uri = 'http://' + self.host + ':' + str(self.port) + '/api/v1/testdata/' + tablename
        data = requests.get(uri)
        BuiltIn().log(data)
        jsondata = json.loads(data.content)
        temp_string = jsondata['testdata']['item']

        my_dict = (eval(temp_string))
        for item in my_dict:
            key = '${' + item + '}'
            value = my_dict[item]
            BuiltIn().set_global_variable(key, value)

    def add_dataset(self, setname):
        uri = 'http://' + self.host + ':' + str(self.port) + '/api/v1/testdata'
        req_headers = {'Content-Type': 'application/json'}
        testdataitem1 = {'username':'user1', 'password': 'password1', 'email': 'user1@nowhere.com'}
        testdataitem2 = {'username':'user2', 'password': 'password2', 'email': 'user2@nowhere.com'}
        req_body = {
            "dataset": setname,
            "items": [
                testdataitem1,
                testdataitem2,
            ]
        }
        requests.post(uri, headers = req_headers, data = json.dumps(req_body))

    def remove_dataset(self, setname):
        uri = 'http://' + self.host + ':' + str(self.port) + '/api/v1/testdata/' + setname
        requests.delete(uri, data = setname)

    def add_data_to_dataset(self):
        pass

    def remove_data_from_dataset(self):
        pass

    def add_values_to_dataset(self):
        pass
