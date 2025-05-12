from django.shortcuts import redirect, render, get_object_or_404
from ..entidades import bioimpedancia as bioimpedancia_entidade
from ..forms import bioimpedancia_forms
from ..services import bioimpedancia_service, aluno_service
from ..models import Aluno, Bioimpedancia

#__________________________________________________________________________________________________________________________________________________

def cadastrar_bioimpedancia(request, aluno_id):
    aluno = Aluno.objects.get(id=aluno_id)
    if request.user.is_superuser or aluno.personal == request.user.personal:
        if request.method == "POST":
            form_bioimpedancia = bioimpedancia_forms.BioimpedanciaForm(request.POST)
            if form_bioimpedancia.is_valid():
                data_medicao = form_bioimpedancia.cleaned_data['data_medicao']
                peso = form_bioimpedancia.cleaned_data['peso']
                altura = form_bioimpedancia.cleaned_data['altura']
                pct_gordura = form_bioimpedancia.cleaned_data['pct_gordura']
                cintura = form_bioimpedancia.cleaned_data['cintura']
                peito = form_bioimpedancia.cleaned_data['peito']
                coxa = form_bioimpedancia.cleaned_data['coxa']
                panturrilha = form_bioimpedancia.cleaned_data['panturrilha']
                braco = form_bioimpedancia.cleaned_data['braco']

                bioimpedancia_novo = bioimpedancia_entidade.Bioimpedancia(
                    data_medicao=data_medicao,
                    peso=peso,
                    altura=altura,
                    pct_gordura=pct_gordura,
                    cintura=cintura,
                    peito=peito,
                    coxa=coxa,
                    panturrilha=panturrilha,
                    braco=braco,
                    aluno=aluno
                )

                bioimpedancia_service.cadastrar_bioimpedancia(bioimpedancia_novo)
                return redirect('listar_alunos')
        else:
            form_bioimpedancia = bioimpedancia_forms.BioimpedanciaForm()

        return render(request, 'bioimpedancia/form_bioimpedancia.html', {
            'form_bioimpedancia': form_bioimpedancia
        })
    else:
        return redirect('listar_alunos')

#__________________________________________________________________________________________________________________________________________________

def listar_bioimpedancia(request, aluno_id):
    aluno = aluno_service.listar_aluno_id(aluno_id)
    if aluno.personal == request.user.personal or request.user.is_superuser:
        bioimpedancia = bioimpedancia_service.listar_bioimpedancia(aluno_id)
        return render(
            request,
            'bioimpedancia/lista_bioimpedancia.html',
            {'bioimpedancia': bioimpedancia, 'aluno': aluno}
        )
    else:
        return redirect('listar_alunos')

#__________________________________________________________________________________________________________________________________________________

def remover_bioimpedancia(request, id):
    bioimpedancia = get_object_or_404(Bioimpedancia, id=id)
    if request.user.is_superuser or bioimpedancia.aluno.personal == request.user.personal:
        if request.method == 'POST':
            bioimpedancia_service.remover_bioimpedancia(bioimpedancia)
            return redirect('listar_alunos')
        else:
            return render(request, 'bioimpedancia/confirmar_exclusao_bio.html', {"bioimpedancia": bioimpedancia})
    else:
        return redirect('listar_alunos')
