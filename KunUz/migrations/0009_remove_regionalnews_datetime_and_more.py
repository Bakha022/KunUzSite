# Generated by Django 4.2 on 2023-05-23 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('KunUz', '0008_alter_regionalnews_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='regionalnews',
            name='dateTime',
        ),
        migrations.AddField(
            model_name='regionalnews',
            name='create_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
