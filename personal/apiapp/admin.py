from django.contrib import admin
from .models import TopManager, Manager, Engineer
# Register your models here.
admin.site.register(TopManager)
admin.site.register(Manager)
admin.site.register(Engineer)