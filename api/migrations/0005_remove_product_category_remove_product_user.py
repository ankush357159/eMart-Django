# Generated by Django 4.0.1 on 2022-01-24 17:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_review_ratings'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='category',
        ),
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
