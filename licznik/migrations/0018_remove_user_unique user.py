# Generated by Django 3.2.14 on 2022-10-07 12:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0017_alter_user_username'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='unique User',
        ),
    ]
