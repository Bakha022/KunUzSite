# Generated by Django 4.2 on 2023-05-16 09:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KunUz', '0004_regionalnews_descriptation_regionalnews_newstypes_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='regionalnews',
            name='summary',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
