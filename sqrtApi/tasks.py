from __future__ import absolute_import
from sqrtApi.models import SqrtNumber
from celery import shared_task


@shared_task
def squareRootProcess(tmpl_vars):
    new = SqrtNumber(number=tmpl_vars[0], sqrt=tmpl_vars[1])
    new.save()
