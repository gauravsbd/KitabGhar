# Generated by Django 4.1.9 on 2023-08-16 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userinfomodel',
            name='Address',
            field=models.CharField(max_length=50),
        ),
    ]
