# Generated by Django 4.1 on 2022-08-16 21:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_todos_name_post'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Post',
        ),
    ]