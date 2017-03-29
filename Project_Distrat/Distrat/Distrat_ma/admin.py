from django.contrib import admin
from .models import Couleur, Produit, Couleurproduit, Realisation, Service, User, Souscategorie, Categorie, Avis

# Register your models here.
admin.site.register(Couleur)
admin.site.register(Produit)
admin.site.register(Couleurproduit)
admin.site.register(Realisation)
admin.site.register(Service)
admin.site.register(User)
admin.site.register(Souscategorie)
admin.site.register(Categorie)
admin.site.register(Avis)