from ..models import Bioimpedancia

def cadastrar_bioimpedancia(bioimpedancia,):
    Bioimpedancia.objects.create(data_medicao=bioimpedancia.data_medicao,peso=bioimpedancia.peso,
                                 altura=bioimpedancia.altura,pct_gordura=bioimpedancia.pct_gordura,
                                 cintura=bioimpedancia.cintura,peito=bioimpedancia.peito,
                                 coxa=bioimpedancia.coxa,panturrilha=bioimpedancia.panturrilha,braco=bioimpedancia.braco,
                                 aluno=bioimpedancia.aluno)


def listar_bioimpedancia(aluno_id):
    return Bioimpedancia.objects.filter(aluno_id=aluno_id)


def editar_bioimpedancia(bioimpedancia,bioimpedancia_novo):
    bioimpedancia.data_medicao=bioimpedancia_novo.data_medicao
    bioimpedancia.peso=bioimpedancia_novo.peso
    bioimpedancia.altura=bioimpedancia_novo.altura
    bioimpedancia.pct_gordura=bioimpedancia_novo.pct_gordura
    bioimpedancia.cintura=bioimpedancia_novo.cintura
    bioimpedancia.peito=bioimpedancia_novo.peito
    bioimpedancia.coxa=bioimpedancia_novo.coxa
    bioimpedancia.panturrilha=bioimpedancia_novo.panturrilha
    bioimpedancia.braco=bioimpedancia_novo.braco
    bioimpedancia.save(force_update=True)


def remover_bioimpedancia(bioimpedancia):
    bioimpedancia.delete()