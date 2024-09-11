from django.conf import settings
from django.shortcuts import redirect, render, get_object_or_404
from .models import Victim, Rescuer, Guest
from .forms import VictimForm, RescuerForm, GuestForm

def victim_list(request):
    victims = Victim.objects.all()
    return render(request, 'rescue/victim_list.html', {'victims': victims})

def rescuer_list(request):
    rescuers = Rescuer.objects.all()
    return render(request, 'rescue/rescuer_list.html', {'rescuers': rescuers})

def victim_detail(request, victim_id):
    victim = get_object_or_404(Victim, pk=victim_id)
    return render(request, 'rescue/victim_detail.html', {'victim': victim})

def update_victim(request, victim_id):
    victim = get_object_or_404(Victim, pk=victim_id)
    if request.method == 'POST':
        form = VictimForm(request.POST, instance=victim)
        if form.is_valid():
            form.save()
            return redirect('victim_list')
    else:
        form = VictimForm(instance=victim)
    return render(request, 'rescue/update_victim.html', {'form': form})

def home(request):
    print(settings.TEMPLATES[0]['DIRS'])  
    return render(request, 'rescue/home.html')

def guest_help(request):
    if request.method == 'POST':
        form = GuestForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = GuestForm()
    return render(request, 'rescue/guest_help.html', {'form': form})

# CRUD for Victims
def victim_list(request):
    victims = Victim.objects.all()
    return render(request, 'rescue/victim_list.html', {'victims': victims})

def victim_detail(request, victim_id):
    victim = get_object_or_404(Victim, pk=victim_id)
    return render(request, 'rescue/victim_detail.html', {'victim': victim})

def add_victim(request):
    if request.method == 'POST':
        form = VictimForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('victim_list')
    else:
        form = VictimForm()
    return render(request, 'rescue/victim_form.html', {'form': form, 'title': 'Add Victim'})

def update_victim(request, victim_id):
    victim = get_object_or_404(Victim, pk=victim_id)
    if request.method == 'POST':
        form = VictimForm(request.POST, instance=victim)
        if form.is_valid():
            form.save()
            return redirect('victim_list')
    else:
        form = VictimForm(instance=victim)
    return render(request, 'rescue/victim_form.html', {'form': form, 'title': 'Update Victim'})

def delete_victim(request, victim_id):
    victim = get_object_or_404(Victim, pk=victim_id)
    if request.method == 'POST':
        victim.delete()
        return redirect('victim_list')
    return render(request, 'rescue/victim_confirm_delete.html', {'victim': victim})

# CRUD for Rescuers
def rescuer_list(request):
    rescuers = Rescuer.objects.all()
    return render(request, 'rescue/rescuer_list.html', {'rescuers': rescuers})

def rescuer_detail(request, rescuer_id):
    rescuer = get_object_or_404(Rescuer, pk=rescuer_id)
    return render(request, 'rescue/rescuer_detail.html', {'rescuer': rescuer})

def add_rescuer(request):
    if request.method == 'POST':
        form = RescuerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rescuer_list')
    else:
        form = RescuerForm()
    return render(request, 'rescue/rescuer_form.html', {'form': form, 'title': 'Add Rescuer'})

def update_rescuer(request, rescuer_id):
    rescuer = get_object_or_404(Rescuer, pk=rescuer_id)
    if request.method == 'POST':
        form = RescuerForm(request.POST, instance=rescuer)
        if form.is_valid():
            form.save()
            return redirect('rescuer_list')
    else:
        form = RescuerForm(instance=rescuer)
    return render(request, 'rescue/rescuer_form.html', {'form': form, 'title': 'Update Rescuer'})

def delete_rescuer(request, rescuer_id):
    rescuer = get_object_or_404(Rescuer, pk=rescuer_id)
    if request.method == 'POST':
        rescuer.delete()
        return redirect('rescuer_list')
    return render(request, 'rescue/rescuer_confirm_delete.html', {'rescuer': rescuer})