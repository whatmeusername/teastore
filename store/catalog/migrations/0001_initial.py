# Generated by Django 3.2.8 on 2021-10-26 20:24

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=300, unique=True, verbose_name='страна производитель')),
                ('slug', models.CharField(max_length=400, verbose_name='url')),
            ],
            options={
                'verbose_name': 'категория (Страна)',
                'verbose_name_plural': 'Категории (Страна)',
            },
        ),
        migrations.CreateModel(
            name='MainType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='TeaType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(max_length=200, unique=True, verbose_name='тип/вид чая')),
                ('slug', models.CharField(max_length=400, verbose_name='url')),
                ('image', models.ImageField(default='media/NoImageAvailable.png', null=True, upload_to='media/TeaType')),
                ('maintype', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.maintype')),
            ],
            options={
                'verbose_name': 'категория (Тип чая)',
                'verbose_name_plural': 'Категории (Тип чая)',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='название')),
                ('slug', models.SlugField(max_length=200, unique=True, verbose_name='url')),
                ('ProductAvt', models.ImageField(blank=True, upload_to='media/productsAvt/')),
                ('ProductMain', models.ImageField(blank=True, upload_to='media/products/')),
                ('price', models.DecimalField(decimal_places=10, max_digits=20)),
                ('added', models.DateTimeField(default=datetime.datetime.now)),
                ('available', models.BooleanField(default=True)),
                ('TeaType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.teatype', verbose_name='тип/вид чая')),
                ('country', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalog.country', verbose_name='страна производитель')),
            ],
            options={
                'verbose_name': 'товар',
                'verbose_name_plural': 'Товары',
                'ordering': ['-added'],
            },
        ),
        migrations.CreateModel(
            name='description',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriptionKey', models.CharField(max_length=100, verbose_name='характеристика')),
                ('descriptionValue', models.TextField(max_length=400, verbose_name='описание')),
                ('image', models.ImageField(blank=True, upload_to='media/productDescription/')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='item', to='catalog.product')),
            ],
        ),
    ]
