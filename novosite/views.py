from django.shortcuts import render,redirect
from novosite.forms import SmatphoneForm
from novosite.models import Smatphone

def home(request):
    data = {}
    data['db'] = Smatphone.objects.all()
    return render(request, 'index.html',data)

def form(request):
    data = {}
    data['formu'] = SmatphoneForm()
    return render(request, 'form.html', data)

def create(request):
    form = SmatphoneForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')

def view(request, pk):
    data = {}
    data['db'] = Smatphone.objects.get(pk=pk)
    return render(request, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db'] = Smatphone.objects.get(pk=pk)
    data['formu'] = SmatphoneForm(instance=data['db'])
    return render(request,'form.html',data)

def update(request, pk):
    data = {}
    data['db'] = Smatphone.objects.get(pk=pk)
    form = SmatphoneForm(request.POST or None, instance=data['db'])
    if form.is_valid():
        form.save()
        return redirect('home')

def delete(request, pk):
    db = Smatphone.objects.get(pk=pk)
    db.delete()
    return redirect('home')