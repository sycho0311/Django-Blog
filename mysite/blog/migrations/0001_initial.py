# Generated by Django 2.2.8 on 2019-12-21 07:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='TITLE')),
                ('slug', models.SlugField(allow_unicode=True, help_text='one word for title alias.', unique=True, verbose_name='SLUG')),
                ('description', models.CharField(blank=True, help_text='simple description text.', max_length=255, verbose_name='DESCRIPTION')),
                ('content', models.TextField(verbose_name='CONTENT')),
                ('create_dt', models.DateTimeField(auto_now_add=True, verbose_name='CREATE DATE')),
                ('modify_dt', models.DateTimeField(auto_now=True, verbose_name='MODIFY DATE')),
            ],
            options={
                'verbose_name': 'blogPost',
                'verbose_name_plural': 'blogPosts',
                'db_table': 'blogPosts',
                'ordering': ['-modify_dt'],
            },
        ),
    ]
