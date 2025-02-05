# Generated by Django 5.1.5 on 2025-01-26 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('stock', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=200)),
                ('size', models.CharField(choices=[('XS', 'Extra Small'), ('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=2)),
                ('color', models.CharField(max_length=50)),
                ('material', models.CharField(blank=True, max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='dresses/')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
