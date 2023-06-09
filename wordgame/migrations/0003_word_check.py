# Generated by Django 4.1.7 on 2023-03-20 20:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wordgame', '0002_button_letter'),
    ]

    operations = [
        migrations.CreateModel(
            name='word_check',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=20)),
                ('isValid', models.BooleanField()),
                ('pointsValue', models.IntegerField()),
            ],
        ),
    ]
