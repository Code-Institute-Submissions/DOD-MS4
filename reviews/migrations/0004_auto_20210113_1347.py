# Generated by Django 3.1.2 on 2021-01-13 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0003_auto_20210112_1622'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='review_rating',
            field=models.CharField(choices=[('1', '1 - Star'), ('2', '2 - Star'), ('3', '3 - Star'), ('4', '4 - Star'), ('5', '5 - Star')], default=0, max_length=1),
        ),
    ]
