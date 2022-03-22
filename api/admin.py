from django.contrib import admin
from .models import Person, Address
from django import forms
from django.forms import Textarea, ChoiceField


class PersonAdminForm(forms.ModelForm):
    class Meta:
        model = Person
        exclude = ()
        widgets = {
            'name': Textarea(attrs={'cols': '80', 'rows': '1'}),
            'email': Textarea(attrs={'cols': '80', 'rows': '1'})
        }


class AddressAdminForm(forms.ModelForm):
    class Meta:
        model = Address
        exclude = ()
        widgets = {
            'street': Textarea(attrs={'cols': '80', 'rows': '3'}),
            'city': Textarea(attrs={'cols': '40', 'rows': '1'})
        }


class PersonAdmin(admin.ModelAdmin):
    search_fields = ['name', 'email']
    list_per_page = 20
    form = PersonAdminForm


class AddressAdmin(admin.ModelAdmin):
    list_filter = ['street', 'city', 'state']
    search_fields = ['number', 'street', 'city', 'state']
    list_per_page = 20
    form = AddressAdminForm


admin.site.register(Person, PersonAdmin)
admin.site.register(Address, AddressAdmin)
