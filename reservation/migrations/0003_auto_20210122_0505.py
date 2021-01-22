# Generated by Django 3.1.3 on 2021-01-22 05:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0002_auto_20201204_1609'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservation',
            name='adult',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='child',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservation',
            name='infant',
            field=models.CharField(default=0, max_length=10),
            preserve_default=False,
        ),
    ]