# Generated by Django 3.2.14 on 2022-10-07 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('licznik', '0016_alter_user_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(help_text='Unikalna nazwa', max_length=30, unique=True, verbose_name='Nazwa użytkownika'),
        ),
    ]