from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0023_add_section_color_fields'),
    ]

    operations = [
        migrations.AddField(
            model_name='slideshowcard',
            name='image_url',
            field=models.URLField(blank=True, null=True, verbose_name='رابط صورة خارجي', help_text='ألصق رابط صورة من Cloudinary أو Google Drive أو أي مصدر'),
        ),
    ]