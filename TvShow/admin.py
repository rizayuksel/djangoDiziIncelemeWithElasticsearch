from django.contrib import admin
from .models import TvShow, Comment, Watchlist

# Register your models here.

@admin.register(TvShow)
class TvShowAdmin(admin.ModelAdmin): #Admin panelini özelleştirmek için
    list_display = ["title","kind","year","director","season","imdbPoint","visitors"] #Admin panelinde göstermek istediğimiz bilgiler
    search_fields = ["keywords"] #Admin paneline arama çubuğu geldi
    list_filter = ["title","kind","year","director","season","imdbPoint","visitors"] #Admin panelinde filtre oluşturduk
    list_max_show_all = 15
    class Meta:
        model = TvShow

admin.site.register(Comment)

admin.site.register(Watchlist)