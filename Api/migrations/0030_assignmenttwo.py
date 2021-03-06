# Generated by Django 4.0.4 on 2022-05-24 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0029_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='Assignmenttwo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(null=True, upload_to='')),
                ('Teacher_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.teacher')),
                ('classs', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.classes')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Api.courses')),
            ],
        ),
    ]
