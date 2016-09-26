from __future__ import absolute_import
from sqrtApi.models import SqrtNumber
from celery import shared_task


@shared_task
def squareRootProcess(tmpl_vars):
    new = SqrtNumber(number=tmpl_vars, sqrt=takesRoot(int(tmpl_vars)))
    new.save()

def takesRoot(number):
    low = 0
    high = number + 1
    while high - low > 1:
        mid = (low + high) / 2
        if mid * mid <= number:
           low = mid
        else:
            high = mid
    return low
