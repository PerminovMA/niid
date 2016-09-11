# -*- coding: utf-8 -*-

# ## CHOICES FOR MODELS

# Choices for Passport model

BOTTLE = 'BOTTLE'
BRIQUETTE = 'BRIQ'
GEL = 'GEL'
GRANULES = 'GRANUL'
DUST = 'DUST'
FLUID = 'FLUID'
PENCIL = 'PENCIL'
GLUE = 'GLUE'
SNARE = 'SNARE'
EMULSION = 'EMULSI'

PASSPORT_FORM_CHOICES = (
    (BOTTLE, u'Аэрозольные баллоны'),
    (BRIQUETTE, u'Брикет'),
    (GEL, u'Гель'),
    (GRANULES, u'Гранулы'),
    (DUST, u'Дуст'),
    (FLUID, u'Жидкость (раствор)'),
    (PENCIL, u'Карандаш'),
    (GLUE, u'Клей'),
    (SNARE, u'Клейкие ловушки'),
    (EMULSION, u'Концентрат эмульсии'),
)

PASSPORT_TARGET_OBJECTS_CHOICES = (
    ('PARASITE1', u'Блохи'),
    ('PARASITE2', u'Вши головные'),
    ('PARASITE3', u'Вши платяные'),
    ('PARASITE4', u'Другие:-Бабочницы;-Мокрицы;-Ногохвостки;-Сверчки;-Пауки;-Уховертки;-Чешуйницы;'),
    ('PARASITE5', u'Клещи домашней пыли'),
    ('PARASITE6', u'Клещи иксодовые'),
    ('PARASITE7', u'Клещи крысиные'),
    ('PARASITE8', u'Клоп постельный'),
    ('PARASITE9', u'Кожееды'),
    ('PARASITE10', u'Комары'),
    ('PARASITE11', u'Летающие и нелетающие насекомые'),
    ('PARASITE12', u'Летающие насекомые'),
    ('PARASITE13', u'Личинки комаров'),
    ('PARASITE14', u'Мокрицы'),
    ('PARASITE15', u'Моль платяная'),
    ('PARASITE16', u'Мошки'),
    ('PARASITE17', u'Муравьи'),
    ('PARASITE18', u'Мухи'),
    ('PARASITE19', u'Нелетающие насекомые'),
    ('PARASITE20', u'Огневки (вредитель запасов)'),
    ('PARASITE21', u'Тараканы')
)


# Choices for Enclosure model

DISINSECTION_1 = "DIS_1"
DISINSECTION_2 = "DIS_2"
DISINSECTION_3 = "DIS_3"
IMPREGNATION = "IMP_1"
INSECTICIDE = "INS"
TERRITORY_HANDLING = "TER_HA"
PEDICULOSIS_1 = "PED_1"
PEDICULOSIS_2 = "PED_2"
OTHER = "OTHER"

ENCLOSURE_APP_SCOPE_CHOICES = (
    (DISINSECTION_1, u'Дезинсекция белья и вещей'),
    (DISINSECTION_2, u'Дезинсекция на объектах железнодорожного транспорта и метрополитена'),
    (DISINSECTION_3, u'Дезинсекция помещений от вшей и чесоточных клещей'),
    (IMPREGNATION, u'Импрегнация тканей'),
    (INSECTICIDE, u'Инсектицид'),
    (TERRITORY_HANDLING, u'Обработка территории от иксодовых клещей'),
    (PEDICULOSIS_1, u'Педикулицид; взрослые и дети'),
    (PEDICULOSIS_2, u'Педикулицид; взрослые с 16 лет'),
    (OTHER, u'Уничтожение членистоногих в МО, для обработки отходов классов А, Б и В и др.'),
)

# Choices for ToxChar model

POSITIVE_MOUSE = "POS_MO"
NEGATIVE_MOUSE = "NEG_MO"
POSITIVE_RATS = "POS_RA"
NEGATIVE_RATS = "NEG_RA"

TOXCHAR_RES_ACT_CHOICES = (
    (POSITIVE_MOUSE, u'Наличие эффекта, мыши'),
    (NEGATIVE_MOUSE, u'Отсутствие эффекта, мыши'),
    (POSITIVE_RATS, u'Наличие эффекта, крысы'),
    (NEGATIVE_RATS, u'Отсутствие эффекта, крысы'),
)

DANGER_RATE_1 = "DR_1"
DANGER_RATE_2 = "DR_2"
DANGER_RATE_3 = "DR_3"
DANGER_RATE_4 = "DR_4"

TOXCHAR_ZBIOC_AC_CHOICES = (
    (DANGER_RATE_1, u'I класс. Чрезвычайно-опасные: менее 10'),
    (DANGER_RATE_2, u'II класс. Высокоопасные: 10-30'),
    (DANGER_RATE_3, u'III класс. Умеренно-опасные: 31-100'),
    (DANGER_RATE_4, u'IV класс. Малоопасные: более 100'),
)

TOXCHAR_ZBIOC_SUBAC_CHOICES = (
    (DANGER_RATE_1, u'I класс. Чрезвычайно-опасные: менее 1'),
    (DANGER_RATE_2, u'II класс. Высокоопасные: 1-5'),
    (DANGER_RATE_3, u'III класс. Умеренно-опасные: 5,1-10'),
    (DANGER_RATE_4, u'IV класс. Малоопасные: более 10'),
)

TOXCHAR_C20_CHOICES = (
    (DANGER_RATE_1, u'I класс. Чрезвычайно-опасные: гибель'),
    (DANGER_RATE_2, u'II класс. Высоко-опасные: клиника отравления, гибель отсутствует'),
    (DANGER_RATE_3,
     u'III класс. Умеренно-опасные: С20 > Limzc, min изменения интегральных показателей (пороговый уровень)'),
    (DANGER_RATE_4, u'IV класс. Мало-опасные: не оказывают токсического действия'),
)

HIGH_RABBITS = "HG_RAB"
NORMAL_RABBITS = "NORMAL_RAB"
WEAK_RABBITS = "WE_RAB"
ABSENCE_RABBITS = "AB_RAB"
NOT_RABBITS = "NO_RAB"  # not determine rabbits
HIGH_PIGS = "HG_PIG"
NORMAL_PIGS = "NORMAL_PIG"
WEAK_PIGS = "WE_PIG"
ABSENCE_PIGS = "AB_PIG"
NOT_PIGS = "NO_PIG"  # not determine pigs


TOXCHAR_IRRITATION_CHOICES = (
    (HIGH_RABBITS, u"Выраженное, кролики"),
    (NORMAL_RABBITS, u"Умеренное, кролики"),
    (WEAK_RABBITS, u"Слабое, кролики"),
    (ABSENCE_RABBITS, u"Отсутствует, кролики"),
    (NOT_RABBITS, u"Не определяли, кролики"),
    (HIGH_PIGS, u"Выраженное, морские свинки"),
    (NORMAL_PIGS, u"Умеренное, морские свинки"),
    (WEAK_PIGS, u"Слабое, морские свинки"),
    (ABSENCE_PIGS, u"Отсутствует, морские свинки"),
    (NOT_PIGS, u"Не определяли, морские свинки"),
)

HIGH_MOUSE = "HG_MOU"
NORMAL_MOUSE = "NORMAL_MOU"
WEAK_MOUSE = "WE_MOU"
ABSENCE_MOUSE = "AB_MOU"
HIGH_PIGS_VKNK = "HG_PIG_VKNK"
NORMAL_PIGS_VKNK = "NORMAL_PIG_VKNK"
WEAK_PIGS_VKNK = "WE_PIG_VKNK"
ABSENCE_PIGS_VKNK = "AB_PIG_VKNK"
NOT_PIGS_VKNK = "NO_PIG_VKNK"  # not determine pigs
NORMAL_PIGS_NK = "NORMAL_PIG_NK"
WEAK_PIGS_NK = "WE_PIG_NK"
ABSENCE_PIGS_NK = "AB_PIG_NK"
NOT_PIGS_NK = "NO_PIG_NK"  # not determine pigs

TOXCHAR_SENSITIZATION_CHOICES = (
    (HIGH_MOUSE, u"ГЗТ мыши – выраженный эффект"),
    (NORMAL_MOUSE, u"ГЗТ мыши – умеренный эффект"),
    (WEAK_MOUSE, u"ГЗТ мыши – слабый эффект"),
    (ABSENCE_MOUSE, u"ГЗТ мыши – отсутствие эффекта"),
    (HIGH_PIGS_VKNK, u"Морские свинки в/к и н/к - выраженный эффект"),
    (NORMAL_PIGS_VKNK, u"Морские свинки в/к и н/к - умеренный эффект"),
    (WEAK_PIGS_VKNK, u"Морские свинки в/к и н/к - слабый эффект"),
    (ABSENCE_PIGS_VKNK, u"Морские свинки н/к - выраженный эффект"),
    (NOT_PIGS_VKNK, u"Морские свинки в/к и н/к - отсутствие эффекта"),
    (NORMAL_PIGS_NK, u"Морские свинки н/к - умеренный эффект"),
    (WEAK_PIGS_NK, u"Морские свинки н/к - слабый эффект"),
    (NOT_PIGS_NK, u"Морские свинки н/к - отсутствие эффекта"),
)

DANGER_RATE_1_MOUSE = "DR_1_l15_mouse"
DANGER_RATE_2_MOUSE = "DR_2_15_150_mouse"
DANGER_RATE_3_MOUSE = "DR_3_151_5000_mouse"
DANGER_RATE_4_MOUSE = "DR_4__m5000_mouse"

DANGER_RATE_1_RATS = "DR_1_l15_rats"
DANGER_RATE_2_RATS = "DR_2_15_150_rats"
DANGER_RATE_3_RATS = "DR_3_151_5000_rats"
DANGER_RATE_4_RATS = "DR_4__m5000_rats"

TOXCHAR_TOX_STOMACH_CHOICES = (
    (DANGER_RATE_1_MOUSE, u"I класс. Чрезвычайно-опасные: менее 15, мыши"),
    (DANGER_RATE_2_MOUSE, u"II класс. Высокоопасные: 15-150, мыши"),
    (DANGER_RATE_3_MOUSE, u"III класс. Умеренно-опасные: 151-5000, мыши"),
    (DANGER_RATE_4_MOUSE, u"IV класс. Малоопасные: более 5000, мыши"),
    (DANGER_RATE_1_RATS, u"I класс. Чрезвычайно-опасные: менее 15, крысы"),
    (DANGER_RATE_2_RATS, u"II класс. Высокоопасные: 15-150, крысы"),
    (DANGER_RATE_3_RATS, u"III класс. Умеренно-опасные: 151-5000, крысы"),
    (DANGER_RATE_4_RATS, u"IV класс. Малоопасные: более 5000, крысы"),
)

DANGER_RATE_1_MOUSE = "DR_1_l100_mouse"
DANGER_RATE_2_MOUSE = "DR_2_100_500_mouse"
DANGER_RATE_3_MOUSE = "DR_3_501_2500_mouse"
DANGER_RATE_4_MOUSE = "DR_4__m2500_mouse"

DANGER_RATE_1_RATS = "DR_1_l100_rats"
DANGER_RATE_2_RATS = "DR_2_100_500_rats"
DANGER_RATE_3_RATS = "DR_3_501_2500_rats"
DANGER_RATE_4_RATS = "DR_4__m2500_rats"

TOXCHAR_TOX_SKIN_CHOICES = (
    (DANGER_RATE_1_MOUSE, u"I класс. Чрезвычайно-опасные: менее 100, мыши"),
    (DANGER_RATE_2_MOUSE, u"II класс. Высокоопасные: 100-500, мыши"),
    (DANGER_RATE_3_MOUSE, u"III класс. Умеренно-опасные: 501-2500, мыши"),
    (DANGER_RATE_4_MOUSE, u"IV класс. Малоопасные: более 2500, мыши"),
    (DANGER_RATE_1_RATS, u"I класс. Чрезвычайно-опасные: менее 100, крысы"),
    (DANGER_RATE_2_RATS, u"II класс. Высокоопасные: 100-500, крысы"),
    (DANGER_RATE_3_RATS, u"III класс. Умеренно-опасные: 501-2500, крысы"),
    (DANGER_RATE_4_RATS, u"IV класс. Малоопасные: более 2500, крысы"),
)

# ##

# Common choices

PEOPLE = "PEOPLE"
PEOPLE_CHILDREN = "PEOPLE_CHILDREN"
SPECIALIST = "SPECIALIST"
SPECIALIST_PEOPLE = "SPECIALIST_PEOPLE"
SPECIALIST_PEOPLE_CHILDREN = "SPECIALIST_PEOPLE_CHILDREN"

PURPOSE_CHOICES = (
    (PEOPLE, u'Населением в быту'),
    (PEOPLE_CHILDREN, u'Населением в быту, включая детей'),
    (SPECIALIST, u'Специалистами'),
    (SPECIALIST_PEOPLE, u'Специалистами и населением в быту'),
    (SPECIALIST_PEOPLE_CHILDREN, u'Специалистами и населением в быту, включая детей'),
)

# ##
