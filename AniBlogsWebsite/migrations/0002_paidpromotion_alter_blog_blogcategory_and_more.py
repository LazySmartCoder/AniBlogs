# Generated by Django 5.0.1 on 2024-02-26 13:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("AniBlogsWebsite", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="PaidPromotion",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("CompanyName", models.CharField(default="", max_length=500)),
                ("Banner", models.CharField(default="", max_length=5000)),
            ],
        ),
        migrations.AlterField(
            model_name="blog",
            name="BlogCategory",
            field=models.CharField(
                choices=[
                    ("Top Trends", "Top Trends"),
                    ("Stock Market", "Stock Market"),
                    ("Shark Tank India", "Shark Tank India"),
                    ("Technology", "Technology"),
                    ("Good Reads", "Good Reads"),
                    ("Python", "Python"),
                    ("Business News", "Business News"),
                ],
                default="",
                max_length=100,
            ),
        ),
        migrations.AlterField(
            model_name="blogcomment",
            name="Date",
            field=models.CharField(default="2024-02-26 19:28:13.415775", max_length=40),
        ),
        migrations.AlterField(
            model_name="contactdetail",
            name="Date_added",
            field=models.CharField(default="2024-02-26 19:28:13.415775", max_length=40),
        ),
    ]
