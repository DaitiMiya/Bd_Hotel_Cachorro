from .Connection import postgree
from pydantic import BaseModel


class Dono(BaseModel):
    dono_id: int
    cpf_cliente: str
    telefone: str
    endereco_id: int  # fk
    nome_cli: str
    sobrenome_cli: str
    telefone_emergencia: str
    data_nascimento: str


def insertDono(dono: Dono):
    print(f'insert \'dono\' {dono}')
    response = postgree.mutation(
        f'INSERT INTO DONO (DONO_ID, CPF_CLIENTE, TELEFONE, ENDERECO_ID, NOME_CLI, SOBRENOME_CLI, TELEFONE_EMERGENCIA, DATA_NASCIMENTO) values ({dono.dono_id}, \'{dono.cpf_cliente}\', \'{dono.telefone}\', \'{dono.endereco_id}\', \'{dono.nome_cli}\', \'{dono.sobrenome_cli}\', \'{dono.telefone_emergencia}\', \'{dono.data_nascimento}\');')


def listDonos():
    print(f'list all \'dono\'')
    donos = postgree.query("SELECT * FROM DONO;")
    return donos


def updateDono(dono: Dono, endereco_id: int):
    print(f'update \'dono\' {dono}')
    return postgree.mutation(
        f'UPDATE DONO SET CPF_CLIENTE = {dono.cpf_cliente}, TELEFONE = {dono.telefone}, ENDERECO_ID = {endereco_id}, NOME_CLI = {dono.nome_cli}, SOBRENOME_CLI = {dono.sobrenome_cli}, TELEFONE_EMERGENCIA = {dono.telefone_emergencia}, DATA_NASCIMENTO = {dono.data_nascimento}  WHERE DONO_ID = {dono.dieta_id};')


def deleteDono(dono_id: int):
    print(f'delete \'dono\' from id {dono_id}')
    response = postgree.mutation(f'DELETE FROM DONO d WHERE d.DONO_ID = {dono_id};')
    return response
