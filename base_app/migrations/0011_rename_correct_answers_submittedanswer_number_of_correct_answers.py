# Generated by Django 4.1.5 on 2023-01-17 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("base_app", "0010_alter_submittedanswer_correct_answers"),
    ]

    operations = [
        migrations.RenameField(
            model_name="submittedanswer",
            old_name="correct_answers",
            new_name="number_of_correct_answers",
        ),
    ]
