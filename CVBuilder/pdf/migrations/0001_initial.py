# Generated by Django 5.0.6 on 2024-06-28 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(max_length=200)),
                ('phone', models.CharField(max_length=13)),
                ('summary', models.TextField(max_length=2000)),
                ('degree', models.CharField(max_length=200)),
                ('school', models.CharField(max_length=200)),
                ('university', models.CharField(max_length=200)),
                ('previous_work', models.TextField(max_length=200)),
                ('skills', models.TextField(max_length=1000)),
            ],
        ),
    ]