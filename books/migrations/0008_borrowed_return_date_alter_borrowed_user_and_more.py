# Generated by Django 4.2.7 on 2024-01-02 13:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0007_alter_review_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='borrowed',
            name='return_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='borrowed',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='review',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='books.book'),
        ),
    ]
