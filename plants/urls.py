from django.contrib import admin
from django.urls import path
from plants.views import index, ajax_index, detail

urlpatterns = [
    path("index/", index ),
    path("ajax/index/", ajax_index ),
    
    #<int:id> represente l'index de la fleur dans first3flowers (voir datatest.py) 
    #(0 = 1ere fleur rouge, 1 = 2eme fleur rouge, 2 = 3eme fleur rouge)
    #il est passé en argument à la View detail (voir views.py)
    path('index/<int:id>/', detail),
]


#NB : vous ne pouvez cliquer que sur les 3 premieres fleurs