# Generated by Django 4.2.3 on 2023-07-08 06:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0002_alter_authors_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='authors',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
    ]
