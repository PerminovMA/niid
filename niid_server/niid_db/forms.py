# -*- coding: utf-8 -*-

from django import forms
from .models import ToxChar, Passport, Enclosure
from .tools import *


class ToxCharForm(forms.ModelForm):
    skin_irritation_1 = forms.MultipleChoiceField(choices=TOXCHAR_IRRITATION_CHOICES,
                                                  widget=forms.CheckboxSelectMultiple,
                                                  label=ToxChar._meta.get_field('skin_irritation_1').verbose_name,
                                                  required=not ToxChar._meta.get_field('skin_irritation_1').blank)
    skin_irritation_2 = forms.MultipleChoiceField(choices=TOXCHAR_IRRITATION_CHOICES,
                                                  widget=forms.CheckboxSelectMultiple,
                                                  label=ToxChar._meta.get_field('skin_irritation_2').verbose_name,
                                                  required=not ToxChar._meta.get_field('skin_irritation_2').blank)
    eyes_irritation = forms.MultipleChoiceField(choices=TOXCHAR_IRRITATION_CHOICES,
                                                widget=forms.CheckboxSelectMultiple,
                                                label=ToxChar._meta.get_field('eyes_irritation').verbose_name,
                                                required=not ToxChar._meta.get_field('eyes_irritation').blank)
    sensitization = forms.MultipleChoiceField(choices=TOXCHAR_SENSITIZATION_CHOICES,
                                              widget=forms.CheckboxSelectMultiple,
                                              label=ToxChar._meta.get_field('sensitization').verbose_name,
                                              required=not ToxChar._meta.get_field('sensitization').blank)
    resorbtive_action = forms.MultipleChoiceField(choices=TOXCHAR_RES_ACT_CHOICES,
                                                  widget=forms.CheckboxSelectMultiple,
                                                  label=ToxChar._meta.get_field('resorbtive_action').verbose_name,
                                                  required=not ToxChar._meta.get_field('resorbtive_action').blank)

    class Meta:
        model = ToxChar
        fields = ['dl50_vz', 'dl50_vz_value', 'dl50_nk', 'dl50_nk_value', 'pdk_atmosphere', 'pdk_work_zone',
                  'obyv_atmosphere', 'obyv_work_zone', 'skin_irritation_1', 'skin_irritation_2',
                  'eyes_irritation', 'c20', 'sensitization', 'resorbtive_action', 'zbioc_eff_subac', 'subac_value',
                  'zbioc_eff_ac', 'ac_value', 'comment']


class PassportForm(forms.ModelForm):
    target_objects = forms.MultipleChoiceField(choices=PASSPORT_TARGET_OBJECTS_CHOICES,
                                               widget=forms.CheckboxSelectMultiple,
                                               label=Passport._meta.get_field('target_objects').verbose_name,
                                               required=not Passport._meta.get_field('target_objects').blank)

    class Meta:
        model = Passport
        fields = ['name', 'reg_num', 'manufacturer', 'receiver', 'reg_date', 'protocol_of_research', 'destination',
                  'form', 'target_objects', 'formulation', 'comment', 'report_file', 'instruction_file', 'tox_char']


class EnclosureForm(forms.ModelForm):
    target_objects = forms.MultipleChoiceField(choices=PASSPORT_TARGET_OBJECTS_CHOICES,
                                               widget=forms.CheckboxSelectMultiple,
                                               label=Enclosure._meta.get_field('target_objects').verbose_name,
                                               required=not Enclosure._meta.get_field('target_objects').blank,
                                               help_text=u'Для выбора нескольких объектов зажмите ctrl')

    class Meta:
        model = Enclosure
        fields = ['application_scope', 'target_objects', 'destination', 'work_concentration', 'expense',
                  'exposition_time',
                  'ovicide_action', 'comment', 'passport', 'tox_char']
