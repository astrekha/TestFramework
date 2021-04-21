import pyodbc


class Connector:
    def __init__(self, server_name, db_name, logger):
        self.logger = logger
        try:
            conn = pyodbc.connect('Driver={SQL Server};'
                                  'server=%s;'
                                  'database=%s;'
                                  'Trusted_Connection=yes;' % (server_name, db_name))
            self.cursor = conn.cursor()
        except pyodbc.OperationalError as OperationalError:
            print(OperationalError)
            exit()

        except pyodbc.ProgrammingError as ProgrammingError:
            print(ProgrammingError)
            exit()

    def execute(self, query, test_type):
        try:
            self.cursor.execute(query)
            if test_type == 'single':
                return self.cursor.fetchone()[0]
            else:
                return ', '.join(self.cursor.fetchone())

        except pyodbc.ProgrammingError as ProgrammingError:
            print(ProgrammingError)
            exit()

