# Generated by Django 5.0.7 on 2024-08-05 23:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("desafioadl", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="SubTarea",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("descripcion", models.TextField(default="")),
                ("eliminada", models.BooleanField(default=False)),
                (
                    "tarea",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="subtareas",
                        to="desafioadl.tarea",
                    ),
                ),
            ],
        ),
    ]
