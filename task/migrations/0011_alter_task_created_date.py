# Generated by Django 4.2 on 2023-04-15 21:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_alter_task_created_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='created_date',
            field=models.DateField(auto_now_add=True),
        ),
    ]
