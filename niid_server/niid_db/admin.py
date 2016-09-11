# -*- coding: utf-8 -*-
from django.contrib import admin
from .models import Passport, ToxChar, Enclosure
from .forms import ToxCharForm, PassportForm, EnclosureForm
from .tools import PASSPORT_TARGET_OBJECTS_CHOICES


class ToxCharAdmin(admin.ModelAdmin):
    form = ToxCharForm

    fields = [('dl50_vz', 'dl50_vz_value'), ('dl50_nk', 'dl50_nk_value'), ('pdk_atmosphere', 'pdk_work_zone'), ('obyv_atmosphere', 'obyv_work_zone'),
              'tox_stomach', 'tox_skin', 'skin_irritation_1', 'skin_irritation_2',
              'eyes_irritation', 'c20', 'sensitization', 'resorbtive_action', ('zbioc_eff_subac', 'subac_value'),
              ('zbioc_eff_ac', 'ac_value'), 'comment']


class EnclosureAdmin(admin.ModelAdmin):
    form = EnclosureForm


class PassportAdmin(admin.ModelAdmin):
    search_fields = ['name', 'formulation']
    list_display = ('name', 'form', 'short_target_objects', 'formulation')
    list_filter = ('form',)
    form = PassportForm

    def short_target_objects(self, obj):
        to = obj.target_objects
        result = ""
        for e in to:
            for i in PASSPORT_TARGET_OBJECTS_CHOICES:
                if i[0] == e:
                    result += i[1] + "; "
        return result

    short_target_objects.allow_tags = True
    short_target_objects.short_description = u"Целевые объекты"

    class EnclosureInLine(admin.StackedInline):
        model = Enclosure
        form = EnclosureForm
        extra = 0

    inlines = (EnclosureInLine,)


admin.site.register(Passport, PassportAdmin)
admin.site.register(ToxChar, ToxCharAdmin)
admin.site.register(Enclosure, EnclosureAdmin)
