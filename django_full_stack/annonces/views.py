from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from .models import Annonce, Category
from .forms import Annonce_form , Category_form
from django.contrib import messages
from django.db.models import Prefetch

# Create your views here.
@login_required(login_url='login')
def home_view(request):
    categories = Category.objects.prefetch_related('annonce_set').all()
    return render(request, 'home.html', {'categories': categories})


@login_required(login_url = 'login')
def annonce_en_attente (request) :
    categorys = Category.objects.filter(annonce__status = 'EN ATTENTE').distinct().prefetch_related(Prefetch("annonce_set", queryset=Annonce.objects.filter(status='EN ATTENTE')))
    return render(request, 'annonce_en_attente.html', {"categorys" : categorys})

@login_required(login_url = 'login')
def annonces_valides (request) :
    categorys = Category.objects.filter(annonce__status = 'VALIDE').distinct().prefetch_related(Prefetch("annonce_set", queryset=Annonce.objects.filter(status='VALIDE')))
    return render(request, 'annonce_valides.html', {"categorys" : categorys})

@login_required(login_url = 'login')
def annonce_rejetes (request) :
    categorys = Category.objects.filter(annonce__status = 'REJETE').distinct().prefetch_related(Prefetch("annonce_set", queryset=Annonce.objects.filter(status='REJETE')))
    return render(request, 'annonce_rejetes.html', {"categorys" : categorys})


@login_required(login_url='login')
def details_annonce_view (request, pk) :
    annonnce = Annonce.objects.get(pk = pk)
    is_publisher = annonnce.publisher == request.user
    return render(request, 'details_annonce.html', {"annonce" : annonnce, "is_publisher" : is_publisher})

@login_required(login_url='login')
def annonces_privees(request) :
    annonces = Annonce.objects.filter(publisher = request.user)
    return render(request, 'annonces_privees.html', {"annonces" : annonces})


@login_required(login_url='login')
def ajouter_annonce (request) :
    if request.method == 'GET' :
        form = Annonce_form()
        return render(request, 'ajouter_annonce.html', {'form': form})
    
    else :
        form = Annonce_form(request.POST, request.FILES)
        if form.is_valid() :
            annonce = form.save(commit=False)
            annonce.publisher = request.user
            annonce.save()
            messages.success(request , "Le nouveau annonce ete enregistrer avec succes")
            return redirect('home')
        
        else :
            messages.error(request, "Erreur lors de la creation de l'annonce")
            return render(request, "ajouter_annonce.html", {"form" : form})


@login_required(login_url='login')
def modifier_annonce (request , pk) :
    annonce = Annonce.objects.get(pk = pk)

    if request.method == 'GET' :
        form = Annonce_form(instance=annonce)
        return render(request, 'modifier_annonce.html', {'form': form})
    
    else :
        form = Annonce_form(request.POST, request.FILES, instance=annonce)
        if form.is_valid() :
            annonce = form.save(commit=False)
            annonce.publisher = request.user
            annonce.save()
            messages.success(request , "Le nouveau annonce ete modifier avec succes")
            return redirect('details_annonce', annonce.id)
        
        else :
            messages.error(request, "Erreur lors de la modification de l'annonce")
            return render(request, "modifier_annonce.html", {"form" : form})


@login_required(login_url='login')
def ajouter_category (request) :
    if request.method == 'GET' :
        form = Category_form()
        return render(request, 'ajouter_category.html', {'form' : form})
    
    else :
        form = Category_form(request.POST)
        if form.is_valid() :
            form.save()
            messages.success(request, 'La novelle categorie ete enregistrer avec succes')
            return redirect('home')
        
        messages.error(request, 'Erreur lors de la creation de la categorie')
        return render(request, 'ajouter_category.html', {'form' : form})
    


@login_required(login_url = 'login')
def supprimer_annonce (request, pk) :
    annonce = Annonce.objects.get(pk = pk)
    annonce.delete()
    messages.success(request, "L'annonce ete supprimer avec succes")
    return redirect("home")



@login_required(login_url='login')
def modifier_status (request, pk, new_status) :
    annonce = Annonce.objects.get(pk = pk)
    annonce.status = new_status
    annonce.save()

    messages.success(request,"la status de l'annonce ete modifier avec succes")
    return redirect('details_annonce', annonce.id)