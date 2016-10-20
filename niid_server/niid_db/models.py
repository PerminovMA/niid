# -*- coding: utf-8 -*-
from django.db import models
from random import randint
from django.conf import settings
from time import time
from django.dispatch.dispatcher import receiver
from django.db.models.signals import pre_delete
from .tools import *
from django.contrib.postgres.fields import ArrayField

__author__ = 'PerminovMA@live.ru'


class ToxChar(models.Model):
    """Toxicological characteristics"""
    dl50_vz = models.CharField(max_length=255, verbose_name=u"DL50", choices=TOXCHAR_TOX_STOMACH_CHOICES)
    dl50_vz_value = models.CharField(max_length=100, verbose_name=u"Значение DL50 в/ж, мг/кг", blank=True, null=True)
    dl50_nk = models.CharField(max_length=255, verbose_name=u"DL50", choices=TOXCHAR_TOX_SKIN_CHOICES)
    dl50_nk_value = models.CharField(max_length=100, verbose_name=u"Значение DL50 н/к, мг/кг", blank=True, null=True)
    pdk_atmosphere = models.DecimalField(max_length=100, decimal_places=3, max_digits=7, blank=True, null=True,
                                         verbose_name=u"ПДК в атмосферном воздухе", help_text=u"мг/м3")
    pdk_work_zone = models.DecimalField(max_length=100, decimal_places=3, max_digits=7, blank=True, null=True,
                                        verbose_name=u"ПДК в воздухе рабочей зоны", help_text=u"мг/м3")
    obyv_atmosphere = models.DecimalField(max_length=100, decimal_places=3, max_digits=7, blank=True, null=True,
                                          verbose_name=u"ОБУВ в атмосферном воздухе", help_text=u"мг/м3")
    obyv_work_zone = models.DecimalField(max_length=100, decimal_places=3, max_digits=7, blank=True, null=True,
                                         verbose_name=u"ОБУВ в воздухе рабочей зоны", help_text=u"мг/м3")
    skin_irritation_1 = ArrayField(
        models.CharField(max_length=100), blank=True, null=True,
        verbose_name=u"Раздраж.действие на кожу")
    skin_irritation_2 = ArrayField(
        models.CharField(max_length=100), blank=True, null=True,
        verbose_name=u"Раздраж.действие на кожу повторное")
    eyes_irritation = ArrayField(
        models.CharField(max_length=100), blank=True, null=True,
        verbose_name=u"Раздраж.действие на глаза")
    c20 = models.CharField(max_length=6, verbose_name=u"С20", blank=True, null=True, choices=TOXCHAR_C20_CHOICES)
    sensitization = ArrayField(
        models.CharField(max_length=100), blank=True, null=True,
        verbose_name=u"Сенсибилизир.действие")
    resorbtive_action = ArrayField(
        models.CharField(max_length=100), blank=True, null=True,
        verbose_name=u"Кожно-резорбтивное действие")
    zbioc_eff_subac = models.CharField(max_length=6, verbose_name=u"Zbioc.eff.subac", blank=True, null=True,
                                       choices=TOXCHAR_ZBIOC_SUBAC_CHOICES)
    subac_value = models.FloatField(verbose_name=u"Значение Zbioc.eff.subac", blank=True, null=True)
    zbioc_eff_ac = models.CharField(max_length=6, verbose_name=u"Zbioc.eff.ac", blank=True, null=True,
                                    choices=TOXCHAR_ZBIOC_AC_CHOICES)
    ac_value = models.FloatField(verbose_name=u"Значение Zbioc.eff.ac", blank=True, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name=u"Комментарий")

    @property
    def is_tox_char_for_passports(self):
        try:
            return self.passport_set is not None
        except Passport.DoesNotExist:
            return False

    def __unicode__(self):
        if self.is_tox_char_for_passports:
            return u"ТХ " + str(self.id)
        else:
            return "Some ToxChar"

    class Meta:
        verbose_name = u"Токсикологическая характеристика"
        verbose_name_plural = u"Токсикологические характеристики"


def generate_filename(filename):
    """returns the new name for save on the server
    :param filename: any name of file
    """
    return str(time()).replace('.', '_') + str(randint(0, 100000)) + filename[filename.rfind('.'):]


def get_upload_files_path(instance, filename):
    return "files/%s/%s/" % (str(randint(1, settings.COUNT_FOLDERS)),
                             str(randint(1, settings.COUNT_FOLDERS))) + generate_filename(filename)


class Passport(models.Model):
    """ Passport of research """
    name = models.CharField(max_length=255, verbose_name=u"Название")
    reg_num = models.CharField(blank=True, null=True, max_length=255, verbose_name=u"Номер госрегистрации")
    manufacturer = models.CharField(blank=True, null=True, max_length=255, verbose_name=u"Заявитель")
    receiver = models.CharField(blank=True, null=True, default=u"Научно-исследовательский институт дезинфектологии",
                                max_length=255, verbose_name=u"Исполнитель")
    reg_date = models.DateField(blank=True, null=True, verbose_name=u"Дата регистрации")
    protocol_of_research = models.CharField(blank=True, null=True, max_length=255,
                                            verbose_name=u"ДВ")
    destination = models.CharField(max_length=100, verbose_name=u"Назначение (описание потребителей)",
                                   choices=PURPOSE_CHOICES)
    form = models.CharField(max_length=50, verbose_name=u"Препаративная форма", choices=PASSPORT_FORM_CHOICES)
    target_objects = ArrayField(
        models.CharField(max_length=100), blank=True, null=True, verbose_name=u"Целевые объекты")
    formulation = models.TextField(verbose_name=u"Рецептура")
    comment = models.TextField(blank=True, null=True, verbose_name=u"Комментарий")
    report_file = models.FileField(blank=True, null=True, upload_to=get_upload_files_path,
                                   verbose_name=u"Отчет")
    instruction_file = models.FileField(blank=True, null=True, upload_to=get_upload_files_path,
                                        verbose_name=u"Инструкция")
    tox_char = models.ForeignKey(ToxChar, verbose_name=u"Токсикологическая характеристика")

    class Meta:
        verbose_name = u"Паспорт"
        verbose_name_plural = u"Паспорта"

    def __unicode__(self):
        return self.name

    def save(self, *args, **kwargs):
        """ delete old report_file/report_file when replacing by updating the file """
        try:
            this = Passport.objects.get(id=self.id)
            if this.report_file != self.report_file:
                this.report_file.delete(save=False)
            if this.instruction_file != self.instruction_file:
                this.instruction_file.delete(save=False)
        except Passport.DoesNotExist:
            pass  # When new report_file/instruction_file then we do nothing, normal case
        super(Passport, self).save(*args, **kwargs)


@receiver(pre_delete, sender=Passport)
def passport_files_deleter(sender, instance, **kwargs):
    """ delete report_file and instruction_file when remove Passport object from admin panel """
    instance.report_file.delete(False)
    instance.instruction_file.delete(False)


class Enclosure(models.Model):
    application_scope = models.CharField(max_length=6, verbose_name=u"Область применения",
                                         choices=ENCLOSURE_APP_SCOPE_CHOICES)
    target_objects = ArrayField(
        models.CharField(max_length=100), blank=True, null=True, verbose_name=u"Целевые объекты")
    destination = models.CharField(max_length=100, verbose_name=u"Назначение (описание потребителей)",
                                   choices=PURPOSE_CHOICES)
    work_concentration = models.CharField(max_length=255, verbose_name=u"Рабочая концентрация")
    expense = models.CharField(max_length=255, verbose_name=u"Норма расхода")
    exposition_time = models.CharField(max_length=255, verbose_name=u"Время экспозиции")
    ovicide_action = models.CharField(max_length=255, verbose_name=u"Овицидное действие", blank=True, null=True)
    comment = models.TextField(blank=True, null=True, verbose_name=u"Комментарий")
    passport = models.ForeignKey(Passport, verbose_name=u"Пасспорт")
    tox_char = models.ForeignKey(ToxChar, blank=True, null=True, verbose_name=u"Токсикологическая характеристика")

    def __unicode__(self):
        return u"Приложение для " + self.passport.name

    class Meta:
        verbose_name = u"Приложение"
        verbose_name_plural = u"Приложения"
