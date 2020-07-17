# Generated by Django 3.0.6 on 2020-07-15 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('anaviuser', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Searcher',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='anaviuser.User')),
            ],
            bases=('anaviuser.user',),
        ),
    ]
