# Generated by Django 3.2 on 2023-04-12 09:49

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='confirmation_code',
            field=models.CharField(
                blank=True, max_length=50, verbose_name='Код для регистрации'
            ),
        ),
        migrations.AlterField(
            model_name='user',
            name='is_active',
            field=models.BooleanField(
                default=False,
                help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.',
                verbose_name='active',
            ),
        ),
    ]