from..models import Aluno

def cadastrar_aluno(aluno,personal_id):
    Aluno.objects.create( nome=aluno.nome,
                         data_nascimento=aluno.data_nascimento, telefone=aluno.telefone,
                         email=aluno.email,
                         personal_id = personal_id,)# Recebe o ID direto (não precisa do objeto completo))


def listar_alunos(request):
    return Aluno.objects.filter(personal=request.user.personal.id)

def listar_aluno_id(id):
    return Aluno.objects.get(id=id)

def editar_aluno(aluno,aluno_novo):
    aluno.nome=aluno_novo.nome
    aluno.data_nascimento=aluno_novo.data_nascimento
    aluno.telefone=aluno_novo.telefone
    aluno.email=aluno_novo.email
    aluno.save (force_update=True)


def remover_aluno(aluno):
    aluno.delete()

