# Generated by Django 4.2.3 on 2023-08-30 11:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="footerdepthtwo",
            name="name",
            field=models.CharField(max_length=450, verbose_name="نام"),
        ),
    ]
