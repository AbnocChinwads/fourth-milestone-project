# Generated by Django 3.1.7 on 2021-04-11 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_auto_20210313_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='content',
            field=models.TextField(),
        ),
    ]