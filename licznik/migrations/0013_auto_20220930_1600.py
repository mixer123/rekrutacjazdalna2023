# Generated by Django 3.2.14 on 2022-09-30 16:00

import django.core.validators
from django.db import migrations, models
import licznik.models


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0012_auto_20220930_1553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(help_text='Wymagany', max_length=254, unique=True, verbose_name='email adress'),
        ),
        migrations.AlterField(
            model_name='user',
            name='pesel',
            field=models.CharField(help_text='Wymagany', max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11), licznik.models.f_pesel]),
        ),
    ]
