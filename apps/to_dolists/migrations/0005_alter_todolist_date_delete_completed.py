# Generated by Django 4.1.5 on 2023-01-22 12:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_dolists', '0004_completed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.DeleteModel(
            name='Completed',
        ),
    ]
