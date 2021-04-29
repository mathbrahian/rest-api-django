from django.urls import path, include
from . import views
from .views import NoteViewSet

from rest_framework import routers
router = routers.DefaultRouter()
router.register(r'api', NoteViewSet)

urlpatterns = [
    path('rest_framework/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('', views.note),
    path('<int:id>/', views.note_id),
]

