# Generated by Django 3.1.7 on 2021-02-26 02:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='discription',
            field=models.CharField(default='', max_length=250),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]
