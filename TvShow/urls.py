from django.contrib import admin
from django.urls import path
from . import views

app_name = "TvShow" #Redirect için gerek

urlpatterns = [
    path('crime/', views.crime, name="crime"),
    path('comedy/', views.comedy, name="comedy"),
    path('mystery/', views.mystery, name="mystery"),
    path('scifi/', views.scifi, name="scifi"),
    path('sport/', views.sport, name="sport"),
    path('action/', views.action, name="action"),
    path('documentary/', views.documentary, name="documentary"),
    path('detective/', views.detective, name="detective"),
    path('drama/', views.drama, name="drama"),
    path('thriller/', views.thriller, name="thriller"),
    path('horror/', views.horror, name="horror"),
    path('romantic/', views.romantic, name="romantic"),
    path('historical/', views.historical, name="historical"),
    path('foreign/', views.foreign, name="foreign"),
    path('domestic/', views.domestic, name="domestic"),
    path('detail/<int:id>', views.detail, name="detail"),
    path('comment/<int:id>', views.comment, name="comment"),
    path('watchlist/<int:id>', views.watchlist, name="watchlist"),
]