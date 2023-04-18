# Generated by Django 4.1.7 on 2023-03-31 06:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AddProduct',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('product_title', models.CharField(max_length=200)),
                ('product_image1', models.ImageField(upload_to='')),
                ('product_image2', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_image3', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_image4', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_image5', models.ImageField(blank=True, null=True, upload_to='')),
                ('product_description', models.TextField()),
                ('product_price', models.IntegerField()),
                ('product_buying_cost', models.IntegerField()),
                ('product_address', models.TextField()),
                ('product_category', models.CharField(max_length=100)),
                ('is_create', models.DateField(default=django.utils.timezone.now)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]