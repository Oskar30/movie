from django.contrib import admin, messages
from .models import Movie
from django.db.models import QuerySet

@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'budget', 'currency']
    list_editable = ['rating', 'currency']
    ordering = ['name']
    list_per_page = 5
    actions = ['set_usd', 'set_eur']


    @admin.action(description='Установить валюту USD')
    def set_usd(self, request, queryset:QuerySet):
        queryset.update(currency=Movie.USD)


    @admin.action(description='Установить валюту EUR')
    def set_eur(self, request, queryset:QuerySet):
        count_updated = queryset.update(currency=Movie.EUR)
        self.message_user(
            request,
            f'Обновлено {count_updated} записей',
            messages.INFO
        )