# Generated by Django 3.2.14 on 2022-09-04 11:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0002_remove_klasa_name_klass'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='klasa',
            unique_together=set(),
        ),
    ]