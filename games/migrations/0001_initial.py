# Generated by Django 5.1.2 on 2024-10-30 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game_name', models.CharField(max_length=100)),
                ('game_platform', models.CharField(choices=[('Playstation 3', 'Ps3'), ('Playstation 4', 'Ps4'), ('Playstation 5', 'Ps5'), ('Steam', 'Pc')], default='Steam', max_length=100)),
                ('game_status', models.CharField(choices=[('Backlogged', 'Backlogged'), ('Waitlist', 'Waitlist'), ('Playing', 'Playing'), ('Post-Game', 'Post'), ('Finished', 'Finished')], default='Playing', max_length=100)),
                ('game_completion_percentage', models.IntegerField()),
                ('hours_played', models.IntegerField()),
                ('game_completed', models.BooleanField()),
                ('game_image_path', models.CharField(max_length=250)),
                ('created_time', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_time', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
