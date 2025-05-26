from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from ..models import Personal

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(is_superuser, login_url='/core/login/') # Redireciona se não for superuser
def listar_profissionais(request):
    """View para listar todos os profissionais (Personal) para o superusuário."""
    profissionais = Personal.objects.select_related('user').all()
    context = {
        'profissionais': profissionais
    }
    return render(request, 'master/listar_profissionais.html', context)

