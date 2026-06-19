# ====================================================
# أضف هذه الـ Views في award/views.py
# ====================================================
# أضف هذا السطر مع الـ imports في الأعلى:
# from django.shortcuts import render, get_object_or_404

def news_list(request):
    """صفحة قائمة الأخبار"""
    all_news = News.objects.filter(is_published=True).order_by('-date')
    return render(request, 'award/news_list.html', {
        'all_news': all_news,
    })

def news_detail(request, pk):
    """صفحة تفاصيل الخبر"""
    news = get_object_or_404(News, pk=pk, is_published=True)
    return render(request, 'award/news_detail.html', {
        'news': news,
    })

def photos_page(request):
    """صفحة الصور"""
    photos = Photo.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'award/photos.html', {
        'photos': photos,
    })

def videos_page(request):
    """مكتبة الفيديو"""
    videos = Video.objects.filter(is_active=True).order_by('order')
    return render(request, 'award/videos.html', {
        'videos': videos,
    })

def success_stories_page(request):
    """قصص النجاح"""
    stories = SuccessStory.objects.filter(is_active=True).order_by('-date')
    return render(request, 'award/success_stories.html', {
        'stories': stories,
    })

def statistics_page(request):
    """صفحة الإحصائيات"""
    return render(request, 'award/statistics.html')

def winners_page(request):
    """صفحة الفائزون"""
    categories = WinnerCategory.objects.filter(is_active=True).order_by('order')
    return render(request, 'award/winners.html', {
        'categories': categories,
    })
