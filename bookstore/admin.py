from django.contrib import admin
from bookstore import models

# Register your models here.
admin.site.register(models.Tweet)
admin.site.register(models.Comment)
