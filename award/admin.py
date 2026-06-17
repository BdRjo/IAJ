from django.contrib import admin
from .models import (
    Field, Track, Submission, SiteSetting, HeroSlide, TimelineEvent, 
    Judge, ThemeSetting, HomeContent, FooterContent, SuccessPageContent,
    SectionBackground, Sponsor, FAQ, Winner, MediaGallery, News, ContactMessage,
    TickerItem, TickerSetting
)

class TrackInline(admin.TabularInline):
    model = Track
    extra = 1

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    inlines = [TrackInline]
    list_display = ('name_ar', 'name_en')

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'field', 'track', 'status', 'submitted_at')
    list_filter = ('status', 'field', 'track')
    search_fields = ('school_name', 'project_title')

admin.site.register(SiteSetting)
admin.site.register(HeroSlide)
admin.site.register(TimelineEvent)
admin.site.register(Judge)
admin.site.register(ThemeSetting)
admin.site.register(HomeContent)
admin.site.register(FooterContent)
admin.site.register(SuccessPageContent)

# === الموديلات الجديدة ===
admin.site.register(SectionBackground)
admin.site.register(Sponsor)
admin.site.register(FAQ)
admin.site.register(Winner)
admin.site.register(MediaGallery)
admin.site.register(News)
admin.site.register(ContactMessage)
admin.site.register(TickerItem)
admin.site.register(TickerSetting)