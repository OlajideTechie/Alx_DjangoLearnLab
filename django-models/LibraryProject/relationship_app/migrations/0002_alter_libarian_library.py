# Generated by Django 5.1.2 on 2024-11-08 14:38

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("relationship_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="libarian",
            name="library",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="relationship_app.library",
            ),
        ),
    ]
