# Generated by Django 4.0.3 on 2022-04-11 17:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_hospital_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospital',
            name='user',
        ),
    ]