# Generated by Django 3.2.23 on 2024-04-16 13:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_trainingmodel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TrainingModel',
        ),
        migrations.RemoveField(
            model_name='user',
            name='is_contestant',
        ),
    ]