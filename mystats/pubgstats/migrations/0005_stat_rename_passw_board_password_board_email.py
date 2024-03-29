# Generated by Django 4.2.5 on 2023-10-04 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pubgstats', '0004_board_last_link'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent_id', models.PositiveSmallIntegerField()),
                ('ign', models.CharField(max_length=30)),
                ('matches', models.PositiveSmallIntegerField()),
                ('kills', models.PositiveSmallIntegerField()),
                ('damage', models.PositiveSmallIntegerField()),
                ('knocks', models.PositiveSmallIntegerField()),
                ('assists', models.PositiveSmallIntegerField()),
                ('longest', models.PositiveSmallIntegerField()),
                ('travel', models.PositiveSmallIntegerField()),
                ('revives', models.PositiveSmallIntegerField()),
                ('accuracy', models.PositiveSmallIntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='board',
            old_name='passw',
            new_name='password',
        ),
        migrations.AddField(
            model_name='board',
            name='email',
            field=models.EmailField(default='defaultmail@gg.gg', max_length=254),
            preserve_default=False,
        ),
    ]
