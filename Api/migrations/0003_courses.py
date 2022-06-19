# Generated by Django 4.0.4 on 2022-04-15 16:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0002_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Courses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=70)),
                ('Year', models.DateTimeField(auto_now=True)),
                ('teacher_id', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Api.teacher')),
            ],
        ),
    ]