# Generated by Django 3.0.6 on 2020-07-15 07:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('hotel', '0001_initial'),
        ('anaviexpert', '0001_initial'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField()),
                ('state', models.BooleanField(default=False)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('hotel', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='hotel.Hotel')),
                ('website', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='website.WebSite')),
            ],
        ),
        migrations.CreateModel(
            name='ExpertComment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(auto_now_add=True)),
                ('comment', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='comment.Comment')),
                ('expert', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='anaviexpert.Expert')),
            ],
        ),
    ]
