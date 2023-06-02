from django.contrib import admin
from .models import Auto, ExtraInfo, Ocena, Model_auta

admin.site.register(Model_auta)

class ExtraInfoInline(admin.TabularInline):
    model = ExtraInfo

class OcenaInline(admin.TabularInline):
    model = Ocena
    extra = 0

class Model_autaInline(admin.TabularInline):
    model = Model_auta.auto.through
    extra = 0

@admin.register(Auto)
class AutoAdmin(admin.ModelAdmin):
    inlines = [ExtraInfoInline, OcenaInline, Model_autaInline]