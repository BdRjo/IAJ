# ====================================================
# أضف هذه الموديلات بنهاية award/models.py
# ====================================================

# ===== معرض الصور =====
class Photo(models.Model):
    title = models.CharField(max_length=255, verbose_name="العنوان")
    image = models.FileField(upload_to='photos/', verbose_name="الصورة")
    description = models.TextField(blank=True, verbose_name="الوصف")
    is_active = models.BooleanField(default=True, verbose_name="مفعّل")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "صورة"
        verbose_name_plural = "معرض الصور"
        ordering = ['-created_at']

    def __str__(self):
        return self.title


# ===== مكتبة الفيديو =====
class Video(models.Model):
    title = models.CharField(max_length=255, verbose_name="العنوان")
    youtube_url = models.URLField(verbose_name="رابط يوتيوب")
    description = models.TextField(blank=True, verbose_name="الوصف")
    order = models.IntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="مفعّل")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "فيديو"
        verbose_name_plural = "مكتبة الفيديو"
        ordering = ['order']

    def __str__(self):
        return self.title

    def get_embed_url(self):
        """تحويل رابط يوتيوب إلى embed URL"""
        url = self.youtube_url
        if 'watch?v=' in url:
            video_id = url.split('watch?v=')[-1].split('&')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        elif 'youtu.be/' in url:
            video_id = url.split('youtu.be/')[-1].split('?')[0]
            return f'https://www.youtube.com/embed/{video_id}'
        return url


# ===== قصص النجاح =====
class SuccessStory(models.Model):
    title = models.CharField(max_length=255, verbose_name="العنوان")
    content = models.TextField(verbose_name="النص")
    image = models.FileField(upload_to='success_stories/', blank=True, verbose_name="الصورة")
    date = models.DateField(verbose_name="التاريخ")
    is_active = models.BooleanField(default=True, verbose_name="مفعّل")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "قصة نجاح"
        verbose_name_plural = "قصص النجاح"
        ordering = ['-date']

    def __str__(self):
        return self.title


# ===== فئات الفوز =====
class WinnerCategory(models.Model):
    name = models.CharField(max_length=255, verbose_name="اسم الفئة")
    description = models.TextField(blank=True, verbose_name="الوصف")
    order = models.IntegerField(default=0, verbose_name="الترتيب")
    is_active = models.BooleanField(default=True, verbose_name="مفعّل")

    class Meta:
        verbose_name = "فئة فوز"
        verbose_name_plural = "فئات الفوز"
        ordering = ['order']

    def __str__(self):
        return self.name


# ===== الفائزون =====
class Winner(models.Model):
    category = models.ForeignKey(WinnerCategory, on_delete=models.CASCADE, related_name='winners', verbose_name="الفئة")
    name = models.CharField(max_length=255, verbose_name="اسم الفائز")
    school = models.CharField(max_length=255, blank=True, verbose_name="المدرسة")
    description = models.TextField(blank=True, verbose_name="نبذة")
    image = models.FileField(upload_to='winners/', blank=True, verbose_name="الصورة")
    year = models.CharField(max_length=4, blank=True, verbose_name="السنة")
    is_active = models.BooleanField(default=True, verbose_name="مفعّل")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "فائز"
        verbose_name_plural = "الفائزون"
        ordering = ['category__order', '-year']

    def __str__(self):
        return self.name
