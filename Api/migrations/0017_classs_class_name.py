# Generated by Django 4.0.4 on 2022-04-18 13:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Api', '0016_stu_sub_teach_classs'),
    ]

    operations = [
        migrations.AddField(
            model_name='classs',
            name='class_name',
            field=models.CharField(default=43, max_length=70),
            preserve_default=False,
        ),
    ]