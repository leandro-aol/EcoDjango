# Generated by Django 2.1.1 on 2018-09-05 21:05

import django.contrib.auth.models
import django.core.validators
from django.db import migrations, models
import re


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0009_alter_user_last_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(help_text='Um nome curto que será usado para identificá-lo de forma única na plataforma', max_length=30, unique=True, validators=[django.core.validators.RegexValidator(re.compile('^[\\w.@+-_]+$'), 'Informe um nome de usuário válido.Este valor deve conter apenas letras, números e os caracteres: @/./+/-/_', 'invalid')], verbose_name='Usuário')),
                ('name', models.CharField(blank=True, max_length=100, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='E-mail')),
                ('is_staff', models.BooleanField(default=False, verbose_name='Equipe')),
                ('is_active', models.BooleanField(default=True, verbose_name='Ativo')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='Data de Entrada')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'Usuário',
                'verbose_name_plural': 'Usuários',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]