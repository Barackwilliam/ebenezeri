# Generated by Django 5.1.6 on 2025-02-25 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0003_service'),
    ]

    operations = [
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=255)),
                ('message', models.TextField()),
            ],
        ),
    ]
