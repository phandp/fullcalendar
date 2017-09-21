from django.db import models

from django.utils.translation import ugettext_lazy as _
from django.utils.encoding import smart_text


class CalendarEvent(models.Model):
    title = models.CharField(_('Title'), blank=True, max_length=200)
    start = models.DateTimeField(_('Start'))
    end = models.DateTimeField(_('End'))
    all_day = models.BooleanField(_('All day'), default=False)

    class Meta:
        verbose_name = _('Aufgabe')
        verbose_name_plural = _('Aufgaben')

    def __str__(self):
        return self.title

# Create your models here.
