# Generated by Django 4.2.5 on 2023-10-26 10:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='checklist',
            name='designer',
        ),
    ]
