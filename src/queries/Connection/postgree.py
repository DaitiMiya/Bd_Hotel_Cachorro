import psycopg2
from psycopg2.extras import RealDictCursor

from .constants import constants


class postgree:

    def __init__(self):
        cons = constants()
        self.connection = psycopg2.connect(host=cons.HOST, database=cons.database,
                                           user=cons.user, password=cons.password)
        self.cursor = self.connection.cursor(cursor_factory=RealDictCursor)

    def mutation(self, sql):
        try:
            self.cursor.execute(sql)
            self.connection.commit()
            print("Mutation realizada com sucesso")
            return
        except Exception as e:
            raise Exception("Erro na mutation: " + str(e))

    def query(self, sql):
        try:
            self.cursor.execute(sql)
            response = self.cursor.fetchall()
            print("Query realizada com sucesso")
            return response
        except Exception as e:
            raise Exception("Erro na query: " + str(e))
