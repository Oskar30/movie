from django.contrib import admin, messages
from .models import Movie, Director, Acter
from django.db.models import QuerySet

admin.site.register(Director)
admin.site.register(Acter)


class RatingFilter(admin.SimpleListFilter):
    title = 'Фильтр по рейтингу'
    parameter_name = 'rating'

    def lookups(self, request, model_admin):
        return [
            ('<40', 'Низкий'),
            ('от 40 до 59', 'Средний'),
            ('от 60 до 79','Высокий'),
            ('>=80','Высочайший'),
        ]

    def queryset(self, request, queryset: QuerySet):
        if self.value() == '<40':
            return queryset.filter(rating__lt=40)
        
        if self.value() == 'от 40 до 59':
            return queryset.filter(rating__gte=40).filter(rating__lt=60)

        if self.value() == 'от 60 до 79':
            return queryset.filter(rating__gte=60).filter(rating__lt=80)

        if self.value() == '>=80':
            return queryset.filter(rating__gte=80)


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    # fields = ['name', 'rating']
    exclude = ['slug']
    readonly_fields = ['year']
    # prepopulated_fields = {'slug':('name',)}

    list_display = ['name', 'rating', 'budget', 'currency', 'director']
    list_editable = ['rating', 'currency', 'director']
    ordering = ['name']
    list_per_page = 5
    actions = ['set_usd', 'set_eur']
    search_fields = ['name']
    list_filter = ['currency', RatingFilter]


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