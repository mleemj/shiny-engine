# Generated by Django 2.1.5 on 2019-04-24 18:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [("blog", "0004_auto_20190423_2345")]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="blogger",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to=settings.AUTH_USER_MODEL,
            ),
        )
    ]