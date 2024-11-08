from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include("apps.users.api.urls")),
    path('company/', include("apps.company.api.urls")),
    path('cages/', include("apps.cages.api.urls")),
    path('animals/', include("apps.animals.api.urls")),
]
