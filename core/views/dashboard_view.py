from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from ..services.dashboard_service import gerar_dados_dashboard

@login_required
def dashboard(request):
    personal = request.user.personal
    dados = gerar_dados_dashboard(personal)

    return render(request, 'dashboard.html', dados)