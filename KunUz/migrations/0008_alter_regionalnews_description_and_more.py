# Generated by Django 4.2 on 2023-05-22 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KunUz', '0007_rename_text_regionalnews_articels_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionalnews',
            name='description',
            field=models.CharField(blank=True, max_length=10000, null=True),
        ),
        migrations.AlterField(
            model_name='regionalnews',
            name='title',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]