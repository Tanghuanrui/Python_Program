# Generated by Django 2.2.7 on 2021-06-21 05:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=32)),
                ('price', models.DecimalField(decimal_places=2, default=10.01, max_digits=5)),
                ('inventory', models.IntegerField(verbose_name='库存数')),
                ('sale_num', models.IntegerField(verbose_name='卖出数')),
                ('publisher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Publisher')),
            ],
        ),
    ]
