from ..models import Plano

def cadastrar_plano(plano):
    Plano.objects.create(aluno=plano.aluno,valor=plano.valor,data_inicio=plano.data_inicio,
                         data_vencimento=plano.data_vencimento,status=plano.status)


def listar_plano_id(aluno_id):
    return Plano.objects.get(aluno_id=aluno_id)

def remover_plano(plano):
    plano.delete()

