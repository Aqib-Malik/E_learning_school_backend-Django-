# Generated by Django 4.0.4 on 2022-05-24 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0032_alter_assignmenttwo_submit_file'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=500)),
                ('Email', models.TextField()),
                ('Subject', models.CharField(max_length=500)),
                ('Message', models.CharField(max_length=500)),
            ],
        ),
    ]
