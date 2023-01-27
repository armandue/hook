class HookDataAccess:
    database = "hook_database"

    def execute(self, table: str, queries: [str]):
        print('Generate SQL query to access ' + self.database)
        if len(queries) > 0:
            where_clause = ' AND '.join(queries)
            query = 'SELECT * FROM ' + table + ' WHERE ' + where_clause + ';'
        else:
            query = 'SELECT * FROM ' + table + ';'
        print(query)
