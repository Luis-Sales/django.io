# Generated by Django 5.0.2 on 2024-02-20 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todos", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo",
            name="deadline",
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name="todo",
            name="finshed_at",
            field=models.DateField(null=True),
        ),
    ]
