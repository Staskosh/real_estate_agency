# Generated by Django 2.2.24 on 2022-02-26 16:57

from django.db import migrations


import phonenumbers


def format_phonenumbers(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flat = Flat.objects.get(owner='г-н. Мамонтов Давыд Фадеевич')
    flat.owners_phonenumber = '+70000000000'
    flat.save()
    for flat in Flat.objects.all():
        parsed_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        if phonenumbers.is_valid_number(parsed_number) is True:
            formated_number = phonenumbers.format_number(parsed_number, phonenumbers.PhoneNumberFormat.E164)
            flat.owner_pure_phone = formated_number
            flat.save()


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0008_auto_20220226_1940'),
    ]

    operations = [
        migrations.RunPython(format_phonenumbers),
    ]
