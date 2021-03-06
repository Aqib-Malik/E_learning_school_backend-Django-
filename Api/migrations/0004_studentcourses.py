# Generated by Django 4.0.4 on 2022-04-15 16:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0003_courses'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentCourses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=70)),
                ('course_id', models.ManyToManyField(to='Api.courses')),
                ('student_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.student')),
            ],
        ),
    ]
