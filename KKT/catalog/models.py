from django.db import models

# Create your models here.

class CatalogModel(models.Model):
    #Fields
    id = models.AutoField(primary_key=True)
    id_kkt = models.IntegerField()
    id_client = models.IntegerField()
    id_ofd = models.IntegerField()
    id_fn = models.IntegerField()

class FnModel(models.Model):
    #Fields
    id = models.AutoField(primary_key=True)
    ffd = models.CharField(max_length=4)
    fh_type = models.CharField(max_length=10)
    fn_z_nom = models.IntegerField(max_length=16)
    fn_status
    fn_data_start
    fn_data_end


class KktModel(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    rmk
    id_client
    id_ofd
    date_reg
    kkt_model
    kkt_z_nom
    id_fn


class OfdModel(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    ofd_inn
    ofd_full_name
    ofd_short_name
    ofd_url
    ofd_set_addres
    ofd_set_port
    ofd_set_email


class ClientsModel(models.Model):
    # Fields
    id = models.AutoField(primary_key=True)
    inn
    ogrn
    ip
    client_full_name
    client_short_name
    director_inn
    predstavitel
    predstavitel_doc
