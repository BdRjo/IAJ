from django.contrib import admin
from .models import (
    Field, Track, Submission, SiteSetting, HeroSlide, TimelineEvent,
    Judge, ThemeSetting, HomeContent, FooterContent, SuccessPageContent,
    SectionBackground, Sponsor, FAQ, Winner, MediaGallery, ContactMessage, TickerItem, SlideshowCard, TickerSetting, News, Video, SuccessStory
)


@admin.register(Field)
class FieldAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en')
    list_display_links = ('name_ar',)


@admin.register(Track)
class TrackAdmin(admin.ModelAdmin):
    list_display = ('name_ar', 'name_en', 'field')
    list_filter = ('field',)
    list_display_links = ('name_ar',)


@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('school_name', 'project_title', 'status', 'submitted_at')
    list_filter = ('status', 'field', 'track')
    list_display_links = ('school_name',)
    search_fields = ('school_name', 'project_title', 'email')
    readonly_fields = ('submitted_at',)


@admin.register(SiteSetting)
class SiteSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not SiteSetting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(HeroSlide)
class HeroSlideAdmin(admin.ModelAdmin):
    list_display = ('media_type', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('media_type',)


@admin.register(TimelineEvent)
class TimelineEventAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_highlighted')
    list_editable = ('order', 'is_highlighted')
    list_display_links = ('title',)


@admin.register(Judge)
class JudgeAdmin(admin.ModelAdmin):
    list_display = ('name', 'title', 'order')
    list_editable = ('order',)
    list_display_links = ('name',)


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
    list_display_links = ('section_id',)


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):
    list_display = ('name', 'tier', 'order')
    list_editable = ('order',)
    list_display_links = ('name',)


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ('question', 'order')
    list_editable = ('order',)
    list_display_links = ('question',)


@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('year', 'school_name', 'rank')
    list_display_links = ('school_name',)


@admin.register(MediaGallery)
class MediaGalleryAdmin(admin.ModelAdmin):
    list_display = ('title', 'media_type', 'order')
    list_editable = ('order',)
    list_display_links = ('title',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_published')
    list_editable = ('is_published',)
    list_display_links = ('title',)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'is_read', 'created_at')
    list_editable = ('is_read',)
    list_display_links = ('name',)


@admin.register(TickerItem)
class TickerItemAdmin(admin.ModelAdmin):
    list_display = ('message_html', 'is_active', 'order')
    list_editable = ('is_active', 'order')
    list_display_links = ('message_html',)


@admin.register(SlideshowCard)
class SlideshowCardAdmin(admin.ModelAdmin):
    list_display = ('card_type', 'order', 'heading', 'is_active')
    list_filter = ('card_type', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('card_type',)


@admin.register(TickerSetting)
class TickerSettingAdmin(admin.ModelAdmin):
    def has_add_permission(self, request):
        return not TickerSetting.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False 
# ====================================================
# أضف هذا بنهاية award/admin.py
# ====================================================

@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ('title', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('title',)
    search_fields = ('title',)

@admin.register(SuccessStory)
class SuccessStoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'is_active')
    list_editable = ('is_active',)
    list_display_links = ('title',)
    search_fields = ('title',)
