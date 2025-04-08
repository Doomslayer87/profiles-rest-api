from django.urls import path
from profiles_api import views

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()) # as_view è la funzione standard che recupera l'endpoint della classe HelloApiView del modulo views.py e renderizza la pagina web (recupera la funzione get definita nella classe HelloApiView)
]
