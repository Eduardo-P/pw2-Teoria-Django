from django.urls import path
from personas.views import (
    personaTestView,
    personaCreateView1,
    personasShowObject,
    searchForHelp,
    personasAnotherCreateView,
    personasListView,
    personasDeleteView,
    )
from .views import (
    PersonaListView,
    )

urlpatterns = [
    path('', PersonaListView.as_view(), name = 'persona-list'),
    path('people/', personaTestView, name='personas'),
    path('add/', personaCreateView1, name='adding'),
    path('anotherAdd/', personasAnotherCreateView, name='anotherAdding'),
    path('search/', searchForHelp, name='buscar'),
    path('<int:myID>/', personasShowObject, name = 'browsing'),
    path('<int:myID>/delete/', personasDeleteView, name = 'deleting'),
    #path('', personasListView, name = 'listing'),
]