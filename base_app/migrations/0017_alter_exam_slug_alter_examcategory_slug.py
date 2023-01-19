# Generated by Django 4.1.5 on 2023-01-18 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("base_app", "0016_submittedanswer_exam"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam",
            name="slug",
            field=models.SlugField(max_length=400, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="examcategory",
            name="slug",
            field=models.SlugField(max_length=150, null=True, unique=True),
        ),
    ]