from django.shortcuts import render, redirect, get_object_or_404
from .models import (
    Field, SiteSetting, HeroSlide, TimelineEvent, Judge, Submission,
    ThemeSetting, HomeContent, FooterContent, SuccessPageContent,
    SectionBackground, Sponsor, SlideshowCard, News, Photo, Video,
    SuccessStory, WinnerCategory, Winner
)
from .forms import SubmissionForm

# دالة مساعدة لجلب أو إنشاء البيانات بدون تكرار
def get_or_none(model):
    obj = model.objects.first()
    if not obj:
        obj = model.objects.create()
    return obj

def home(request):
    settings = get_or_none(SiteSetting)
    theme = get_or_none(ThemeSetting)
    content = get_or_none(HomeContent)
    footer = get_or_none(FooterContent)

    fields = Field.objects.all()
    slides = HeroSlide.objects.filter(is_active=True)
    timeline = TimelineEvent.objects.all()
    judges = Judge.objects.all()
    sponsors = Sponsor.objects.all()
    slideshow_cards = SlideshowCard.objects.filter(is_active=True)

    # بناء قاموس خلفيات الأقسام
    section_bgs = {}
    for sb in SectionBackground.objects.all():
        section_bgs[sb.section_id] = sb

    total_submissions = Submission.objects.count()
    accepted_submissions = Submission.objects.filter(status='accepted').count()

    context = {
        'fields': fields,
        'settings': settings,
        'slides': slides,
        'timeline': timeline,
        'judges': judges,
        'sponsors': sponsors,
        'slideshow_cards': slideshow_cards,
        'section_bgs': section_bgs,
        'total_submissions': total_submissions,
        'accepted_submissions': accepted_submissions,
        'theme': theme,      
        'content': content,  
        'footer': footer,  
        'latest_news': News.objects.filter(is_published=True)[:3],        
    }
    return render(request, 'award/home.html', context)


def submit_project(request):
    success_content = get_or_none(SuccessPageContent)
    content = get_or_none(HomeContent)
    settings = get_or_none(SiteSetting)
    theme = get_or_none(ThemeSetting)
    footer = get_or_none(FooterContent)
    
    if request.method == 'POST':
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'award/success.html', {
                'success_content': success_content, 
                'content': content, 
                'settings': settings, 
                'theme': theme,
                'footer': footer
            })
    else:
        form = SubmissionForm()
    
    return render(request, 'award/submit.html', {
        'form': form, 
        'content': content, 
        'settings': settings, 
        'theme': theme,
        'footer': footer
    })


# ===== بيانات مشتركة لكل الصفحات =====
def get_common_context():
    """بيانات مشتركة: شعار، ألوان، فوتر، خلفيات"""
    settings = get_or_none(SiteSetting)
    theme = get_or_none(ThemeSetting)
    footer = get_or_none(FooterContent)
    section_bgs = {}
    for sb in SectionBackground.objects.all():
        section_bgs[sb.section_id] = sb
    return {
        'settings': settings,
        'theme': theme,
        'footer': footer,
        'section_bgs': section_bgs,
    }


# ===== صفحات المركز الإعلامي =====

def news_list(request):
    """صفحة قائمة الأخبار"""
    ctx = get_common_context()
    ctx['all_news'] = News.objects.filter(is_published=True).order_by('-date')
    return render(request, 'award/news_list.html', ctx)

def news_detail(request, pk):
    """صفحة تفاصيل الخبر"""
    ctx = get_common_context()
    ctx['news'] = get_object_or_404(News, pk=pk, is_published=True)
    return render(request, 'award/news_detail.html', ctx)

def photos_page(request):
    """صفحة الصور"""
    ctx = get_common_context()
    ctx['photos'] = Photo.objects.filter(is_active=True).order_by('-created_at')
    return render(request, 'award/photos.html', ctx)

def videos_page(request):
    """مكتبة الفيديو"""
    ctx = get_common_context()
    ctx['videos'] = Video.objects.filter(is_active=True).order_by('order')
    return render(request, 'award/videos.html', ctx)

def success_stories_page(request):
    """قصص النجاح"""
    ctx = get_common_context()
    ctx['stories'] = SuccessStory.objects.filter(is_active=True).order_by('-date')
    return render(request, 'award/success_stories.html', ctx)

def statistics_page(request):
    """صفحة الإحصائيات"""
    ctx = get_common_context()
    ctx['total_submissions'] = Submission.objects.count()
    ctx['accepted_submissions'] = Submission.objects.filter(status='accepted').count()
    return render(request, 'award/statistics.html', ctx)

def winners_page(request):
    """صفحة الفائزون"""
    ctx = get_common_context()
    ctx['categories'] = WinnerCategory.objects.filter(is_active=True).order_by('order')
    return render(request, 'award/winners.html', ctx)
