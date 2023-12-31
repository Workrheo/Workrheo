# Generated by Django 4.2.5 on 2023-10-26 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_name', models.CharField(max_length=100, null=True)),
                ('project_category', models.IntegerField(choices=[(1, 'New home interiors'), (2, 'Renovation interiors')])),
                ('project_type', models.IntegerField(choices=[(1, '1BHK Apartment'), (2, '2BHK Apartment'), (3, '3BHK Apartment'), (4, '4BHK Apartment'), (5, '5BHK Apartment'), (6, 'Villa'), (7, 'Individual Apartment')])),
                ('kitchen_finish', models.IntegerField(choices=[(1, 'Laminate_Glossy'), (2, 'Laminate_Matt'), (3, 'Acrylic'), (4, 'PU/DUCO'), (5, 'Laminate_Glossy and Laminate_Matt'), (6, 'Laminate_Glossy and Acrylic'), (7, 'Acrylic and PU/DUCO'), (8, 'NA')])),
                ('kitchen_countertop', models.IntegerField(choices=[(1, 'Grantite'), (2, 'Quartz'), (3, 'NA')])),
                ('kitchen_dado', models.IntegerField(choices=[(1, 'Tiles'), (2, 'Quartz'), (3, 'NA')])),
                ('kitchen_loft', models.IntegerField(choices=[(1, 'REQUIRED'), (2, 'NOT REQUIRED')])),
                ('utility', models.IntegerField(choices=[(1, 'Wall unit'), (2, 'Base unit'), (3, 'Both Base and Wall unit'), (4, 'NA')])),
                ('MBR_Wardrobe', models.IntegerField(choices=[(1, 'Sliding Wardrobe'), (2, 'Openable Wardrobe'), (3, 'Sliding Wardrobe with Loft'), (4, 'Openable Wardrobe with Loft'), (5, 'NA')])),
                ('MBR_COT', models.IntegerField(choices=[(1, 'King Size'), (2, 'Queen Size'), (3, 'NA')])),
                ('MBR_Reqs', models.IntegerField(choices=[(1, 'Chest Of Drawer'), (2, 'Dresser'), (3, 'Bay Window'), (4, 'Dresser ,  Chest Of Drawer'), (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'), (6, 'Bay window ,  Dresser ,  Study , Wallpaper'), (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'), (8, 'NA')])),
                ('GBR_Wardrobe', models.IntegerField(choices=[(1, 'Sliding Wardrobe'), (2, 'Openable Wardrobe'), (3, 'Sliding Wardrobe with Loft'), (4, 'Openable Wardrobe with Loft'), (5, 'NA')])),
                ('GBR_COT', models.IntegerField(choices=[(1, 'King Size'), (2, 'Queen Size'), (3, 'NA')])),
                ('GBR_Reqs', models.IntegerField(choices=[(1, 'Chest Of Drawer'), (2, 'Dresser'), (3, 'Bay Window'), (4, 'Dresser ,  Chest Of Drawer'), (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'), (6, 'Bay window ,  Dresser ,  Study , Wallpaper'), (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'), (8, 'NA')])),
                ('KBR_Wardrobe', models.IntegerField(choices=[(1, 'Sliding Wardrobe'), (2, 'Openable Wardrobe'), (3, 'Sliding Wardrobe with Loft'), (4, 'Openable Wardrobe with Loft'), (5, 'NA')])),
                ('KBR_COT', models.IntegerField(choices=[(1, 'King Size'), (2, 'Queen Size'), (3, 'NA')])),
                ('KBR_Reqs', models.IntegerField(choices=[(1, 'Chest Of Drawer'), (2, 'Dresser'), (3, 'Bay Window'), (4, 'Dresser ,  Chest Of Drawer'), (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'), (6, 'Bay window ,  Dresser ,  Study , Wallpaper'), (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'), (8, 'NA')])),
                ('Four_BR_Wardrobe', models.IntegerField(choices=[(1, 'Sliding Wardrobe'), (2, 'Openable Wardrobe'), (3, 'Sliding Wardrobe with Loft'), (4, 'Openable Wardrobe with Loft'), (5, 'NA')])),
                ('Four_BR_COT', models.IntegerField(choices=[(1, 'King Size'), (2, 'Queen Size'), (3, 'NA')])),
                ('Four_BR_Reqs', models.IntegerField(choices=[(1, 'Chest Of Drawer'), (2, 'Dresser'), (3, 'Bay Window'), (4, 'Dresser ,  Chest Of Drawer'), (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'), (6, 'Bay window ,  Dresser ,  Study , Wallpaper'), (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'), (8, 'NA')])),
                ('Five_BR_Wardrobe', models.IntegerField(choices=[(1, 'Sliding Wardrobe'), (2, 'Openable Wardrobe'), (3, 'Sliding Wardrobe with Loft'), (4, 'Openable Wardrobe with Loft'), (5, 'NA')])),
                ('Five_BR_COT', models.IntegerField(choices=[(1, 'King Size'), (2, 'Queen Size'), (3, 'NA')])),
                ('Five_BR_Reqs', models.IntegerField(choices=[(1, 'Chest Of Drawer'), (2, 'Dresser'), (3, 'Bay Window'), (4, 'Dresser ,  Chest Of Drawer'), (5, 'Bay window ,Chest Of Drawer ,Dresser and Study'), (6, 'Bay window ,  Dresser ,  Study , Wallpaper'), (7, 'Bay window ,  Dresser ,  Study , Wallpaper, Painting'), (8, 'NA')])),
                ('Livingroom', models.IntegerField(choices=[(1, 'TV unit'), (2, 'TV unit, Partition'), (3, 'TV unit, Partition, False ceiling'), (4, 'TV unit, Partition, False ceiling, Wallpaper'), (5, 'TV unit, Partition, False ceiling, Wallpaper, Wall Panelling'), (6, 'TV unit, Partition, False ceiling, Wallpaper, Wall Panelling, Sofa'), (7, 'TV unit, Partition, False ceiling, Wallpaper, Wall Panelling, Sofa, Centre Table'), (8, 'TV unit, Partition, False ceiling, Wallpaper, Wall Panelling, Sofa, Centre Table, Curtains'), (9, 'NA')])),
                ('Diningroom', models.IntegerField(choices=[(1, 'Crockery Unit'), (2, 'Crockery Unit, False ceiling'), (3, 'Crockery Unit, False ceiling, Dining table & Chairs'), (4, 'Crockery Unit, False ceiling, Dining table & Chairs, Partition'), (5, 'Crockery Unit, False ceiling, Dining table & Chairs, Partition, Wallpaper'), (6, 'Crockery Unit, False ceiling, Dining table & Chairs, Partition, Wallpaper, Curtains'), (7, 'NA')])),
                ('Washroom', models.IntegerField(choices=[(1, 'Vanity'), (2, 'Vanity, Shower Partition'), (3, 'Vanity, Shower Partition, Mirror '), (4, 'NA')])),
                ('Foyer', models.IntegerField(choices=[(1, 'Shoe rack'), (2, 'Shoe rack, Foyer unit'), (3, 'Shoe rack, Foyer unit, Wallpaper'), (4, 'Shoe rack, Foyer unit, Wallpaper, Wall panelling'), (5, 'Shoe rack, Foyer unit, Wallpaper, Wall panelling, False ceiling'), (6, 'NA')])),
                ('Requirements', models.TextField(null=True)),
                ('floor_plan', models.ImageField(blank=True, null=True, upload_to='users/floorplan')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_checklist', to=settings.AUTH_USER_MODEL)),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designer_checklist', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('a_date', models.DateField(null=True)),
                ('a_timing', models.TimeField(null=True)),
                ('status', models.CharField(max_length=100, null=True)),
                ('c_status', models.CharField(max_length=100, null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='customer_appointments', to=settings.AUTH_USER_MODEL)),
                ('designer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='designer_appointments', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
