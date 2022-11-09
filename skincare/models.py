from django.db import models

# Create your models here.

SKINTYPE_FLAG = (
    ('OILY SKIN', 'OILY SKIN'),
    ('DRY SKIN', 'DRY SKIN'),
    ('NORMAL SKIN', 'NORMAL SKIN')

)


class issues(models.Model):
    name = models.CharField(_('Name'), max_length=100)
    flag = models.CharField(_('flag'), max_length=10, choices=SKINTYPE_FLAG)
    sol = models.TextField(_('SOLUTION'), max_length=10000)
