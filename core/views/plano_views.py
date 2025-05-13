from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required

from ..models import Aluno, Plano
from ..forms import plano_forms
from ..services import plano_service, aluno_service
from ..entidades import plano as plano_entidade

#__________________________________________________________________________________________________________________________________________________

@login_required
def cadastrar_plano(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if request.user.is_superuser or aluno.personal.user == request.user:
        if request.method == 'POST':
            form_plano = plano_forms.PlanoForm(request.POST)
            if form_plano.is_valid():
                # Verifica se já existe plano para esse aluno
                if hasattr(aluno, 'plano'):
                    mensagem_erro = "Este cliente já tem um plano cadastrado. Exclua esse plano para adicionar outro."
                    return render(request, 'plano/form_plano.html', {
                        'form_plano': form_plano,
                        'aluno': aluno,
                        'mensagem_erro': mensagem_erro
                    })

                valor = form_plano.cleaned_data['valor']
                data_inicio = form_plano.cleaned_data['data_inicio']
                data_vencimento = form_plano.cleaned_data['data_vencimento']
                status = form_plano.cleaned_data['status']

                plano_novo = plano_entidade.Plano(
                    valor=valor,
                    data_inicio=data_inicio,
                    data_vencimento=data_vencimento,
                    status=status,
                    aluno=aluno
                )

                plano_service.cadastrar_plano(plano_novo)
                return redirect('listar_plano', aluno_id=aluno.id)
        else:
            form_plano = plano_forms.PlanoForm()

        return render(request, 'plano/form_plano.html', {
            'form_plano': form_plano,
            'aluno': aluno
        })

    return redirect('listar_alunos')


#__________________________________________________________________________________________________________________________________________________

@login_required
def listar_plano_id(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if request.user.is_superuser or aluno.personal.user == request.user:
        plano = plano_service.listar_plano_id(aluno_id)
        return render(request, 'plano/lista_plano.html', {'plano': plano, 'aluno': aluno})

    return redirect('listar_alunos')

#__________________________________________________________________________________________________________________________________________________

@login_required
def remover_plano(request, id):
    plano_obj = get_object_or_404(Plano, id=id)
    aluno = plano_obj.aluno

    if request.user.is_superuser or aluno.personal.user == request.user:
        if request.method == 'POST':
            plano_service.remover_plano(plano_obj)
            return redirect('listar_alunos')
        else:
            return render(request, 'plano/confirmar_exclusao_plano.html', {"plano": plano_obj})

    return redirect('listar_alunos')

#__________________________________________________________________________________________________________________________________________________
