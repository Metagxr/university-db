# Generated by Django 3.2.3 on 2021-05-19 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dbmanage', '0002_auto_20210316_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='teacher_name',
            field=models.CharField(max_length=255, verbose_name='ФИО'),
        ),
    ]
