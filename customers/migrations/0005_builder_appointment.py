# Generated by Django 4.2.5 on 2023-12-02 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('customers', '0004_architect_appointment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Builder_Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.DateField(null=True)),
                ('a_timing', models.TimeField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('c_status', models.CharField(max_length=100, null=True)),
                ('builder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='builder_appointments', to=settings.AUTH_USER_MODEL)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_builder_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
