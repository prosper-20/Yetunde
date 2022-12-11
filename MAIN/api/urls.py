from django.urls import path
from .views import api_home_page, api_detail_page, api_update_view, api_delete_view, api_create_view

urlpatterns = [
    path("home", api_home_page, name="api-home"),
    path("<slug:slug>/", api_detail_page, name="api-detail"),
    path("<slug:slug>/update", api_update_view, name="update"),
    path("<slug:slug>/delete", api_delete_view, name="delete"),
    path("create", api_create_view, name="create")
]   