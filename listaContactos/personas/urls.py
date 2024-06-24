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
    PersonaDetailView,
    PersonaCreateView,
    PersonaUpdateView,
    PersonaDeleteView,
    )

urlpatterns = [
    path('', PersonaListView.as_view(), name = 'persona-list'),
    path('<int:pk>/', PersonaDetailView.as_view(), name = 'persona-detail'),
    path('create/', PersonaCreateView.as_view(), name = 'persona-create'),
    path('<int:pk>/update/', PersonaUpdateView.as_view(), name = 'persona-update'),
    path('<int:pk>/delete/', PersonaDeleteView.as_view(), name = 'persona-delete'),
    path('people/', personaTestView, name='personas'),
    path('add/', personaCreateView1, name='adding'),
    path('anotherAdd/', personasAnotherCreateView, name='anotherAdding'),
    path('search/', searchForHelp, name='buscar'),
    #path('<int:myID>/', personasShowObject, name = 'browsing'),
    #path('<int:myID>/delete/', personasDeleteView, name = 'deleting'),
    #path('', personasListView, name = 'listing'),
]