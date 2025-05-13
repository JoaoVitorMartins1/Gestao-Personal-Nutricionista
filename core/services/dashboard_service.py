from ..models import Aluno
from ..entidades.plano import Plano as PlanoEntidade

def converter_para_entidade(plano_model):
    return PlanoEntidade(
        aluno=plano_model.aluno,
        valor=plano_model.valor,
        data_inicio=plano_model.data_inicio,
        data_vencimento=plano_model.data_vencimento,
        status=plano_model.status
    )

def gerar_dados_dashboard(personal):
    # Busca os alunos desse personal logado
    alunos = Aluno.objects.filter(personal=personal)
    total_alunos = alunos.count()

    planos_ativos = 0
    planos_vencidos = 0

    for aluno in alunos:
        try:
            plano_model = aluno.plano  # pelo OneToOneField
            plano_entidade = converter_para_entidade(plano_model)

            if plano_entidade.esta_ativo:
                planos_ativos += 1
            else:
                planos_vencidos += 1

        except:
            continue  # se não tiver plano, ignora

    return {
        'total_alunos': total_alunos,
        'planos_ativos': planos_ativos,
        'planos_vencidos': planos_vencidos,
    }
