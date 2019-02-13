from robot.libraries.BuiltIn import BuiltIn
import requests

class TDSlibrary:

    def __init__(self, host='localhost', port=80):
        self.port = port
        self.host = host

    def fetch_testdata(self, tablename):
        uri = 'http://' + self.host + ':' + str(self.port) + '/api/v1/testdata/' + tablename
        data = requests.get(uri).json()
        BuiltIn().log(data)

    def add_dataset(self):
        pass

    def remove_dataset(self):
        pass

    def add_data_to_dataset(self):
        pass

    def remove_data_from_dataset(self):
        pass

    def add_values_to_dataset(self):
        pass
