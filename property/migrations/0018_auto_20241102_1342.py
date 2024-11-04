from django.db import migrations

def link_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    flats_to_update = []

    for flat in Flat.objects.iterator():
        owner, created = Owner.objects.get_or_create(
            user=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,
        )
        flat.owners.add(owner)

        flats_to_update.append(flat)

        # Если достигли лимита, обновляем все в bulk
        if len(flats_to_update) >= 1000:
            Flat.objects.bulk_update(flats_to_update, [])
            flats_to_update = []

    if flats_to_update:
        Flat.objects.bulk_update(flats_to_update, [])

class Migration(migrations.Migration):
    dependencies = [
        ('property', '0017_auto_20241102_1339'),
    ]

    operations = [
        migrations.RunPython(link_flats_to_owners)
    ]
