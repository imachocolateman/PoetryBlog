# Generated by Django 4.0.3 on 2022-03-02 15:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='last_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
