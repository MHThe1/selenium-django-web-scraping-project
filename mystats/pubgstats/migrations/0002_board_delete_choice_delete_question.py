# Generated by Django 4.2.5 on 2023-10-04 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubgstats', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('passw', models.CharField(max_length=100)),
            ],
        ),
        migrations.DeleteModel(
            name='Choice',
        ),
        migrations.DeleteModel(
            name='Question',
        ),
    ]
