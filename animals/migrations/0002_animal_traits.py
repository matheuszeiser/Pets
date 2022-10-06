# Generated by Django 4.1.2 on 2022-10-06 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("traits", "0002_remove_trait_animals"),
        ("animals", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="animal",
            name="traits",
            field=models.ManyToManyField(related_name="animals", to="traits.trait"),
        ),
    ]