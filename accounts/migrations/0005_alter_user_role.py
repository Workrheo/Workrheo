# Generated by Django 4.2.5 on 2023-12-02 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Designer'), (2, 'Customer'), (3, 'Architect'), (4, 'Builder')], null=True),
        ),
    ]
