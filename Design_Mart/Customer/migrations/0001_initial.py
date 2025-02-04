# Generated by Django 5.1.5 on 2025-01-22 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='adddesign',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('discription', models.TextField(blank=True, null=True)),
                ('price', models.TextField(blank=True, null=True)),
                ('design_pic', models.ImageField(upload_to='design/')),
            ],
        ),
    ]
