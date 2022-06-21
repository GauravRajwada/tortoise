from django.contrib import admin
from .models import Plans
# Register your models here.
@admin.register(Plans)
class PlansAdmin(admin.ModelAdmin):
    list_display=['planName',
                    'amounts','tenure',
                    'benifitPercentage',
                    'bTypes',
                    'benifitTypes']
