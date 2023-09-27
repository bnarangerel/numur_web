# Generated by Django 4.2.4 on 2023-09-22 02:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0012_alter_loan_type_icon'),
    ]

    operations = [
        migrations.CreateModel(
            name='Merchant',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('merchant_name', models.CharField(max_length=200)),
                ('merchant_phone_number', models.CharField(max_length=8)),
                ('fb_url', models.CharField(default='', max_length=200)),
                ('merchant_logo', models.ImageField(default='path_to_default_image.jpg', upload_to='images/merchant/%y/')),
            ],
        ),
        migrations.RenameField(
            model_name='loan_type',
            old_name='description',
            new_name='loan_description',
        ),
        migrations.RenameField(
            model_name='loan_type',
            old_name='name',
            new_name='loan_name',
        ),
        migrations.RenameField(
            model_name='loan_type',
            old_name='url',
            new_name='loan_page_url',
        ),
    ]