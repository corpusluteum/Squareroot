from __future__ import absolute_import
from sqrtApi.models import SqrtNumber
from celery import shared_task
import decimal

@shared_task
def squareRootProcess(var):
    new = SqrtNumber(number=var, sqrt=takesRoot(var))
    new.save()

def takesRoot(number):
    n = int(number)
    assert n > 0
    with decimal.localcontext() as ctx:
        ctx.prec += 2
        x, prior = decimal.Decimal(n), None
        while x != prior:
            prior = x
            x = (x + n / x) / 2
    return +x
