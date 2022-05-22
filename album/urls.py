from django.urls import path

from . import views

app_name = 'album'
urlpatterns = [
    path('', views.top, name='top'),
    path('album', views.album, name='album'),
    path('mkarticle', views.mkarticle, name='mkarticle'),
    path('detail/<int:album_id>/', views.detail, name='detail'),
    path('create/', views.create, name='create'),
    path('update/<int:pk>/', views.UpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AlbumDeleteView.as_view(), name='delete'),
    path('mkmake1/<int:number>', views.mkmake1, name='mkmake1'),
]
