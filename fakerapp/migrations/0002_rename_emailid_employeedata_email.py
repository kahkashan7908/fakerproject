# Generated by Django 4.1 on 2023-04-11 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fakerapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employeedata',
            old_name='emailid',
            new_name='email',
        ),
    ]
