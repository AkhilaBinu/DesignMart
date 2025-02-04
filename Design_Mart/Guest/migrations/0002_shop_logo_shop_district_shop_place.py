# Generated by Django 5.1.5 on 2025-01-20 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='Logo',
            field=models.ImageField(default=1, upload_to='Shop_logo/'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='district',
            field=models.CharField(choices=[('ernakulam', 'Ernakulam'), ('kollam', 'Kollam'), ('idukki', 'Idukki')], default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='shop',
            name='place',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
