# Generated by Django 5.0.1 on 2024-02-27 06:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AniBlogsWebsite", "0005_alter_blogcomment_date_and_more"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ContactDetail",
        ),
        migrations.AlterField(
            model_name="blogcomment",
            name="Date",
            field=models.CharField(default="2024-02-27 12:21:55.129426", max_length=40),
        ),
    ]
