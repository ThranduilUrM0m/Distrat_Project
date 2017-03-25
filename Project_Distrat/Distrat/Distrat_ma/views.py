from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Categorie, Souscategorie, Realisation, Produit, Couleurproduit, Couleur
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


# Create your views here.

def index(request):
    latest_categorie_list = Categorie.objects.order_by('-datederniermodif')
    latest_souscategorie_list = Souscategorie.objects.order_by('-datedernmodif')
    context = {
        'latest_categorie_list': latest_categorie_list,
        'latest_souscategorie_list': latest_souscategorie_list,
    }
    return render(request, 'Distrat_ma/index.html', context)


def about_us(request):
    latest_categorie_list = Categorie.objects.order_by('-datederniermodif')
    latest_souscategorie_list = Souscategorie.objects.order_by('-datedernmodif')
    context = {
        'latest_categorie_list': latest_categorie_list,
        'latest_souscategorie_list': latest_souscategorie_list,
    }
    return render(request, 'Distrat_ma/about_us.html', context)


def products(request):
    latest_categorie_list = Categorie.objects.order_by('-datederniermodif')
    latest_souscategorie_list = Souscategorie.objects.order_by('-datedernmodif')
    context = {
        'latest_categorie_list': latest_categorie_list,
        'latest_souscategorie_list': latest_souscategorie_list,
    }
    return render(request, 'Distrat_ma/products.html', context)


def samples(request):
    latest_samples_list = Realisation.objects.order_by('-daterealisation')
    latest_categorie_list = Categorie.objects.order_by('-datederniermodif')
    latest_souscategorie_list = Souscategorie.objects.order_by('-datedernmodif')

    paginator = Paginator(latest_samples_list, 4)
    page = request.GET.get('page')
    try:
        realisations = paginator.page(page)
    except Categorie.DoesNotExist:
        raise Http404("Question does not exist")
    except PageNotAnInteger:
        realisations = paginator.page(1)
    except EmptyPage:
        realisations = paginator.page(paginator.num_pages)
    context = {
        'latest_categorie_list': latest_categorie_list,
        'latest_souscategorie_list': latest_souscategorie_list,
        'latest_samples_list': latest_samples_list,
        'realisations': realisations,
    }
    return render(request, 'Distrat_ma/samples.html', context)


def showrooms(request):
    latest_categorie_list = Categorie.objects.order_by('-datederniermodif')
    latest_souscategorie_list = Souscategorie.objects.order_by('-datedernmodif')
    context = {
        'latest_categorie_list': latest_categorie_list,
        'latest_souscategorie_list': latest_souscategorie_list,
    }
    return render(request, 'Distrat_ma/showrooms.html', context)


def categories(request, categorie_id):
    categorie = Categorie.objects.get(pk=categorie_id)
    latest_categorie_list = Categorie.objects.order_by('-datederniermodif')
    latest_souscategorie_list = Souscategorie.objects.order_by('-datedernmodif')
    souscategorie_list = Souscategorie.objects.filter(categorieid=categorie_id)
    latest_produits_list = Produit.objects.filter(souscategorieid__in=souscategorie_list)

    couleur_produits_list = Couleurproduit.objects.all()
    couleur_list = Couleur.objects.all()

    paginator = Paginator(latest_produits_list, 16)
    page = request.GET.get('page')
    try:
        products = paginator.page(page)
    except Categorie.DoesNotExist:
        raise Http404("Something Went Wrong !")
    except PageNotAnInteger:
        products = paginator.page(1)
    except EmptyPage:
        products = paginator.page(paginator.num_pages)
    context = {
        'latest_categorie_list': latest_categorie_list,
        'latest_souscategorie_list': latest_souscategorie_list,
        'categorie': categorie,
        'latest_produits_list': latest_produits_list,
        'products': products,
        'couleur_produits_list': couleur_produits_list,
        'couleur_list': couleur_list,
    }
    return render(request, 'Distrat_ma/categories.html', context)


def subcategories(request, souscategorie_id):
    souscategorie = Souscategorie.objects.get(pk=souscategorie_id)

    categorie = Categorie.objects.get(pk=souscategorie.categorieid.id)

    latest_categorie_list = Categorie.objects.order_by('-datederniermodif')

    latest_souscategorie_list = Souscategorie.objects.order_by('-datedernmodif')
    c_id = categorie.id
    souscategorie_list = Souscategorie.objects.filter(categorieid=c_id)

    latest_produits_list = Produit.objects.filter(souscategorieid=souscategorie_id)

    paginator = Paginator(latest_produits_list, 16)
    page = request.GET.get('page')
    try:
        products_s = paginator.page(page)
    except Categorie.DoesNotExist:
        raise Http404("Question does not exist")
    except PageNotAnInteger:
        products_s = paginator.page(1)
    except EmptyPage:
        products_s = paginator.page(paginator.num_pages)
    context = {
        'souscategorie': souscategorie,
        'latest_categorie_list': latest_categorie_list,
        'latest_souscategorie_list': latest_souscategorie_list,
        'categorie': categorie,
        'souscategorie_list': souscategorie_list,
        'latest_produits_list': latest_produits_list,
        'products_s': products_s,
    }
    return render(request, 'Distrat_ma/subcategories.html', context)