# Generated by Django 4.2.1 on 2023-06-13 19:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_scope_is_main'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-published_at'], 'verbose_name': 'Статья', 'verbose_name_plural': 'Статьи'},
        ),
    ]