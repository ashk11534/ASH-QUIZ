# Generated by Django 4.1.5 on 2023-01-17 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("base_app", "0015_alter_exam_participants"),
    ]

    operations = [
        migrations.AddField(
            model_name="submittedanswer",
            name="exam",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="base_app.exam",
            ),
        ),
    ]
