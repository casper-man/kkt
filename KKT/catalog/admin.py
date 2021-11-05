from django.contrib import admin

# Register your models here.
from .models import FnModel, OfdModel, ClientsModel, KktModel, CatalogModel, FnLiveModel

admin.site.register(FnModel)
admin.site.register(OfdModel)
admin.site.register(ClientsModel)
admin.site.register(KktModel)
admin.site.register(CatalogModel)
admin.site.register(FnLiveModel)