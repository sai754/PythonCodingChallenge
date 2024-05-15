class PropertyUtil:
    @staticmethod
    def getProperty():
        server_name = "DESKTOP-PR637UP"
        database_name = "OrderManagement"
        
        
        conn_str = (
            f"Driver={{ODBC Driver 17 for SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str
    