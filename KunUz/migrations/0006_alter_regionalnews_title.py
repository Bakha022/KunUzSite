# Generated by Django 4.2 on 2023-05-16 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KunUz', '0005_alter_regionalnews_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionalnews',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
