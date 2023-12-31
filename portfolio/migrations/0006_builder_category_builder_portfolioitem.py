# Generated by Django 4.2.5 on 2023-12-02 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('builder', '0001_initial'),
        ('portfolio', '0005_architect_portfolioitem_description_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Builder_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
                ('property_name', models.CharField(blank=True, max_length=50, null=True)),
                ('project_image', models.ImageField(blank=True, null=True, upload_to='foodimages')),
                ('project_created_at', models.DateField(blank=True, null=True)),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('description', models.TextField(blank=True, max_length=250)),
                ('project_budget', models.PositiveIntegerField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('builder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.builder')),
            ],
            options={
                'verbose_name': 'Builder_Category',
                'verbose_name_plural': 'Builder_categories',
            },
        ),
        migrations.CreateModel(
            name='Builder_PortfolioItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='foodimages')),
                ('price', models.PositiveBigIntegerField(blank=True, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('is_available', models.BooleanField(default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('builder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='builder.builder')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='architect_portfolioitems', to='portfolio.builder_category')),
            ],
        ),
    ]
