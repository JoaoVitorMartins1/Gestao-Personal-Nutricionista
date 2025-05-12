from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from ..forms.user_forms import UsuarioPersonalForm
from ..models import Personal

@login_required
def cadastrar_usuario_personal(request):
    if not request.user.is_superuser:
        return redirect('listar_alunos')  # ou outra página de acesso negado

    if request.method == 'POST':
        form = UsuarioPersonalForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_personal = True  # define como personal
            user.save()

            # Cria o perfil de Personal vinculado
            Personal.objects.create(user=user, nome=user.username, telefone='')

            return redirect('listar_alunos')  # redireciona após cadastro
    else:
        form = UsuarioPersonalForm()

    return render(request, 'usuarios/cadastrar_usuario_personal.html', {'form': form})
