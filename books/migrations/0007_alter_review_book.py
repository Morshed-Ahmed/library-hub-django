# Generated by Django 4.2.7 on 2024-01-02 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0006_borrowed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
