from django.urls import include, path
from . import views

urlpatterns = [
    path('<slug:song>/', views.Index.as_view())
]
