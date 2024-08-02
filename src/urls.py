from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include
from ferramentas.views import index
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="home"),  
    path('ferramentas/', include("ferramentas.urls"),name="ferramentas"), 
    path('accounts/', include('accounts.urls'), name="login"), 
]

# Adicionar URLs para servir arquivos estáticos durante o desenvolvimento
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
