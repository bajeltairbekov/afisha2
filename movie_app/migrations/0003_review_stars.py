# Generated by Django 5.1.5 on 2025-01-25 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie_app', '0002_rename_derector_director'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='stars',
            field=models.ImageField(choices=[(1, '1'), (2, '2'), (3, '3'), ('4', 4), ('5', 5)], default=1, upload_to=''),
        ),
    ]
