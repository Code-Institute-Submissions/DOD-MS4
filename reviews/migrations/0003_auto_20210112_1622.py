# Generated by Django 3.1.2 on 2021-01-12 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0002_auto_20210112_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_body',
            field=models.TextField(default='', max_length=600),
        ),
    ]
