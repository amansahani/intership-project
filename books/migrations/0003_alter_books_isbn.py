# Generated by Django 4.2.3 on 2023-09-10 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_rename_img_urls_books_img_url1_books_img_url2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='isbn',
            field=models.CharField(max_length=100),
        ),
    ]
