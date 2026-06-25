from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('award', '0022_photo_winnercategory_delete_newsitem_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            [
                "ALTER TABLE award_sectionbackground ADD COLUMN IF NOT EXISTS heading_color varchar(7) DEFAULT '';",
                "ALTER TABLE award_sectionbackground ADD COLUMN IF NOT EXISTS heading_size varchar(7) DEFAULT '';",
                "ALTER TABLE award_sectionbackground ADD COLUMN IF NOT EXISTS text_color varchar(7) DEFAULT '';",
                "ALTER TABLE award_sectionbackground ADD COLUMN IF NOT EXISTS text_size varchar(7) DEFAULT '';",
                "ALTER TABLE award_sectionbackground ADD COLUMN IF NOT EXISTS sub_heading_color varchar(7) DEFAULT '';",
                "ALTER TABLE award_sectionbackground ADD COLUMN IF NOT EXISTS sub_heading_size varchar(7) DEFAULT '';",
                "ALTER TABLE award_sectionbackground ADD COLUMN IF NOT EXISTS gold_line_color varchar(7) DEFAULT '';",
            ],
            reverse_sql=[
                "ALTER TABLE award_sectionbackground DROP COLUMN IF EXISTS heading_color;",
                "ALTER TABLE award_sectionbackground DROP COLUMN IF EXISTS heading_size;",
                "ALTER TABLE award_sectionbackground DROP COLUMN IF EXISTS text_color;",
                "ALTER TABLE award_sectionbackground DROP COLUMN IF EXISTS text_size;",
                "ALTER TABLE award_sectionbackground DROP COLUMN IF EXISTS sub_heading_color;",
                "ALTER TABLE award_sectionbackground DROP COLUMN IF EXISTS sub_heading_size;",
                "ALTER TABLE award_sectionbackground DROP COLUMN IF EXISTS gold_line_color;",
            ]
        )
    ]