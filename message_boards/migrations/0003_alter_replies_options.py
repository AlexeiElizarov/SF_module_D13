# Generated by Django 4.0.4 on 2022-07-07 05:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message_boards', '0002_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='replies',
            options={'ordering': ['-id']},
        ),
    ]