# Generated by Django 3.2.14 on 2022-10-07 13:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0018_remove_user_unique user'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username',), name='unique User'),
        ),
    ]
