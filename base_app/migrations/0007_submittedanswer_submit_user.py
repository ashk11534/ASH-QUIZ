# Generated by Django 4.1.5 on 2023-01-17 11:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("base_app", "0006_submittedanswer_rename_option_correctanswer_option"),
    ]

    operations = [
        migrations.AddField(
            model_name="submittedanswer",
            name="submit_user",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
