# Generated by Django 4.0.3 on 2022-03-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='favorite',
            field=models.BooleanField(default=False),
        ),
    ]
