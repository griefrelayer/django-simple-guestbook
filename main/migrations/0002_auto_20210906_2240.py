# Generated by Django 3.2.6 on 2021-09-06 19:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='messages',
            name='datetime_created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='messages',
            name='email',
            field=models.EmailField(max_length=50),
        ),
    ]
