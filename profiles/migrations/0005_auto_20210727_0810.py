# Generated by Django 3.2.5 on 2021-07-27 06:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_relationship'),
    ]

    operations = [
        migrations.AlterField(
            model_name='relationship',
            name='receiver',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='receiver', to='profiles.profile'),
        ),
        migrations.AlterField(
            model_name='relationship',
            name='senders',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sender', to='profiles.profile'),
        ),
    ]
