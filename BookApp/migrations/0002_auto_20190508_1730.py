# Generated by Django 2.2.1 on 2019-05-08 09:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('BookApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='heroinfo',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='BookApp.BookInfo'),
        ),
    ]