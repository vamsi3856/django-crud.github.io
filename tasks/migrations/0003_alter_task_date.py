# Generated by Django 4.0.6 on 2022-11-17 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0002_task_date_task_timestramp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='date',
            field=models.DateField(blank=True, null=True, verbose_name='(mm/dd/yy)'),
        ),
    ]
