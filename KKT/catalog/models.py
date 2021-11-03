from django.db import models

# Create your models here.


class FnModel(models.Model):
    #Fields
    ffd = models.CharField(max_length=4)
    fh_type = models.CharField(max_length=10)
    fn_z_nom = models.IntegerField(max_length=16)
    fn_status = models.BooleanField(default=True)
    fn_data_start = models.DateField(auto_now_add=True)
    fn_data_end = models.DateField(default=None)


class OfdModel(models.Model):
    # Fields
    ofd_inn = models.CharField(max_length=12)
    ofd_full_name = models.CharField(max_length=250)
    ofd_short_name = models.CharField(max_length=150)
    ofd_url = models.CharField(max_length=50)
    ofd_set_address = models.CharField(max_length=50)
    ofd_set_port = models.CharField(max_length=6)
    ofd_set_email = models.CharField(max_length=50)


class ClientsModel(models.Model):
    # Fields
    client_inn = models.CharField(max_length=12)
    client_ogrn = models.CharField(max_length=16)
    ip = models.BooleanField(default=True)
    client_full_name = models.CharField(max_length=250)
    client_short_name = models.CharField(max_length=150)
    director_inn = models.CharField(max_length=12)
    agent = models.CharField(max_length=150)
    agent_doc = models.CharField(max_length=150)
    kkt_address = models.CharField(max_length=350)
    kkt_place = models.CharField(max_length=100)


class KktModel(models.Model):
    # Fields
    rmk = models.CharField(max_length=16)
    id_client = models.ForeignKey(ClientsModel, on_delete=models.PROTECT)
    id_ofd = models.ForeignKey(OfdModel, on_delete=models.PROTECT)
    date_reg = models.DateField(auto_now_add=True)
    kkt_model = models.CharField(max_length=150)
    kkt_z_nom = models.CharField(max_length=150)
    id_fn = models.ForeignKey(FnModel, on_delete=models.PROTECT)


class CatalogModel(models.Model):
    #Fields
    id_kkt = models.ForeignKey(KktModel, on_delete=models.PROTECT)
    id_client = models.ForeignKey(ClientsModel, on_delete=models.PROTECT)
    id_ofd = models.ForeignKey(OfdModel, on_delete=models.PROTECT)
    id_fn = models.ForeignKey(FnModel, on_delete=models.PROTECT)
    date = models.DateField(auto_now_add=True)
    agent_status = models.BooleanField(default=False)
    registration = models.BooleanField(default=False)
    change_address = models.BooleanField(default=False)
    change_ofd = models.BooleanField(default=False)
    change_in_automate = models.BooleanField(default=False)
    change_fn = models.BooleanField(default=False)
    change_to_offline = models.BooleanField(default=False)
    change_to_online = models.BooleanField(default=False)
    change_client_name = models.BooleanField(default=False)
    change_other = models.BooleanField(default=False)
    old_fn_fd = models.IntegerField(max_length=8)
    old_fn_fp = models.IntegerField(max_length=10)
    old_fn_datetime = models.DateTimeField()
    new_fn_fd = models.IntegerField(max_length=8)
    new_fn_fp = models.IntegerField(max_length=10)
    new_fn_datetime = models.DateTimeField()
