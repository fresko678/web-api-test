from django.urls import path
from main import views


urlpatterns = [
    path('', views.List.as_view(), name='home'),
    path('add', views.Create.as_view(), name='add'),
    path('<int:pk>/update', views.Update.as_view(), name='update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete')
]
