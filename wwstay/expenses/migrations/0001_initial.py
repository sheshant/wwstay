# Generated by Django 2.0 on 2018-08-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Expense',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('publication_date', models.DateField(blank=True, null=True)),
                ('author', models.CharField(blank=True, max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('pages', models.IntegerField(blank=True, null=True)),
                ('image', models.ImageField(default=None, null=True, upload_to='pic_folder/')),
                ('book_type', models.PositiveSmallIntegerField(blank=True, choices=[(1, 'Hardcover'), (2, 'Paperback'), (3, 'E-book')], null=True)),
            ],
        ),
    ]