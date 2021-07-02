# Generated by Django 3.2.5 on 2021-07-02 16:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0003_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='category',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='album.category'),
        ),
        migrations.AddField(
            model_name='image',
            name='location',
            field=models.ForeignKey(default='0', on_delete=django.db.models.deletion.CASCADE, to='album.location'),
        ),
    ]
