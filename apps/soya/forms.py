# coding: utf-8
from django import forms
from models import Zakaz


class Zakazat(forms.ModelForm):
	class Meta:
		model = Zakaz
		fields = ('name','number', 'soya_sort', 'how_many', )