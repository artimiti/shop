from django.contrib import admin
from .models import Subscribers

class SubscribersAdmin (admin.ModelAdmin):
    list_display = [field.name for field in Subscribers._meta.fields]

    class Meta:
        model = Subscribers

admin.site.register(Subscribers, SubscribersAdmin)
