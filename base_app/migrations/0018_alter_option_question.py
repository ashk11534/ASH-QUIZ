# Generated by Django 4.1.5 on 2023-01-19 02:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base_app", "0017_alter_exam_slug_alter_examcategory_slug"),
    ]

    operations = [
        migrations.AlterField(
            model_name="option",
            name="question",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base_app.question",
            ),
        ),
    ]