# Generated by Django 3.1.5 on 2021-02-06 17:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_homesection_deeplink_path'),
    ]

    operations = [
        migrations.AddField(
            model_name='homesectionitem',
            name='type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
