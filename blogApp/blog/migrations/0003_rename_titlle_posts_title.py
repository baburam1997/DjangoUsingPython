# Generated by Django 3.2.4 on 2021-06-19 07:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_posts_author'),
    ]

    operations = [
        migrations.RenameField(
            model_name='posts',
            old_name='titlle',
            new_name='title',
        ),
    ]
