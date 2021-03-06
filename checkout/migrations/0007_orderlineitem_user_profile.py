# Generated by Django 3.1.2 on 2021-01-13 13:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_userprofile_default_full_name'),
        ('checkout', '0006_order_user_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderlineitem',
            name='user_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='lineorders', to='profiles.userprofile'),
        ),
    ]
