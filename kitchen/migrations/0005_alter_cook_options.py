# Generated by Django 5.0.3 on 2024-04-08 21:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("kitchen", "0004_alter_dishtype_options_alter_dish_cooks_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="cook",
            options={"ordering": ("first_name", "last_name")},
        ),
    ]
