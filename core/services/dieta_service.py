from ..models import Dieta


def cadastrar_dieta(dieta):
        Dieta.objects.create(aluno=dieta.aluno,descricao=dieta.descricao)

def listar_dieta_id(aluno_id):
        return Dieta.objects.filter(aluno_id=aluno_id)

def editar_dieta_id(dieta,dieta_novo):
        dieta.descricao=dieta_novo.descricao
        dieta.save (force_update=True)


def remover_dieta(dieta):
        dieta.delete()