# Generated by Django 4.2.3 on 2023-09-02 14:27

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account", "0002_remove_profile_description_profile_phone_number_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="national_code",
            field=models.CharField(max_length=10, null=True),
        ),
    ]