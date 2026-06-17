from django.contrib import admin
from django.urls import path
from award import views

# هذين السطرين ضروريان لعرض الصور المرفوعة في وضع التطوير
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('submit/', views.submit_project, name='submit_project'),
]

# هذا السطر هو السحر الذي يسمح بعرض الصور والفيديوهات التي ترفعها من الـ Admin
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)