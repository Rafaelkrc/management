from django.contrib.admin import ModelAdmin, register
from app.employees.models import Countries, State, Cities, Job, Employees


@register(Countries)
class CountriesAdmin(ModelAdmin):
    list_display = ('id', 'country', 'abbreviation', 'continent')
    search_fields = ('country', 'abbreviation', 'continent',)


@register(State)
class StateAdmin(ModelAdmin):
    list_display = ('state', 'abbreviation', 'country', 'region')
    search_fields = ('state', 'abbreviation', 'country__country', 'region',)


@register(Cities)
class CitiesAdmin(ModelAdmin):
    list_display = ('city', 'state')
    search_fields = ('city', 'state__state',)


@register(Job)
class JobAdmin(ModelAdmin):
    list_display = ('job', 'description_job')
    search_fields = ('job',)


@register(Employees)
class EmployessAdmin(ModelAdmin):
    list_display = ('identifier', 'full_name', 'surname', 'address_street', 'address_number', 'postal_code', 'city',
                    'telephone_number', 'mobile_number', 'date_of_birth', 'position_job', 'date_of_registration', 'photo',)
    search_fields = ('identifier', 'full_name', 'surname', 'address_street', 'address_number', 'postal_code', 'city__city',
                     'telephone_number', 'mobile_number', 'date_of_birth', 'position_job__job', 'date_of_registration', 'photo',)
