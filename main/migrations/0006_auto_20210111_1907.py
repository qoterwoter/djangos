# Generated by Django 3.1.5 on 2021-01-11 16:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_studentslessons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='studentslessons',
            old_name='lessons',
            new_name='lesson',
        ),
    ]
