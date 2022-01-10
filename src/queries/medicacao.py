from .Connection import postgree
from pydantic import BaseModel


class Medicacao(BaseModel):
    med_id: int
    registro_federal: str
    nome: str
    fabricante: str
    circunstancia: str


def insertMedicacao(medicacao: Medicacao):
    print(f'insert \'medicacao\' {medicacao}')
    response = postgree.mutation(
        f'INSERT INTO MEDICACAO (MED_ID, REGISTRO_FEDERAL, NOME, FABRICANTE, CIRCUNSTANCIA) values ({medicacao.med_id}, \'{medicacao.registro_federal}\', \'{medicacao.nome}\', \'{medicacao.fabricante}\', \'{medicacao.circunstancia}\');')


def listMedicacoes():
    print(f'list all \'medicacao\'')
    medicacoes = postgree.query("SELECT * FROM MEDICACAO;")
    return medicacoes


def updateMedicacao(medicacao: Medicacao):
    print(f'update \'medicacao\' {medicacao}')
    return postgree.mutation(
        f'UPDATE MEDICACAO SET REGISTRO_FEDERAL = {medicacao.registro_federal}, NOME = {medicacao.nome}, FABRICANTE = {medicacao.fabricante}, CIRCUNSTANCIA = {medicacao.circunstancia} WHERE MED_ID = {medicacao.med_id};')


def deleteMedicacao(med_id: int):
    print(f'delete medicacao from id {med_id}')
    response = postgree.mutation(f'DELETE FROM MEDICACAO m WHERE m.MED_ID = {med_id};')
    return response
