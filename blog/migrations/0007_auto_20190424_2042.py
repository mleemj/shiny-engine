# Generated by Django 2.1.5 on 2019-04-24 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("blog", "0006_blogcomment")]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="description",
            field=models.TextField(
                help_text="Enter your blog text here", max_length=2000
            ),
        )
    ]