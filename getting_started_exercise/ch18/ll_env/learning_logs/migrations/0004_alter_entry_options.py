# Generated by Django 5.1.3 on 2024-11-15 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0003_alter_entry_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='entry',
            options={'verbose_name_plural': 'entries'},
        ),
    ]