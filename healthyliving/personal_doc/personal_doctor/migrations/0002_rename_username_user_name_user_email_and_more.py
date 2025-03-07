# Generated by Django 5.1.4 on 2025-01-23 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal_doctor', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='username',
            new_name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='email',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.CharField(max_length=128, null=True),
        ),
    ]
