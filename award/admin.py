from django.contrib import admin
from .models import (
    Field, Track, Submission, SiteSetting, HeroSlide, TimelineEvent,
    Judge, ThemeSetting, HomeContent, FooterContent, SuccessPageContent,
    SectionBackground, Sponsor, FAQ, Winner, MediaGallery, News,
    ContactMessage, TickerItem, SlideshowCard, TickerSetting,
)

@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en')

@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en', 'field')
    list_filter = ('field',)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'project_title', 'status', 'submitted_at')
    list_filter = ('status', 'field')

@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('order', 'media_type', 'is_active')
    list_editable = ('is_active', 'order')

@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'is_highlighted')
    list_editable = ('order', 'is_highlighted')

@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'order')
    list_editable = ('order',)

@admin.register(ThemeSetting)
class ThemeSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not ThemeSetting.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(HomeContent)
class HomeContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not HomeContent.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(FooterContent)
class FooterContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not FooterContent.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(SuccessPageContent)
class SuccessPageContentAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SuccessPageContent.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(SectionBackground)
class SectionBackgroundAdmin(admin.ModelAdmin):
    list_display = ('section_id', 'bg_color', 'is_parallax')
    list_editable = ('is_parallax',)

@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'order')
    list_editable = ('order',)

@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('year', 'school_name', 'rank')

@admin.register(MediaGallery)
class MediaGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'order')
    list_editable = ('order',)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_published')
    list_editable = ('is_published',)

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_editable = ('is_read',)

@admin.register(TickerItem)
class TickerItemAdmin(admin.ModelAdmin):
    list_display = ('message_html', 'is_active', 'order')
    list_editable = ('is_active', 'order')

@admin.register(SlideshowCard)
class SlideshowCardAdmin(admin.ModelAdmin):
    list_display = ('order', 'card_type', 'heading', 'is_active')
    list_filter = ('card_type', 'is_active')
    list_editable = ('order', 'is_active')

@admin.register(TickerSetting)
class TickerSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not TickerSetting.objects.exists()
    def has_delete_permission(self, request, obj=None):
        return False