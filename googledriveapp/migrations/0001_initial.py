# Generated by Django 3.2.2 on 2022-10-22 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filetitle', models.CharField(max_length=50)),
                ('file', models.FileField(upload_to='Files')),
            ],
        ),
        migrations.CreateModel(
            name='Folder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('foldername', models.CharField(max_length=50)),
                ('folderdesc', models.CharField(max_length=255)),
            ],
        ),
    ]