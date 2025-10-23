from django.contrib import admin
from django.urls import path
from equipe import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('equipe/', views.cadastro_equipe, name='cadastro_equipe'),
    path('equipes/', views.list, name='list'),
]
