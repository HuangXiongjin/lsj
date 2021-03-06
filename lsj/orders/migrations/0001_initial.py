# Generated by Django 2.1.13 on 2019-12-16 08:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('no', models.CharField(max_length=512)),
                ('detail', models.CharField(max_length=1024, null=True)),
                ('pay_status', models.IntegerField(default=0)),
                ('create_time', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.User')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderGoods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('goods_num', models.IntegerField(default=1)),
                ('goods', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='goods.Goods')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order')),
            ],
            options={
                'db_table': 'goods_order',
            },
        ),
    ]
