from django.contrib import admin
from django.urls import path
from award import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('submit/', views.submit_project, name='submit_project'),

    # صفحة الأخبار
    path('news/', views.news_list, name='news_list'),
    path('news/<int:pk>/', views.news_detail, name='news_detail'),

    # صفحة الصور
    path('photos/', views.photos_page, name='photos_page'),

    # مكتبة الفيديو
    path('videos/', views.videos_page, name='videos_page'),

    # قصص النجاح
    path('success-stories/', views.success_stories_page, name='success_stories_page'),

    # الإحصائيات
    path('statistics/', views.statistics_page, name='statistics_page'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)