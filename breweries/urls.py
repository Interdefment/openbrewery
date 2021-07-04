from django.urls import path

from . import views


app_name = 'breweries'

urlpatterns = [
    path('recreate_types/', views.create_types, name='create_types'),
    path('download_data/', views.download_data, name='download_data'),
    path('brewery/add', views.BreweriesCreateView.as_view(), name='create'),
    path('brewery/<int:pk>/edit', views.BreweriesUpdateView.as_view(), name='edit'),
    path('brewery/<int:pk>/delete', views.BreweriesDeleteView.as_view(), name='delete'),
    path('brewery/<int:pk>', views.BreweriesDetailView.as_view(), name='detail'),
    path('', views.BreweriesListView.as_view(), name='list'),
]


