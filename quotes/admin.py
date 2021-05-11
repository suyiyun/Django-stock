from django.contrib import admin
from .models import Stock, Stock2, PredictPrice

admin.site.register(Stock)
admin.site.register(Stock2)
admin.site.register(PredictPrice)