# Generated by Django 4.0 on 2022-04-17 21:00

from Project import storage
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nickname', models.CharField(error_messages={'unique': 'This nickname already exists.'}, max_length=50, null=True, unique=True, verbose_name='Nick', blank=True)),
                ('bio', models.TextField(null=True, verbose_name='Bio', blank=True)),
                ('image', models.ImageField(null=True, upload_to=storage.image_file_upload, verbose_name='Profile image', blank=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update date')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to='Users.user')),
            ],
        ),
    ]
