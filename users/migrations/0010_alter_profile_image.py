# Generated by Django 4.1.6 on 2023-04-06 09:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_profile_phone_alter_profile_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='image',
            field=models.ImageField(default="{% static 'images/cart.png' %}", upload_to='static/user_images'),
        ),
    ]
