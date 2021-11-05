from django.db import models

# Create your models here.
class FnLiveModel(models.Model):
    fn_live_mons = models.IntegerField(verbose_name='Срок ФН (мес)')
    fn_live_deys = models.IntegerField(verbose_name='Срок ФН (ден)')

    class Meta:
        verbose_name = "Срок жизни ФН"
        verbose_name_plural = "Сроки жизни ФН"

    def __str__(self):
        return 'Срок жизни ФН %s (%s дней)' % (self.fn_live_mons, self.fn_live_deys)


class FnModel(models.Model):
    #Fields
    ffd = models.CharField(max_length=4, verbose_name='ФФД')
    fh_type = models.CharField(max_length=10, verbose_name='Исполнение')
    id_fn_live = models.ForeignKey(FnLiveModel, on_delete=models.PROTECT, default=1, blank=True, verbose_name='Срок службы')
    fn_z_nom = models.IntegerField(verbose_name='Заводской номер')
    fn_status = models.BooleanField(default=True, verbose_name='Статус')
    fn_data_start = models.DateField(auto_now_add=False, verbose_name='Дата регистрации')
    fn_data_end = models.DateField(blank=True, verbose_name='Дата закрытия')

    class Meta:
        verbose_name = "Модель ФН"
        verbose_name_plural = "Модели ФН"

    def __str__(self):
        return 'ФН (%s) Исполнение %s (%s)' % (self.ffd, self.fh_type, self.id_fn_live)


class OfdModel(models.Model):
    # Fields
    ofd_inn = models.CharField(max_length=12, verbose_name='ИНН')
    ofd_full_name = models.CharField(max_length=250, verbose_name='Наименование')
    ofd_short_name = models.CharField(max_length=150, verbose_name='Краткое наименование')
    ofd_url = models.CharField(max_length=50, verbose_name='Адрес сайта')
    ofd_set_address = models.CharField(max_length=50, verbose_name='Адрес отправки чеков', blank=True)
    ofd_set_port = models.CharField(max_length=6, verbose_name='Порт', blank=True)
    ofd_set_email = models.CharField(max_length=50, verbose_name='E-mail отправки чеков', blank=True)

    class Meta:
        verbose_name = "Оператор ОФД"
        verbose_name_plural = "Операторы ОФД"

    def __str__(self):
        return '%s (%s)' % (self.ofd_short_name, self.ofd_inn)


class ClientsModel(models.Model):
    # Fields
    client_inn = models.CharField(max_length=12)
    client_ogrn = models.CharField(max_length=16)
    ip = models.BooleanField(default=True)
    client_full_name = models.CharField(max_length=250)
    client_short_name = models.CharField(max_length=150)
    director_inn = models.CharField(max_length=12, blank=True)
    agent = models.CharField(max_length=150, blank=True)
    agent_doc = models.CharField(max_length=150, blank=True)
    sno_osn = models.BooleanField(default=False)
    sno_usn_d = models.BooleanField(default=False)
    sno_usn_d_r = models.BooleanField(default=False)
    sno_eshn = models.BooleanField(default=False)
    sno_psn = models.BooleanField(default=False)
    sno_ndp = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Контрагент"
        verbose_name_plural = "Контрагенты"

    def __str__(self):
        return '%s (%s)' % (self.client_short_name, self.client_inn)


class KktModel(models.Model):
    # Fields
    rmk = models.CharField(max_length=16)
    id_client = models.ForeignKey(ClientsModel, on_delete=models.PROTECT)
    id_ofd = models.ForeignKey(OfdModel, on_delete=models.PROTECT)
    date_reg = models.DateField(auto_now_add=True)
    kkt_model = models.CharField(max_length=150)
    kkt_z_nom = models.CharField(max_length=150)
    id_fn = models.ForeignKey(FnModel, on_delete=models.PROTECT)
    kkt_address = models.CharField(max_length=350)
    kkt_place = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Касса"
        verbose_name_plural = "Кассы"

    def __str__(self):
        return 'ККТ %s (%s)' % (self.kkt_model, self.id_client)


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
    old_fn_fd = models.IntegerField(blank=True)
    old_fn_fp = models.IntegerField(blank=True)
    old_fn_datetime = models.DateTimeField(blank=True)
    new_fn_fd = models.IntegerField(blank=True)
    new_fn_fp = models.IntegerField(blank=True)
    new_fn_datetime = models.DateTimeField(blank=True)

    class Meta:
        verbose_name = "Запись ККТ"
        verbose_name_plural = "Записи ККТ"

    def __str__(self):
        return '%s (%s) запись от %s' % (self.id_kkt, self.id_client, self.date)
