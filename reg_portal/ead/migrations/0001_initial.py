# Generated by Django 4.1.7 on 2023-06-27 16:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('landingPage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EADUser',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('mobile', models.CharField(max_length=15)),
                ('college_name', models.CharField(max_length=255)),
                ('ead_city', models.CharField(choices=[('hyderabad', 'Hyderabad'), ('chennai', 'Chennai'), ('kochi', 'Kochi')], max_length=255)),
            ],
        ),
    ]
