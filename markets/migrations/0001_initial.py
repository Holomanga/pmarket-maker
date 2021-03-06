# Generated by Django 3.0.5 on 2020-04-19 21:52

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Market',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('desc', models.TextField(blank=True)),
                ('rules', models.TextField(blank=True)),
                ('curated', models.BooleanField(default=False)),
                ('creationdate', models.DateTimeField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('closed', models.BooleanField(default=False)),
                ('resolveprice', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('tag', models.SlugField(blank=True)),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.Market')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('price', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('creationdate', models.DateTimeField()),
                ('buyer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='boughtIn', to=settings.AUTH_USER_MODEL)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.Option')),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='soldIn', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-creationdate'],
            },
        ),
        migrations.CreateModel(
            name='SellOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('minPrice', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('maxNumber', models.IntegerField(default=0)),
                ('creationdate', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.Option')),
            ],
            options={
                'ordering': ['minPrice', '-creationdate'],
            },
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.FloatField()),
                ('market', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.Market')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BuyOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('maxPrice', models.DecimalField(decimal_places=3, default=0, max_digits=6)),
                ('maxNumber', models.IntegerField(default=0)),
                ('creationdate', models.DateTimeField()),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('option', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='markets.Option')),
            ],
            options={
                'ordering': ['-maxPrice', '-creationdate'],
            },
        ),
    ]
