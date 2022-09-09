# Generated by Django 3.2.7 on 2022-09-09 10:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=60, unique=True)),
                ('username', models.CharField(default='', max_length=30, unique=True)),
                ('signup_date', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='User_profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_type', models.CharField(default='User', max_length=12)),
                ('profile_pic', models.ImageField(default='deafult_profile_pic.jpeg', upload_to='user/profile_image')),
                ('country_code', models.CharField(max_length=10)),
                ('phone_number', models.CharField(max_length=15)),
                ('address', models.CharField(max_length=15)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='User', to='Users.user')),
            ],
        ),
    ]
