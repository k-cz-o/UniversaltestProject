# Generated by Django 4.0.4 on 2022-05-14 21:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excel', '0005_alter_uploadfile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfile',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
