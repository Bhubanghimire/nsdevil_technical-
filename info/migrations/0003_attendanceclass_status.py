# Generated by Django 4.1 on 2022-09-04 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_alter_studentcourse_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='attendanceclass',
            name='status',
            field=models.IntegerField(default=0),
        ),
    ]