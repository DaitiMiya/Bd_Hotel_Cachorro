from postgreConnection import query, mutation
from pydantic import BaseModel

class Endereco(BaseModel):
    endereco_id: int
    rua: str
    complemento: str
    bairro: str
    cidade: str
    estado: str
    cep: str

def insertEndereco(endereco: Endereco):
    response = mutation(f'INSERT INTO ENDERECO (ENDERECO_ID, RUA, COMPLEMENTO, BAIRRO, CIDADE, ESTADO, CEP) values ({endereco.endereco_id}, \'{endereco.rua}\', \'{endereco.complemento}\', \'{endereco.bairro}\', \'{endereco.cidade}\', \'{endereco.estado}\', \'{endereco.cep}\');')

def listEnderecos():
    enderecos = query("SELECT * FROM ENDERECO;")
    return enderecos

def updateEndereco(endereco: Endereco):
    return mutation(f'UPDATE ENDERECO SET RUA = {endereco.rua}, COMPLEMENTO = {endereco.complemento}, BAIRRO = {endereco.bairro}, CIDADE = {endereco.cidade}, ESTADO = {endereco.estado}, CEP = {endereco.cep} WHERE ENDERECO_ID = {endereco.endereco_id};')

def deleteEndereco(endereco_id: int):
    response = mutation(f'DELETE FROM ENDERECO e WHERE e.ENDERECO_ID = {endereco_id};')
    return response


    