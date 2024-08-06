from .forms import TareaForm, SubTareaForm
from .models import Tarea, SubTarea
from django.contrib import messages
from django.shortcuts import render, HttpResponseRedirect, get_object_or_404

# Create your views here.

def index(request):
        if request.method =='POST':                 
            form = TareaForm(request.POST)          

            if form.is_valid():
                    contact_form = Tarea.objects.create(**form.cleaned_data)
                    messages.success(request, "Los datos han sido guardados!")
                    return HttpResponseRedirect('/listado')
            
            else:
                    messages.error(request, "No se ha podido guardar la informacion!")
                    return HttpResponseRedirect('/')

        else:
            form = TareaForm()
    
        return render(request, 'index.html', {'form': form})

def subtarea(request):
        if request.method =='POST':                         
            form = SubTareaForm(request.POST)
            
            if form.is_valid():
                    contact_form = SubTarea.objects.create(**form.cleaned_data)
                    messages.success(request, "Los datos han sido guardados!")
                    return HttpResponseRedirect('/listado')
            else:
                    messages.error(request, "No se ha podido guardar la informacion!")
                    return HttpResponseRedirect('/subtarea')

        else:
            form = SubTareaForm()
    
        return render(request, 'subtarea.html', {'form': form})

def listado(request):
        tarea = Tarea.objects.all()  
        subtarea = SubTarea.objects.all()          
        return render(request, 'listado.html', {'tarea': tarea, 'subtarea': subtarea})    

def eliminar_tarea(request, id):
    tarea = get_object_or_404(Tarea, id=id)
    tarea.delete()
    messages.success(request, "Tarea eliminada con éxito.")
    return HttpResponseRedirect('/listado')

def eliminar_subtarea(request, id):
    subtarea = get_object_or_404(SubTarea, id=id)
    subtarea.delete()
    messages.success(request, "Subtarea eliminada con éxito.")
    return HttpResponseRedirect('/listado')

def modificar_tarea(request, id):
    if request.method == 'POST':
        tarea = get_object_or_404(Tarea, id=id)
        tarea.eliminada = not tarea.eliminada  # Cambia el estado entre True y False
        tarea.save()
        return HttpResponseRedirect('/listado')
    else:
        return HttpResponseRedirect('/listado')

def modificar_subtarea(request, id):
    if request.method == 'POST':
        subtarea = get_object_or_404(SubTarea, id=id)
        subtarea.eliminada = not subtarea.eliminada  # Cambia el estado entre True y False
        subtarea.save()
        return HttpResponseRedirect('/listado')
    else:
        return HttpResponseRedirect('/listado')
