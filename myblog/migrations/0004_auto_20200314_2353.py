# Generated by Django 3.0.4 on 2020-03-14 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myblog', '0003_auto_20200314_2352'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='slug',
            field=models.SlugField(blank=True, max_length=150),
        ),
    ]
