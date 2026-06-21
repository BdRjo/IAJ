from django.shortcuts import render, redirect
from .models import (
    Field, SiteSetting, HeroSlide, TimelineEvent, Judge, Submission,
    ThemeSetting, HomeContent, FooterContent, SuccessPageContent,
    SectionBackground, Sponsor, SlideshowCard, News
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
    latest_news = News.objects.filter(is_published=True).order_by('-date')[:3]
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
        'latest_news': latest_news,
        'section_bgs': section_bgs,
        'total_submissions': total_submissions,
        'accepted_submissions': accepted_submissions,
        'theme': theme,      
        'content': content,  
        'footer': footer,   
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


def get_base_context():
    """context مشترك بين كل الصفحات"""
    from award.models import TickerItem, TickerSetting
    return {
        'settings': get_or_none(SiteSetting),
        'theme': get_or_none(ThemeSetting),
        'footer': get_or_none(FooterContent),
        'content': get_or_none(HomeContent),
    }


def news_list(request):
    news = News.objects.filter(is_published=True).order_by('-date')
    ctx = get_base_context()
    ctx['news_list'] = news
    return render(request, 'award/news_list.html', ctx)


def news_detail(request, pk):
    from django.shortcuts import get_object_or_404
    article = get_object_or_404(News, pk=pk, is_published=True)
    ctx = get_base_context()
    ctx['article'] = article
    return render(request, 'award/news_detail.html', ctx)
