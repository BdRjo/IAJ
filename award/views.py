from django.shortcuts import render, redirect
from .models import (
    Field, SiteSetting, HeroSlide, TimelineEvent, Judge, Submission,
    ThemeSetting, HomeContent, FooterContent, SuccessPageContent,
    SectionBackground, Sponsor, SlideshowCard
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
        'latest_news': NewsItem.objects.filter(is_active=True)[:3],        
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
