# Generated by Django 5.0.1 on 2024-04-20 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "AniBlogsWebsite",
            "0010_alter_blog_blogcategory_alter_blogcomment_actualdate_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogcomment",
            name="Date",
            field=models.CharField(default="2024-04-20 22:50:12.047856", max_length=40),
        ),
    ]