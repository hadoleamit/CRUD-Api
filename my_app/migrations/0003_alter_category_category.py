# Generated by Django 3.2.5 on 2021-07-02 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_category_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(choices=[('CLOTHS', 'Cloths'), ('VEGITABLE', 'Vegitable'), ('BOOK', 'Book')], max_length=100),
        ),
    ]