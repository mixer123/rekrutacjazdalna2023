# Generated by Django 3.2.14 on 2022-09-04 11:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0001_initial'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='klasa',
            name='name_klass',
        ),
    ]
