# Generated by Django 3.1.5 on 2021-02-08 19:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homesectionitem_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homesection',
            name='title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]