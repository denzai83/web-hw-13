# Generated by Django 4.2 on 2023-04-22 19:58

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("quotes", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="quote",
            name="quote",
            field=models.TextField(),
        ),
    ]
