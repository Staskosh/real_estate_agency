# Generated by Django 2.2.24 on 2022-03-02 09:10

from django.db import migrations


def fill_owner_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for owner in Owner.objects.all():
        flats = Flat.objects.filter(owner=owner.owner)
        print(owner.owner)
        owner.owned_flat.set(flats)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20220228_1003'),
    ]

    operations = [
        migrations.RunPython(fill_owner_flats),
    ]
