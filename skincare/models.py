from django.db import models

# Create your models here.

SKINTYPE_TYPE = (
    ('OILY SKIN', 'OILY SKIN'),
    ('DRY SKIN', 'DRY SKIN'),
    ('NORMAL SKIN', 'NORMAL SKIN')

)


class Issue(models.Model):
    name = models.CharField('Problem', max_length=100)
    skin_type = models.CharField(
        'Skin Type', max_length=15, choices=SKINTYPE_TYPE)
    solution = models.TextField('Solution', max_length=10000)

    def __str__(self):
        return self.name


class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()

    def __str__(self):
        return self.name
