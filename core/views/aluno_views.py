from django.contrib.auth.decorators import login_required
from ..entidades import aluno as aluno_entidade
from ..forms import aluno_forms
from ..services import aluno_service
from django.shortcuts import redirect, render

#__________________________________________________________________________________________________________________________________________________

@login_required
def cadastrar_aluno(request):
    if request.method == 'POST':
        form_aluno = aluno_forms.AlunoForm(request.POST)
        if form_aluno.is_valid():
            nome = form_aluno.cleaned_data['nome']
            email = form_aluno.cleaned_data['email']
            data_nascimento = form_aluno.cleaned_data['data_nascimento']
            telefone = form_aluno.cleaned_data['telefone']
            personal = request.user.personal  # Vincula ao personal logado
            aluno_novo = aluno_entidade.Aluno(
                nome=nome,
                email=email,
                data_nascimento=data_nascimento,
                telefone=telefone,
            )

            aluno_service.cadastrar_aluno(aluno_novo, request.user.personal.user_id)
            return redirect('listar_alunos')

    else:
        form_aluno = aluno_forms.AlunoForm()

    return render(request, 'alunos/form_aluno.html', {'form_aluno': form_aluno})

#__________________________________________________________________________________________________________________________________________________

@login_required
def listar_alunos(request):
    if request.user.is_superuser:
        alunos = aluno_service.listar_alunos(request)
    else:
        alunos = aluno_service.listar_alunos(request.user.personal)

    return render(request, 'alunos/lista_alunos.html', {'alunos': alunos})

#__________________________________________________________________________________________________________________________________________________

@login_required
def listar_aluno_id(request, id):
    aluno = aluno_service.listar_aluno_id(id)
    if request.user.is_superuser or aluno.personal == request.user.personal:
        return render(request, 'alunos/lista_aluno.html', {'aluno': aluno})
    else:
        return redirect('listar_alunos')

#__________________________________________________________________________________________________________________________________________________

@login_required
def editar_aluno(request, id):
    aluno_editar = aluno_service.listar_aluno_id(id)
    if request.user.is_superuser or aluno_editar.personal == request.user.personal:
        form_aluno = aluno_forms.AlunoForm(request.POST or None, instance=aluno_editar)
        if form_aluno.is_valid():
            nome = form_aluno.cleaned_data['nome']
            email = form_aluno.cleaned_data['email']
            data_nascimento = form_aluno.cleaned_data['data_nascimento']
            telefone = form_aluno.cleaned_data['telefone']
            personal = request.user.personal  # Vincula ao personal logado
            aluno_novo = aluno_entidade.Aluno(
                nome=nome,
                email=email,
                data_nascimento=data_nascimento,
                telefone=telefone,
            )
            aluno_service.editar_aluno(aluno_editar, aluno_novo)
            return redirect('listar_alunos')
        else:
            form_aluno = aluno_forms.AlunoForm()

        return render(request, 'alunos/form_aluno.html', {'form_aluno': form_aluno})
    else:
        return redirect('listar_alunos')

#__________________________________________________________________________________________________________________________________________________

@login_required
def remover_aluno(request, id):
    aluno = aluno_service.listar_aluno_id(id)
    if request.user.is_superuser or aluno.personal == request.user.personal:
        if request.method == 'POST':
            aluno_service.remover_aluno(aluno)
            return redirect('listar_alunos')
        else:
            return render(request, 'alunos/confirma_exclusao.html', {'aluno': aluno})
    else:
        return redirect('listar_alunos')
