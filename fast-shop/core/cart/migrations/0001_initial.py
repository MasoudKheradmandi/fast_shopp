# Generated by Django 4.2.3 on 2023-09-05 10:32

import cart.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("account", "0005_alter_profile_phone_number"),
        ("product", "0005_wishlist"),
    ]

    operations = [
        migrations.CreateModel(
            name="Order",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("first_name", models.CharField(blank=True, max_length=250, null=True)),
                ("last_name", models.CharField(blank=True, max_length=250, null=True)),
                ("address", models.TextField(blank=True, null=True)),
                (
                    "phone_number",
                    models.CharField(
                        blank=True,
                        max_length=15,
                        null=True,
                        validators=[cart.models.validate_phone_number],
                    ),
                ),
                ("zip_code", models.CharField(max_length=30, null=True)),
                ("national_code", models.CharField(max_length=10, null=True)),
                (
                    "paid_amount",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=8, null=True
                    ),
                ),
                ("is_paid", models.BooleanField(default=False)),
                (
                    "stripe_token",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
                ("payment_date", models.DateTimeField(blank=True, null=True)),
                (
                    "profile",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="account.profile",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="OrderItem",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "price",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=8, null=True
                    ),
                ),
                ("quantity", models.IntegerField()),
                (
                    "order",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="cart.order"
                    ),
                ),
                (
                    "product",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="product.product",
                    ),
                ),
            ],
        ),
    ]