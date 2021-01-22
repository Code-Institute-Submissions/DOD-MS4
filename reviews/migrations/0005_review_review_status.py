# Generated by Django 3.1.2 on 2021-01-22 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0004_auto_20210113_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='review_status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Rejected', 'Rejected'), ('Approved', 'Approved')], default=0, max_length=10),
        ),
    ]
