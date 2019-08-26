from django.urls import path
from utilities import views,admin
from django.conf import settings
from django.conf.urls.static import static

app_name="utilities"

urlpatterns = [

 path('login/',views.myapp, name='login'),
 path('home/',views.myhome, name='home'),
 path('findplaces/',views.findplaces, name='findplaces'),
 path('closest/',views.closest, name='closest'),

 ]

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
