# Generated by Django 2.1.13 on 2019-12-16 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_no', models.CharField(max_length=512)),
                ('type_name', models.CharField(max_length=128)),
                ('child_type_name', models.CharField(default='全部分类:0', max_length=512)),
                ('type_sort', models.IntegerField(default=1)),
            ],
            options={
                'db_table': 'food_type',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_no', models.CharField(max_length=128, unique=True)),
                ('goods_name', models.CharField(max_length=128, unique=True)),
                ('goods_img', models.CharField(max_length=512, null=True)),
                ('price', models.FloatField(default=0)),
                ('unit', models.CharField(max_length=32, null=True)),
                ('goods_type_name', models.CharField(max_length=128, null=True)),
                ('childid', models.CharField(max_length=128)),
                ('total', models.IntegerField(default=0)),
                ('sale_num', models.IntegerField(default=0)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.FoodType')),
            ],
            options={
                'db_table': 'goods',
            },
        ),
        migrations.CreateModel(
            name='MainNav',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('img', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'main_nav',
            },
        ),
        migrations.CreateModel(
            name='MainShow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('img', models.CharField(max_length=512)),
                ('product_no', models.CharField(max_length=128, unique=True)),
                ('product_name', models.CharField(max_length=128, unique=True)),
                ('price', models.FloatField(default=0)),
                ('unit', models.CharField(max_length=32, null=True)),
            ],
            options={
                'db_table': 'main_show',
            },
        ),
        migrations.CreateModel(
            name='MainWheel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128)),
                ('img', models.CharField(max_length=512)),
            ],
            options={
                'db_table': 'main_wheel',
            },
        ),
    ]
