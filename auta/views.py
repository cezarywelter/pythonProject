from django.shortcuts import render, get_object_or_404, redirect
from .models import Auto
from .forms import AutoForm
from django.contrib.auth.decorators import login_required, permission_required


def wszystkie_auta(request):
    auta=Auto.objects.all()
    context = {'auta': auta}
    return render(request, 'auta/wszystkie.html', context)

def szczegoly_auta(request, auto_id):
    auto = get_object_or_404(Auto, pk=auto_id)
    field_names = [f.name for f in Auto._meta.get_fields()]
    for i,f in enumerate(field_names):
        if f == "oceny":
            field_names[i] = "oceny_set"
        elif f == "aktor":
            field_names[i] = "aktor_set"
    return render(request, 'auta/szczegoly.html', {'auto': auto, 'field_names': field_names})

@login_required
@permission_required
def nowy_auto(request):
    form = AutoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_auta)
    return render(request, 'auta/auto_form.html', {'form': form})

@login_required
@permission_required
def edytuj_auto(request, id):
    auto = get_object_or_404(Auto, pk=id)
    form = AutoForm(request.POST or None, instance=auto)
    if form.is_valid():
        form.save()
        return redirect(wszystkie_auta)
    return render(request, 'auta/auto_form.html', {'form':form})


@login_required
@permission_required('auta.delete_auto')
def usun_auto(request, id):
    auto = get_object_or_404(Auto, pk=id)
    if request.method=="POST":
        auto.delete()
        return redirect(wszystkie_auta)
    return render(request, 'auta/auto_usun.html', {'auto': auto})
