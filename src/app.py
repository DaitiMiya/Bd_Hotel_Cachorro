import queries
from typing import Optional
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/{entidade}")
def get_entidade(entidade: str):
    if entidade == 'animal':
        return queries.animal.listAnimais()
    if entidade == 'dieta':
        return queries.dieta.listDietas()
    if entidade == 'dono':
        return queries.dono.listDonos()
    if entidade == 'endereco':
        return queries.endereco.listEnderecos()
    if entidade == 'medicacao':
        return queries.medicacao.listMedicacoes()
    if entidade == 'relacaoMedicamentos':
        return queries.relacaoMedicamentos.listRelacoesMedicamentos()
    raise HTTPException(status_code=404, detail="entidade nao encontrada")


@app.delete('/{entidade}/delete/{item_id}')
def delete_entidade(entidade: str, item_id):
    if entidade == 'animal':
        return queries.animal.deleteAnimal(item_id)
    if entidade == 'dieta':
        return queries.dieta.deleteDieta(item_id)
    if entidade == 'dono':
        return queries.dono.deleteDono(item_id)
    if entidade == 'endereco':
        return queries.endereco.deleteEndereco(item_id)
    if entidade == 'medicacao':
        return queries.medicacao.deleteMedicacao(item_id)
    if entidade == 'relacaoMedicamentos':
        return queries.relacaoMedicamentos.deleteRelacaoMedicamento(item_id)
    raise HTTPException(status_code=404, detail="entidade nao encontrada")


@app.post('insert/animal')
def new_animal(animal: queries.Animal):
    return queries.animal.insertAnimal(animal)


@app.post('insert/dieta')
def new_dieta(dieta: queries.Dieta):
    return queries.dieta.insertDieta(dieta)


@app.post('insert/dono')
def new_dono(dono: queries.Dono):
    return queries.dono.insertDono(dono)


@app.post('insert/endereco')
def new_endereco(endereco: queries.Endereco):
    return queries.endereco.insertEndereco(endereco)


@app.post('insert/medicacao')
def new_medicacao(medicacao: queries.Medicacao):
    return queries.medicacao.insertMedicacao(medicacao)


@app.post('insert/relacaoMedicamentos')
def new_rel(rel: queries.RelacaoMedicamentos):
    return queries.relacaoMedicamentos.insertRelacaoMedicamentos(rel)


@app.put('update/animal/{idAnimal}/{idDono}')
def updateAnimal(animal: queries.Animal, idAnimal, idDono):
    return queries.animal.updateAnimal(animal, idAnimal, idDono)


@app.put('update/dieta')
def updateAnimal(dieta: queries.Dieta):
    return queries.dieta.updateDieta(dieta)


@app.put('update/dono/{endeco_id}')
def updateAnimal(dono: queries.Dono, eneredo_id):
    return queries.dono.updateDono(dono, eneredo_id)


@app.put('update/medicacao')
def updateAnimal(medicacao: queries.Medicacao):
    return queries.medicacao.updateMedicacao(medicacao)


@app.put('update/relacaoMedicamentos/{rel_id}/{med_id}/{animal_id}')
def updateRelacao(rel_id, med_id, animal_id):
    return queries.relacaoMedicamentos.updateRelacaoMedicamentos(rel_id, animal_id, med_id)
