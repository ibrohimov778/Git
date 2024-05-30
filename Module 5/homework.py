class DbConnect:
    def __init__(self,db_params):
        self.db_params = db_params
    def __enter__(self):
        self.conn = psycopg2.connect(**self.db_params)    