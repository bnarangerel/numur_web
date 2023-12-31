# Generated by Django 4.2.4 on 2023-09-21 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_slide_img_url'),
    ]

    operations = [
        migrations.RenameField(
            model_name='loan_type',
            old_name='title',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='loan_type',
            name='loan_amount',
        ),
        migrations.RemoveField(
            model_name='loan_type',
            name='loan_fee',
        ),
        migrations.RemoveField(
            model_name='loan_type',
            name='loan_interest',
        ),
        migrations.RemoveField(
            model_name='loan_type',
            name='loan_term',
        ),
        migrations.AddField(
            model_name='loan_type',
            name='img_caption',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='loan_type',
            name='img_url',
            field=models.ImageField(default='path_to_default_image.jpg', upload_to='images/icons/loan_type/%y/'),
        ),
        migrations.AddField(
            model_name='loan_type',
            name='url',
            field=models.CharField(default='http://127.0.0.1:8000/', max_length=200),
        ),
    ]
