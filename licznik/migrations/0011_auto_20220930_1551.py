# Generated by Django 3.2.14 on 2022-09-30 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0010_auto_20220930_1543'),
    ]

    operations = [
        migrations.RemoveConstraint(
            model_name='user',
            name='unique User',
        ),
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Unikalna nazwa', max_length=30, unique=True, verbose_name='Nazwa użytkownika'),
        ),
        migrations.AddConstraint(
            model_name='user',
            constraint=models.UniqueConstraint(fields=('username',), name='unique User'),
        ),
    ]
