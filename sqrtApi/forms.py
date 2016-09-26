from django.forms import ModelForm

from sqrtApi.models import SqrtNumber


class SqrtRequestForm(ModelForm):
	class Meta:
		model = SqrtNumber
		fields = ('number',)