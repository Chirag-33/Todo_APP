# Generated by Django 4.2.7 on 2024-12-10 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Todo', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='Title',
            field=models.CharField(max_length=50),
        ),
    ]
