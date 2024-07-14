from django.shortcuts import render
from public.models import Public, Category
from public.forms import PublicForm

def publics(request):
    publics = Public.objects.all()
    return render(request, 'public_list.html', {'publics': publics, })

def public_detail(request, public_id: int):
    public = Public.objects.filter(pk=public_id).first()
    return render(request, 'public_detail.html', {'public':public})

def public_form(request):
    if request.method == 'POST':
        form = PublicForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=PublicForm
    
    return render(request, 'public_form.html', {'form':form})