# Generated by Django 4.2.7 on 2023-11-14 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CLoom_app_1', '0003_userdetails_bio_userdetails_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetails',
            name='profile_pic',
            field=models.ImageField(default='https://mdbootstrap.com/img/Photos/Others/placeholder-avatar.jpg', upload_to=''),
        ),
    ]
