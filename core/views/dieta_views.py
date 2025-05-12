from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import dieta_forms
from ..models import Aluno, Dieta
from ..entidades import dieta as dieta_entidade
from ..services import dieta_service, aluno_service

#__________________________________________________________________________________________________________________________________________________

@login_required
def cadastrar_dieta(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if request.user.is_superuser or aluno.personal.user == request.user:
        if request.method == 'POST':
            form_dieta = dieta_forms.DietaForm(request.POST)
            if form_dieta.is_valid():
                descricao = form_dieta.cleaned_data["descricao"]
                dieta_novo = dieta_entidade.Dieta(descricao=descricao, aluno=aluno)
                dieta_service.cadastrar_dieta(dieta_novo)
                return redirect("listar_dieta", aluno_id=aluno.id)
        else:
            form_dieta = dieta_forms.DietaForm()
        return render(request, "dieta/form_dieta.html", {"form_dieta": form_dieta})

    return redirect("listar_alunos")

#__________________________________________________________________________________________________________________________________________________

@login_required
def listar_dieta_id(request, aluno_id):
    aluno = get_object_or_404(Aluno, id=aluno_id)

    if request.user.is_superuser or aluno.personal.user == request.user:
        dieta = dieta_service.listar_dieta_id(aluno_id)
        return render(request, 'dieta/lista_dieta.html', {'dieta': dieta, 'aluno': aluno})

    return redirect("listar_alunos")

#__________________________________________________________________________________________________________________________________________________

@login_required
def editar_dieta_id(request, id):
    dieta_obj = get_object_or_404(Dieta, id=id)
    aluno = dieta_obj.aluno

    if request.user.is_superuser or aluno.personal.user == request.user:
        if request.method == 'POST':
            form_dieta = dieta_forms.DietaForm(request.POST, instance=dieta_obj)
            if form_dieta.is_valid():
                descricao = form_dieta.cleaned_data['descricao']
                dieta_novo = dieta_entidade.Dieta(descricao=descricao, aluno=aluno)
                dieta_service.editar_dieta_id(dieta_obj, dieta_novo)
                return redirect("listar_dieta", aluno_id=aluno.id)
        else:
            form_dieta = dieta_forms.DietaForm(instance=dieta_obj)
        return render(request, 'dieta/form_dieta.html', {"form_dieta": form_dieta})

    return redirect("listar_alunos")

#__________________________________________________________________________________________________________________________________________________

@login_required
def remover_dieta(request, id):
    dieta_obj = get_object_or_404(Dieta, id=id)
    aluno = dieta_obj.aluno

    if request.user.is_superuser or aluno.personal.user == request.user:
        if request.method == 'POST':
            dieta_service.remover_dieta(dieta_obj)
            return redirect('listar_alunos')
        else:
            return render(request, 'dieta/confirmar_exclusao_dieta.html', {"dieta": dieta_obj})

    return redirect("listar_alunos")
