# Generated by Django 4.0.3 on 2022-03-08 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='email',
            field=models.EmailField(default='#', max_length=254),
        ),
    ]
