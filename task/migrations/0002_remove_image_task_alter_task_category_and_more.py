# Generated by Django 4.2 on 2023-04-11 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='task',
        ),
        migrations.AlterField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, choices=[('Urgent and important', 'Urgent and important'), ('Not urgent but important', 'Not urgent but important'), ('Urgent but not important', 'Urgent but not important'), ('Not urgent and not important', 'Not urgent and not important')], default='Urgent and important', max_length=50, null=True, verbose_name='task category'),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
