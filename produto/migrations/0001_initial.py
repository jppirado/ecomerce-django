# Generated by Django 4.1 on 2022-08-19 19:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('carrosapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_product', models.CharField(max_length=70)),
                ('quantity_product', models.IntegerField()),
                ('fornecedor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='carrosapp.supplier')),
            ],
        ),
    ]
