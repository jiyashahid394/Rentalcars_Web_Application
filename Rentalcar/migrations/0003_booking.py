# Generated by Django 4.2.3 on 2023-08-08 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_msg_contact_message'),
    ]

    operations = [
        migrations.CreateModel(
            name='booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=122)),
                ('email', models.CharField(max_length=122)),
                ('number', models.CharField(max_length=12)),
                ('fdate', models.DateField()),
                ('tdate', models.DateField()),
            ],
        ),
    ]
