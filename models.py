import sqlite3
class Schema:
    def __init__(self):
        self.conn = sqlite3.connect('alcstats.db')
        self.create_alcstats_table()
        # Why are we calling user table before to_do table
        # what happens if we swap them?

    def create_alcstats_table(self):
        query = """
        CREATE TABLE IF NOT EXISTS "Alc_stats" (
          id INTEGER PRIMARY KEY,
          Name TEXT,
          ABV REAL,
          Calories INTEGER,
          Amount INTEGER,
          Efficiency REAL
        );
        """

        self.conn.execute(query)

class AlcStatsModel:
    TABLENAME = "Alc_stats"

    def __init__(self):
        self.conn = sqlite3.connect('alcstats.db')
        self.conn.row_factory = sqlite3.Row

    def __del__(self):
        # body of destructor
        self.conn.commit()
        self.conn.close()

    def get_by_id(self, _id):
        where_clause = f"AND id={_id}"
        return self.list_items(where_clause)

    def create(self, params):
        print (params)
        query = f'insert into {self.TABLENAME} ' \
                f'(Name, ABV, Calories, Amount, Efficiency) ' \
                f'values ("{params.get("Name")}","{params.get("ABV")}",' \
                f'"{params.get("Amount")}","{params.get("Efficiency")}")'
        result = self.conn.execute(query)
        return self.get_by_id(result.lastrowid)


    def list_items(self, where_clause=""):
        query = f"SELECT id, Name, ABV, Calories, Amount, Efficiency " \
                f"from {self.TABLENAME}" + where_clause
        print (query)
        result_set = self.conn.execute(query).fetchall()
        result = [{column: row[i]
                  for i, column in enumerate(result_set[0].keys())}
                  for row in result_set]
        return result