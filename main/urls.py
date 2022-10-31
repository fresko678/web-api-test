from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('add', views.add, name='add'),
    path('<int:pk>/update', views.Update.as_view(), name='update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete')
]
