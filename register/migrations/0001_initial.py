# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-18 12:02
from __future__ import unicode_literals

import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.ASCIIUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nickname', models.CharField(default='', max_length=16, verbose_name='\u6635\u79f0')),
                ('gender', models.CharField(choices=[('MALE', 'male'), ('FEMALE', 'female'), ('SECRET', 'secret')], default='SECRET', max_length=6, null=True, verbose_name='\u6027\u522b')),
                ('kind', models.CharField(choices=[('A', 'Individual'), ('B', 'Individual_plus'), ('C', 'Station'), ('D', 'Station_plus')], max_length=1, verbose_name='\u7528\u6237\u7c7b\u578b')),
                ('phone', models.CharField(max_length=20, verbose_name='\u8054\u7cfb\u7535\u8bdd')),
                ('introduce', models.CharField(blank=True, max_length=100, null=True, verbose_name='\u4ecb\u7ecd')),
                ('adress', models.CharField(blank=True, max_length=45, null=True, verbose_name='\u5730\u5740')),
                ('icon', models.ImageField(default='user_icon/default.png', upload_to='user_icon/%Y/%M', verbose_name='\u5934\u50cf')),
                ('photo', models.ImageField(default='user_photo/default.jpg', upload_to='user_photo/%Y/%M', verbose_name='\u76f8\u518c')),
                ('creditrating', models.IntegerField(default=60, verbose_name='\u4fe1\u8a89\u8bc4\u5206')),
                ('likes', models.IntegerField(default=0, verbose_name='\u9876')),
                ('dislikes', models.IntegerField(default=0, verbose_name='\u8e29')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': '\u7528\u6237\u4fe1\u606f',
                'verbose_name_plural': '\u7528\u6237\u4fe1\u606f',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]