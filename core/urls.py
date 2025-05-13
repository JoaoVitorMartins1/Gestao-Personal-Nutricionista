from django.urls import path
from .views import aluno_views, bioimpedancia_views, gerar_pdf, plano_views, user_views,dieta_views,dashboard_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('cadastrar_aluno', aluno_views.cadastrar_aluno, name='cadastrar_aluno'),
    path('listar_alunos', aluno_views.listar_alunos, name='listar_alunos'),
    path('listar_aluno/<int:id>', aluno_views.listar_aluno_id, name='listar_aluno'),
    path('editar_aluno/<int:id>', aluno_views.editar_aluno, name='editar_aluno'),
    path('remover_aluno/<int:id>', aluno_views.remover_aluno, name='remover_aluno'),
    # _____________________________________________________________________________________________________________________
    path('cadastrar_bioimpedancia/<int:aluno_id>', bioimpedancia_views.cadastrar_bioimpedancia,
         name='cadastrar_bioimpedancia'),
    path('listar_bioimpedancia/<int:aluno_id>', bioimpedancia_views.listar_bioimpedancia, name='listar_bioimpedancia'),
    path('bioimpedancia/pdf/<int:bio_id>/', gerar_pdf.gerar_pdf_bioimpedancia, name='gerar_pdf_bioimpedancia'),
    path('bioimpedancia/delete/<int:id>/', bioimpedancia_views.remover_bioimpedancia, name='remover_bioimpedancia'),
    # _____________________________________________________________________________________________________________________
    path('cadastrar_plano/<int:aluno_id>', plano_views.cadastrar_plano, name='cadastrar_plano'),
    path('listar_plano/<int:aluno_id>', plano_views.listar_plano_id, name='listar_plano'),
    path('plano/delete/<int:id>/', plano_views.remover_plano, name='remover_plano'),
    # _____________________________________________________________________________________________________________________
    path('cadastrar_dieta/<int:aluno_id>', dieta_views.cadastrar_dieta, name='cadastrar_dieta'),
    path('listar_dieta/<int:aluno_id>', dieta_views.listar_dieta_id, name='listar_dieta'),
    path('editar_dieta/<int:id>', dieta_views.editar_dieta_id, name='editar_dieta'),
    path('dieta/delete/<int:id>/', dieta_views.remover_dieta, name='remover_dieta'),
    path('dieta/pdf/<int:dieta_id>/', gerar_pdf.gerar_pdf_dieta, name='gerar_pdf_dieta'),
    # _____________________________________________________________________________________________________________________
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('usuarios/cadastrar/', user_views.cadastrar_usuario_personal, name='cadastrar_usuario_personal'),
    # _____________________________________________________________________________________________________________________
    path('dashboard/', dashboard_view.dashboard, name='dashboard'),
]

