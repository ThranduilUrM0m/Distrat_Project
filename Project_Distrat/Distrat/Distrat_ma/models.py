# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Categorie(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=25)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    urlimage = models.CharField(db_column='URlImage', max_length=255)  # Field name made lowercase.
    utilsajouter = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsAjouter',
                                     related_name="%(app_label)s_%(class)s_UtilsAjouter")  # Field name made lowercase.
    dateajout = models.DateTimeField(db_column='DateAjout')  # Field name made lowercase.
    utilsmodif = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsModif', blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_UtilsModif")  # Field name made lowercase.
    datederniermodif = models.DateTimeField(db_column='DateDernierModif', blank=True,
                                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'categorie'
    def __str__(self):
        return self.titre


class Couleur(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=25)  # Field name made lowercase.
    urlimage = models.CharField(db_column='URlImage', max_length=150)  # Field name made lowercase.
    utilsajouter = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsAjouter',
                                     related_name="%(app_label)s_%(class)s_UtilsAjouter")  # Field name made lowercase.
    dateajout = models.DateTimeField(db_column='DateAjout')  # Field name made lowercase.
    utilsmodif = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsModif', blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_UtilsModif")  # Field name made lowercase.
    datederniermodif = models.DateTimeField(db_column='DateDernierModif', blank=True,
                                            null=True)  # Field name made lowercase.

    def __str__(self):
        return self.titre

    class Meta:
        managed = False
        db_table = 'couleur'


class Couleurproduit(models.Model):
    produitid = models.ForeignKey('Produit', models.DO_NOTHING, db_column='ProduitId',
                                  primary_key=True)  # Field name made lowercase.
    couleurid = models.ForeignKey(Couleur, models.DO_NOTHING, db_column='CouleurId',
                                  primary_key=True)  # Field name made lowercase.
    urlimage = models.CharField(db_column='URlImage', max_length=200, blank=True,
                                null=True)  # Field name made lowercase.
    dateajout = models.DateTimeField(db_column='DateAjout')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'couleurproduit'
        unique_together = ('produitid', 'couleurid')
    def __str__(self):
        return self.urlimage


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Produit(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=55)  # Field name made lowercase.
    designation = models.CharField(db_column='Designation', max_length=150)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    disponibilite = models.CharField(db_column='Disponibilite', max_length=3)  # Field name made lowercase.
    prix = models.FloatField(db_column='Prix', blank=True, null=True)  # Field name made lowercase.
    nouveau = models.CharField(db_column='Nouveau', max_length=3)  # Field name made lowercase.
    garantie = models.CharField(db_column='Garantie', max_length=3, blank=True, null=True)  # Field name made lowercase.
    dureegarantie = models.IntegerField(db_column='DureeGarantie', blank=True, null=True)  # Field name made lowercase.
    urlimage = models.CharField(db_column='UrlImage', max_length=255)  # Field name made lowercase.
    souscategorieid = models.ForeignKey('Souscategorie', models.DO_NOTHING,
                                        db_column='SousCategorieId')  # Field name made lowercase.
    utilisajouter = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilisAjouter',
                                      related_name="%(app_label)s_%(class)s_UtilsAjouter")  # Field name made lowercase.
    dateajout = models.DateTimeField(db_column='DateAjout')  # Field name made lowercase.
    utilismodif = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilisModif', blank=True, null=True,
                                    related_name="%(app_label)s_%(class)s_UtilsModif")  # Field name made lowercase.
    datedernmodif = models.DateTimeField(db_column='DateDernModif', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'produit'

    def __str__(self):
        return self.designation


class Realisation(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    reference = models.CharField(db_column='Reference', max_length=10)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=25)  # Field name made lowercase.
    souscategorieid = models.ForeignKey('Souscategorie', models.DO_NOTHING,
                                        db_column='SousCategorieId')  # Field name made lowercase.
    urlimage = models.CharField(db_column='URlImage', max_length=255)  # Field name made lowercase.
    daterealisation = models.DateField(db_column='DateRealisation', blank=True, null=True)  # Field name made lowercase.
    utilsajouter = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsAjouter',
                                     related_name="%(app_label)s_%(class)s_UtilsAjouter")  # Field name made lowercase.
    dateajout = models.DateTimeField(db_column='DateAjout')  # Field name made lowercase.
    utilsmodif = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsModif', blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_UtilsModif")  # Field name made lowercase.
    datederniermodif = models.DateTimeField(db_column='DateDernierModif', blank=True,
                                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'realisation'

    def __str__(self):
        return self.titre


class Service(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=25)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    logoservice = models.CharField(db_column='LogoService', max_length=150)  # Field name made lowercase.
    utilsajouter = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsAjouter',
                                     related_name="%(app_label)s_%(class)s_UtilsAjouter")  # Field name made lowercase.
    dateajout = models.DateTimeField(db_column='DateAjout')  # Field name made lowercase.
    utilsmodif = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsModif', blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_UtilsModif")  # Field name made lowercase.
    datederniermodif = models.DateTimeField(db_column='DateDernierModif', blank=True,
                                            null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'service'

    def __str__(self):
        return self.titre


class Avis(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    f_name = models.CharField(db_column="f_name", max_length=25)
    l_name = models.CharField(db_column="l_name", max_length=25)
    avis_text = models.CharField(db_column="avis_text", max_length=500)
    dt_created = models.DateTimeField(db_column='dt_created')

    class Meta:
        managed = False
        db_table = 'avis'

    def __str__(self):
        return self.avis_text
            

class Souscategorie(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    titre = models.CharField(db_column='Titre', max_length=100)  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    categorieid = models.ForeignKey(Categorie, models.DO_NOTHING, db_column='CategorieId')  # Field name made lowercase.
    utilsajouter = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsAjouter',
                                     related_name="%(app_label)s_%(class)s_UtilsAjouter")  # Field name made lowercase.
    dateajout = models.DateTimeField(db_column='DateAjout')  # Field name made lowercase.
    utilsmodif = models.ForeignKey('User', models.DO_NOTHING, db_column='UtilsModif', blank=True, null=True,
                                   related_name="%(app_label)s_%(class)s_UtilsModif")  # Field name made lowercase.
    datedernmodif = models.DateTimeField(db_column='DateDernModif', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'souscategorie'

    def __str__(self):
        return self.titre


class User(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nom = models.CharField(db_column='Nom', max_length=150)  # Field name made lowercase.
    prenom = models.CharField(db_column='Prenom', max_length=150)  # Field name made lowercase.
    role = models.CharField(max_length=20)
    login = models.CharField(db_column='Login', max_length=255)  # Field name made lowercase.
    password = models.CharField(db_column='Password', max_length=255)  # Field name made lowercase.
    etatcompte = models.CharField(db_column='EtatCompte', max_length=15)  # Field name made lowercase.
    dateajout = models.DateTimeField(db_column='DateAjout')  # Field name made lowercase.
    datedernconx = models.DateTimeField(db_column='DateDernconx', blank=True, null=True)  # Field name made lowercase.
    datedernmodif = models.DateTimeField(db_column='DateDernModif', blank=True, null=True)  # Field name made lowercase.
    utilisateurajouter = models.ForeignKey('self', models.DO_NOTHING, db_column='UtilisateurAjouter', blank=True,
                                           null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'

    def __str__(self):
        return self.nom