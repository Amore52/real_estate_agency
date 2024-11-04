import phonenumbers
from django.db import migrations

def make_new_number(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats_to_update = []

    for flat in Flat.objects.iterator():
        phone_number = phonenumbers.parse(flat.owners_phonenumber, 'RU')
        flat.owner_pure_phone = phonenumbers.format_number(phone_number, phonenumbers.PhoneNumberFormat.E164)
        flats_to_update.append(flat)

        if len(flats_to_update) >= 1000:
            Flat.objects.bulk_update(flats_to_update, ['owner_pure_phone'])
            flats_to_update = []

    if flats_to_update:
        Flat.objects.bulk_update(flats_to_update, ['owner_pure_phone'])

def move_backward(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    flats_to_update = []

    for flat in Flat.objects.iterator():
        flat.owner_pure_phone = None
        flats_to_update.append(flat)

        if len(flats_to_update) >= 1000:
            Flat.objects.bulk_update(flats_to_update, ['owner_pure_phone'])
            flats_to_update = []

    if flats_to_update:
        Flat.objects.bulk_update(flats_to_update, ['owner_pure_phone'])

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0010_flat_owner_pure_phone'),
    ]

    operations = [
        migrations.RunPython(make_new_number, move_backward)
    ]
