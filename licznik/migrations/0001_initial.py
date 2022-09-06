# Generated by Django 3.2.14 on 2022-09-06 08:03

import datetime
from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import licznik.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('pesel', models.CharField(help_text='Wymagany', max_length=11, unique=True, validators=[django.core.validators.MinLengthValidator(11), django.core.validators.MaxLengthValidator(11), licznik.models.f_pesel])),
                ('second_name', models.CharField(blank=True, help_text='Opcja', max_length=10, null=True, verbose_name='Drugie imię ')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email adress')),
                ('first_name', models.CharField(help_text='Wymagany', max_length=200, verbose_name='Imię')),
                ('last_name', models.CharField(help_text='Wymagany', max_length=200, verbose_name='Nazwisko')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Ocena',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ocena', models.IntegerField(choices=[(2, 2), (3, 3), (4, 4), (5, 5), (6, 6)], default=2, unique=True)),
                ('punkty', models.IntegerField(default=2)),
            ],
            options={
                'verbose_name': 'Oceny',
                'verbose_name_plural': 'Oceny',
            },
        ),
        migrations.CreateModel(
            name='Oryginal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'Dokumenty',
                'verbose_name_plural': 'Dokumenty',
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('text', models.CharField(max_length=255)),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Data wpisu')),
            ],
        ),
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=100, unique=True, verbose_name='')),
            ],
            options={
                'verbose_name': 'Szkola',
                'verbose_name_plural': 'Szkola',
            },
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datastart', models.DateField(default=datetime.date.today, verbose_name='Data początkowa')),
                ('dataend', models.DateField(default=datetime.date.today, verbose_name='Data końcowa')),
                ('status', models.BooleanField(default=False, verbose_name='status')),
            ],
        ),
        migrations.CreateModel(
            name='Upload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Klasa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='klasa')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='licznik.school')),
            ],
            options={
                'verbose_name': 'Klasa',
                'verbose_name_plural': 'Klasa',
            },
        ),
        migrations.CreateModel(
            name='Kandydat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('internat', models.BooleanField(default=False, verbose_name='Internat')),
                ('j_pol_egz', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='J.polski punkty egzamin')),
                ('mat_egz', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='Matematyka punkty egzamin')),
                ('j_obcy_egz', models.IntegerField(default=0, validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(0)], verbose_name='J.obcy punkty egzamin')),
                ('sw_wyr', models.BooleanField(default=False, verbose_name='Świadectwo z wyróżnieniem')),
                ('konk_ponad_wyr', models.IntegerField(choices=[(0, 0), (5, 5), (7, 7), (10, 10)], default=0, verbose_name='Konkurs ponadwojewódzki')),
                ('konk_woj', models.IntegerField(choices=[(0, 0), (3, 3), (5, 5), (7, 7), (10, 10)], default=0, verbose_name='Konkurs wojewódzki')),
                ('konk_przedm', models.IntegerField(choices=[(0, 0), (3, 3), (4, 4), (10, 10)], default=0, verbose_name='Konkurs przedmiotowy')),
                ('konk_inne', models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)], default=0, verbose_name='Konkursy inne ')),
                ('aktyw_spol', models.IntegerField(choices=[(0, 0), (3, 3)], default=0, verbose_name='Aktywność społeczna')),
                ('suma_pkt', models.DecimalField(decimal_places=2, default=0, editable=False, max_digits=5)),
                ('biol_oc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='biol_oc', to='licznik.ocena', verbose_name='Biologia ocena')),
                ('clas', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='licznik.klasa', verbose_name='Klasa')),
                ('document', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='licznik.oryginal', verbose_name='Dokument')),
                ('inf_oc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inf_oc', to='licznik.ocena', verbose_name='Informatyka ocena')),
                ('j_pol_oc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='j_pol_oc', to='licznik.ocena', verbose_name='J.polski ocena')),
                ('mat_oc', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='mat_oc', to='licznik.ocena', verbose_name='Matematyka ocena')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Kandydat',
                'verbose_name_plural': 'Kandydat',
            },
        ),
    ]
