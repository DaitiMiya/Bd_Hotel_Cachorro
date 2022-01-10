from .Connection import postgree
from pydantic import BaseModel


class RelacaoMedicamentos(BaseModel):
    rel_id: int
    animal_id: int  # fk
    med_id: int  # fk


def insertRelacaoMedicamentos(relacaoMedicamentos: RelacaoMedicamentos):
    print(f'insert \'relacao\' {relacaoMedicamentos}')
    response = postgree.mutation(
        f'INSERT INTO MEDICAMENTO_PET (REL_ID, ANIMAL_ID, MED_ID) values ({relacaoMedicamentos.rel_id}, \'{relacaoMedicamentos.animal_id}\', \'{relacaoMedicamentos.med_id}\');')


def listRelacoesMedicamentos():
    print(f'list all  \'relacao\'')
    rel = postgree.query("SELECT * FROM MEDICAMENTO_PET;")
    return rel


def updateRelacaoMedicamentos(rel_id: int, animal_id: int, med_id: int):
    print(f'update \'relacao\' from id {rel_id}')
    return postgree.mutation(
        f'UPDATE MEDICAMENTO_PET SET ANIMAL_ID = {animal_id}, MED_ID = {med_id} WHERE REL_ID = {rel_id};')


def deleteRelacaoMedicamento(rel_id: int):
    print(f'delete \'relacao\' from id {rel_id}')
    response = postgree.mutation(f'DELETE FROM MEDICAMENTO_PET m WHERE m.REL_ID = {rel_id};')
    return response
