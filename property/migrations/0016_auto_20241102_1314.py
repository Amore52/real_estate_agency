from django.db import migrations

def make_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats_to_update = []

    for flat in Flat.objects.iterator():
        owner, created = Owner.objects.get_or_create(
            user=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone
        )
        owner.flats.add(flat)
        flats_to_update.append(flat)

        if len(flats_to_update) >= 1000:
            Owner.objects.bulk_update(flats_to_update, ['owners_phonenumber', 'owner_pure_phone'])
            flats_to_update = []

    if flats_to_update:
        Owner.objects.bulk_update(flats_to_update, ['owners_phonenumber', 'owner_pure_phone'])

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0015_auto_20241102_1254'),
    ]

    operations = [
        migrations.RunPython(make_owner)
    ]
