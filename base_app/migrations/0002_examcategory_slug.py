# Generated by Django 4.1.5 on 2023-01-13 19:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base_app", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="examcategory",
            name="slug",
            field=models.SlugField(max_length=150, null=True),
        ),
    ]
