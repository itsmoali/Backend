# Generated by Django 4.2.5 on 2023-11-20 11:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GPT_API', '0002_courses_ne_field'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courses',
            name='ne_field',
        ),
    ]