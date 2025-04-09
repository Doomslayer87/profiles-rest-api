from django.urls import path,include
from rest_framework.routers import DefaultRouter
from profiles_api import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

urlpatterns = [
    path('hello-view/', views.HelloApiView.as_view()), # as_view è la funzione standard che recupera l'endpoint della classe HelloApiView del modulo views.py e renderizza la pagina web (recupera la funzione get definita nella classe HelloApiView),
    path('', include(router.urls))
]
