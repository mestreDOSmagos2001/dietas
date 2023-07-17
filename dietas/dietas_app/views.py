from django.shortcuts import render

def index(request):
    return render(request, 'index.html')


from django.shortcuts import render


def processar_formulario(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        sexo = request.POST.get('sexo')
        idade = request.POST.get('idade')
        peso = request.POST.get('peso')
        altura = request.POST.get('altura')
        context = {
            'nome': nome,
            'sexo': sexo,
            'idade': idade,
            'peso': peso,
            'altura': altura,
        }

        # Faça algo com os dados do formulário aqui, como salvar no banco de dados ou realizar cálculos

        # Redirecione para outra página ou renderize um template de confirmação
        return render(request, 'confirmacao.html', context)

    # Se não for uma requisição POST, retorne uma página vazia ou redirecione para outra página
    return render(request, 'vazio.html')




