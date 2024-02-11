#-------------- Template Pattern --------------------
import sqlite3
import datetime

# conn = sqlite3.connect("sales.db")

# conn.execute(
#     "CREATE TABLE SALES (salesperson text,"
#     "amt currency, year integer, model text,new boolean)"
# )

# conn.execute(
#     "INSERT INTO SALES values"
#     "('Tim',16000,2010,'Honda Fit','true'),"
#     "('Tim',9000,2006,'Ford Focus','false'),"
#     " ('Gayle', 8000, 2004, 'Dodge Neon', 'false'),"
#     " ('Gayle', 28000, 2009, 'Ford Mustang', 'true'),"
#     " ('Gayle', 50000, 2010, 'Lincoln Navigator', 'true'),"
#     " ('Don', 20000, 2008, 'Toyota Prius', 'false')"
# )

# conn.commit()
# conn.close()

class QueryTemplate:
    def connect(self):
        self.conn = sqlite3.connect("sales.db")

    def construct_query(self):
        raise NotImplementedError()
    
    def do_query(self):
        results = self.conn.execute(self.query)
        self.results = results.fetchall()

    def format_results(self):
        output = []
        for row in self.results:
            row = [str(i) for i in row]
            output.append(",".join(row))
        self.formatted_results = "\n".join(output)

    def output_results(self):
        raise NotImplementedError()
    
    def process_format(self):
        self.connect()
        self.construct_query()
        self.do_query()
        self.format_results()
        self.output_results()


class NewVehicleQuery(QueryTemplate):
    def construct_query(self):
        self.query = "SELECT * FROM SALES WHERE new = 'true'"

    def output_results(self):
        print(self.formatted_results)

class UserGrossQuery(QueryTemplate):
    def construct_query(self):
        self.query = "SELECT salesperson, SUM(amt) FROM SALES GROUP BY salesperson"

    def output_results(self):
        filename = "gross_sales_{0}".format(datetime.datetime.today().strftime("%Y%m%d"))

        with open(filename,"w") as outfile:
            outfile.write(self.formatted_results)

# nv = NewVehicleQuery()
# nv.process_format()

# gross_sales = UserGrossQuery()
# gross_sales.process_format()