from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from .forms import PacienteForm, AlimentoForm, DietasForm
from .models import Paciente, Alimento,Medida,Dietas,Refeicao
from django.contrib import messages
from django.db.models import  Q
from django.shortcuts import render
from django.utils.dateparse import parse_date


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

       
        return render(request, 'confirmacao.html', context)

    
    return render(request, 'vazio.html')


def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            
            return redirect('painel') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout(request):
    logout(request)
    return redirect('login')


def cadastro(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)  
        if form.is_valid():
            form.save()
            messages.success(request, 'Cadastro realizado com sucesso!')
            return redirect('cadastro')
        else:
            messages.error(request, 'Erro ao cadastrar!')
    else:
        form = PacienteForm()
        
    
    return render(request, 'cadastro_paciente.html', {'form': form})


def painel(request):
    pacientes = Paciente.objects.all()
    context={
        'pacientes': pacientes
    }
    return render(request, 'painel.html',context)



def paciente(request, pk):
    paciente_form = Paciente.objects.get(id=pk)
    paciente = Paciente.objects.get(id=pk)
    data_especifica = None  # Defina um valor padrão para data_especifica

    if request.method == 'POST':
        data_especifica = request.POST.get('data_especifica')
        
        # Validação da data
        try:
            data_especifica = parse_date(data_especifica)
        except:
            data_especifica = None

        form = DietasForm(request.POST)
        
        if form.is_valid():
            form.instance.paciente = paciente
            form.save()
            return redirect('paciente', pk=pk) 
    else:
        form = DietasForm(initial={'paciente': paciente})
    
    cafe_manha = Dietas.objects.filter(Q(refeicoes__refeicoes__icontains='café da manha') & Q(paciente__nome=paciente_form.nome) & Q(criado__exact=data_especifica))
    almoco = Dietas.objects.filter(Q(refeicoes__refeicoes__icontains='almoço') & Q(paciente__nome=paciente_form.nome) & Q(criado__exact=data_especifica))

    total_proteina_cafe_manha = sum(d.alimento.proteina * d.quantidade for d in cafe_manha)
    total_proteina_cafe_manha = round(total_proteina_cafe_manha, 3) 

    total_proteina_almoco = sum(d.alimento.proteina * d.quantidade for d in almoco)
    total_proteina_almoco = round(total_proteina_almoco, 3) 

    total_proteina = total_proteina_cafe_manha + total_proteina_almoco
    
    context = {
        'paciente_form': paciente_form,
        'cafe_manha': cafe_manha,
        'almoco': almoco,
        'total_proteina': total_proteina,
        'form': form,
        'paciente': paciente,
    }
    return render(request, 'paciente.html', context)




def dieta(request, pk):
    paciente = Paciente.objects.get(id=pk)
    
    if request.method == 'POST':
        form = DietasForm(request.POST)
        
        if form.is_valid():
            form.instance.paciente = paciente 
            form.save()
            return redirect('paciente', pk=pk) 
    else:
        form = DietasForm(initial={'paciente': paciente})  
    return render(request, 'dieta.html', {'form': form})



