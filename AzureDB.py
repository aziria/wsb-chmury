import pypyodbc
import azurecred


class AzureDB:


    dsn='DRIVER='+azurecred.AZDBDRIVER+';SERVER='+azurecred.AZDBSERVER+';PORT=1433;DATABASE='+azurecred.AZDBNAME+';UID='+azurecred.AZDBUSER+';PWD='+ azurecred.AZDBPW

    def __init__(self):
        self.conn = pypyodbc.connect(self.dsn)
        self.cursor = self.conn.cursor()

    def finalize(self):
        if self.conn:
            self.conn.close()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.finalize()

    def __enter__(self):
        return self


    def azureGetData(self):
        try:
            self.cursor.execute("SELECT product, details from data2")
            data = self.cursor.fetchall()
            return data
        except pypyodbc.DatabaseError as exception:
            print('Failed to execute query')
            print(exception)
            exit(1)

    def azureAddData(self, name, text):
        sql = "INSERT INTO data2 (product, details) values (?, ?)"
        val = (name, text)
        self.cursor.execute(sql, val)
        self.conn.commit()
