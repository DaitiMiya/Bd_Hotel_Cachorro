from postgreConnection import query, mutation
from pydantic import BaseModel

class Dieta(BaseModel):
    dieta_id: int
    comida: str
    frequencia: str
    restricoes: str

def insertDieta(dieta: Dieta):
    response = mutation(f'INSERT INTO DIETA (DIETA_ID, COMIDA, FREQUENCIA, RESTRICOES) values ({dieta.dieta_id}, \'{dieta.comida}\', \'{dieta.frequencia}\', \'{dieta.restricoes}\');')

def listDietas():
    dietas = query("SELECT * FROM DIETA;")
    return dietas

def updateDieta(dieta: Dieta):
    return mutation(f'UPDATE DIETA SET COMIDA = {dieta.comida}, FREQUENCIA = {dieta.frequencia}, RESTRICOES = {dieta.restricoes} WHERE DIETA_ID = {dieta.dieta_id};')

def deleteDieta(dieta_id: int):
    response = mutation(f'DELETE FROM DIETA d WHERE d.DIETA_ID = {dieta_id};')
    return response


    