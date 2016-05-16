# -*- coding: utf-8 -*-
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

MASCULINE = 'MSC'
FEMININE = 'FMN'

GENRES = (
    (MASCULINE, _(u'Masculine')),
    (FEMININE, _(u'Feminine')),
)