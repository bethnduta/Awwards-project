# Generated by Django 3.2.10 on 2022-06-18 20:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('share', '0004_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='flower.jpg', upload_to=''),
        ),
    ]