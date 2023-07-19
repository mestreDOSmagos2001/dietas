from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout

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

    a
    return render(request, 'vazio.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            return redirect('index') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')



