# ====================================================
# أضف هذا بنهاية award/admin.py
# ====================================================

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'is_active')
    list_editable = ('is_active',)
    list_display_links = ('title',)
    search_fields = ('title',)

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

@admin.register(WinnerCategory)
class WinnerCategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'order', 'is_active')
    list_editable = ('order', 'is_active')
    list_display_links = ('name',)

@admin.register(Winner)
class WinnerAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'year', 'school', 'is_active')
    list_editable = ('is_active',)
    list_display_links = ('name',)
    list_filter = ('category', 'year')
    search_fields = ('name', 'school')
