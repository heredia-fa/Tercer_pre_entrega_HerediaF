# Generated by Django 5.0.6 on 2024-06-02 18:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Taverna', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='favotire_game',
            new_name='favorite_game',
        ),
    ]