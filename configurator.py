

class Configurator:
    def __init__(self, environment):
        try:
            with open('config.json') as f:
                self.config = eval(f.read())
            self.config = self.config[environment]
        except SyntaxError:
            print("SyntaxError in config file")
            exit()

    def get_server_name(self):
        try:
            return self.config['server_name']
        except KeyError:
            print("'server_name' parameter is missed")
            exit()

    def get_db_name(self):
        try:
            return self.config['db_name']
        except KeyError:
            print("'db_name' parameter is missed")
            exit()

    def get_test_data_folder(self):
        try:
            return self.config['test_data_folder']
        except KeyError:
            print("'test_data_folder' parameter is missed")
            exit()




