from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('backend.core.urls', namespace='core')),
    #path('crm/', include('backend.crm.urls', namespace='core')),
    #path('servico/', include('backend.servico.urls', namespace='core')),
    path('admin/', admin.site.urls),
]
