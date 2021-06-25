# Generated by Django 3.2.4 on 2021-06-25 16:37

import ModelFormsApp.register_app.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BookModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)])),
                ('pages', models.IntegerField(default=0, validators=[ModelFormsApp.register_app.models.pages_positive_not_zero_validator])),
                ('description', models.CharField(default='', max_length=100, validators=[django.core.validators.MaxLengthValidator(100)])),
                ('author', models.CharField(max_length=20, validators=[django.core.validators.MaxLengthValidator(20)])),
            ],
        ),
    ]
