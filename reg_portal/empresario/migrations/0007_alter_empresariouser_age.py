# Generated by Django 4.2.2 on 2023-07-04 09:01

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("empresario", "0006_alter_empresariouser_profile_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="empresariouser",
            name="age",
            field=models.IntegerField(null=True),
        ),
    ]
