# Generated by Django 4.1 on 2022-09-04 06:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_teacher_id'),
        ('info', '0005_alter_course_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='AttendanceTotal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accounts.student')),
            ],
            options={
                'unique_together': {('student', 'course')},
            },
        ),
    ]
