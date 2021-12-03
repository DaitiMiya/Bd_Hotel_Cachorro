from dono import Dono
from dieta import Dieta
from postgreConnection import query, mutation
from pydantic import BaseModel

class Animal(BaseModel):
    animal_id: int 
    dono_id: int #fk
    dieta_id: int #fk
    nome: str
    data_nascimento: str
    condicao_especial: int 

def insertAnimal(animal: Animal):
    response = mutation(f'INSERT INTO ANIMAL (ANIMAL_ID, DONO_ID, DIETA_ID, NOME, DATA_NASCIMENTO, CONDICAO_ESPECIAL) values ({animal.animal_id}, \'{animal.dono_id}\', \'{animal.dieta_id}\', \'{animal.nome}\', \'{animal.data_nascimento}\', \'{animal.condicao_especial}\');')

def listAnimais():
    animais = query("SELECT * FROM ANIMAL;")
    return animais

def updateAnimal(animal: Animal, dono_id: int, dieta_id: int):
    return mutation(f'UPDATE ANIMAL SET DONO_ID = {dono_id}, DIETA_ID = {dieta_id}, NOME = {animal.nome}, DATA_NASCIMENTO = {animal.data_nascimento}, CONDICAO_ESPECIAL = {animal.condicao_especial} WHERE ANIMAL_ID = {animal.animal_id};')

def deleteAnimal(animal_id: int):
    response = mutation(f'DELETE FROM ANIMAL a WHERE a.ANIMAL_ID = {animal_id};')
    return response


    