from django.http import HttpResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from django.shortcuts import get_object_or_404
from ..models import Dieta, Bioimpedancia

# Função para gerar PDF da Bioimpedância
def gerar_pdf_bioimpedancia(request, bio_id):
    bio = get_object_or_404(Bioimpedancia, id=bio_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="bioimpedancia_{bio.aluno.nome}_{bio.data_medicao}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)

    p.setFont("Helvetica-Bold", 20)
    p.drawString(1 * inch, 10 * inch, f"Relatório de Bioimpedância - {bio.aluno.nome}")
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 9.5 * inch, f"Data da Avaliação: {bio.data_medicao.strftime('%d/%m/%Y')}")

    y = 8.5 * inch
    p.setFont("Helvetica-Bold", 12)
    p.drawString(1 * inch, y, "Dados Antropométricos:")
    p.setFont("Helvetica", 12)

    dados = [
        ("Peso:", f"{bio.peso} kg"),
        ("Altura:", f"{bio.altura} m"),
        ("PGC %:", f"{bio.pct_gordura}%"),
        ("Cintura:", f"{bio.cintura} cm"),
        ("Peito:", f"{bio.peito} cm"),
        ("Coxa:", f"{bio.coxa} cm"),
        ("Panturrilha:", f"{bio.panturrilha} cm"),
        ("Braço:", f"{bio.braco} cm")
    ]

    for label, value in dados:
        y -= 0.4 * inch
        p.drawString(1.5 * inch, y, label)
        p.drawString(3 * inch, y, value)

    p.showPage()
    p.save()

    return response

# Função para gerar PDF da Dieta
def gerar_pdf_dieta(request, dieta_id):
    dieta = get_object_or_404(Dieta, id=dieta_id)

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="dieta_{dieta.aluno.nome}_{dieta.data_criacao}.pdf"'

    p = canvas.Canvas(response, pagesize=letter)

    p.setFont("Helvetica-Bold", 20)
    p.drawString(1 * inch, 10 * inch, f"Plano Alimentar - {dieta.aluno.nome}")

    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, 9.5 * inch, f"Data da Criação: {dieta.data_criacao.strftime('%d/%m/%Y')}")

    y = 8.5 * inch
    p.setFont("Helvetica", 12)
    p.drawString(1 * inch, y, "Descrição da Dieta:")

    textobject = p.beginText()
    textobject.setTextOrigin(1 * inch, y - 0.5 * inch)
    textobject.setFont("Helvetica", 12)
    for line in dieta.descricao.splitlines():
        textobject.textLine(line)
    p.drawText(textobject)

    p.showPage()
    p.save()

    return response
