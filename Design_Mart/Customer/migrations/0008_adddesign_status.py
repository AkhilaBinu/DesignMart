# Generated by Django 5.1.5 on 2025-01-26 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customer', '0007_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='adddesign',
            name='status',
            field=models.CharField(default='pending', max_length=10),
        ),
    ]
