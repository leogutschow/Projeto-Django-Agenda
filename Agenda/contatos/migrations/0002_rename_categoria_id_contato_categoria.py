# Generated by Django 3.2.9 on 2021-11-18 12:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contatos', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contato',
            old_name='categoria_id',
            new_name='categoria',
        ),
    ]
