# Generated by Django 4.1.7 on 2023-03-13 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0005_region_district'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
            ],
        ),
    ]
