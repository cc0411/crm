from django.contrib import admin
from web import  models


# Register your models here.


admin.site.register(models.Host)
admin.site.register(models.HostGroup)
admin.site.register(models.IDC)
admin.site.register(models.Tag)
admin.site.register(models.BindHost)
admin.site.register(models.UserProfile)
admin.site.register(models.Dep)