from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0012_contactmessage_faq_mediagallery_news_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tickeritem',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='ticker/', verbose_name='لوغو (اختياري)'),
        ),
    ]
