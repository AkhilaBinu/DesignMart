# Generated by Django 5.1.5 on 2025-01-17 08:11

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop_name', models.CharField(max_length=100)),
                ('owner_name', models.CharField(max_length=100)),
                ('contact_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('address', models.TextField()),
                ('date_joined', models.DateTimeField(auto_now_add=True)),
                ('password', models.CharField(max_length=100)),
                ('proof', models.ImageField(upload_to='Shop_proof/')),
            ],
        ),
    ]
