from django.urls import path
from .views import wszystkie_auta, szczegoly_auta, nowy_auto


urlpatterns = [
    path('wszystkie/',wszystkie_auta, name='wszystkie_auta'),
    path('wszystkie/<int:auto_id>/',szczegoly_auta, name='szczegoly_auta'),
    path('nowy/', nowy_auto, name='nowy_auto'),

]