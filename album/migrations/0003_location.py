# Generated by Django 3.2.5 on 2021-07-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_category'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]
