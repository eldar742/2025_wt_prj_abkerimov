from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from melody import views 

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # Mapování pohledů přímo z aplikace melody (přesně podle vzoru chalupnicek)
    path('', views.landing_page, name='landing_page'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('artist/<int:artist_id>/', views.artist_detail, name='artist_detail'),
    path('album/<int:album_id>/', views.album_detail, name='album_detail'),
    path('playlists/', views.playlists, name='playlists'),
    path('playlist/<int:playlist_id>/', views.playlist_detail, name='playlist_detail'),
    path('playlist/new/', views.create_playlist, name='create_playlist'),
    path('add-to-playlist/<int:track_id>/', views.add_to_playlist, name='add_to_playlist'),
    path('playlist/<int:playlist_id>/remove/<int:track_id>/', views.remove_from_playlist, name='remove_from_playlist'),
    path('search/', views.search, name='search'),
    path('signup/', views.signup, name='signup'),
    
    # Autentizace (pokud budeš využívat vestavěné šablony pro login)
    path('auth/', include('django.contrib.auth.urls')),
]

# Pro načítání médií/obrázků
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)