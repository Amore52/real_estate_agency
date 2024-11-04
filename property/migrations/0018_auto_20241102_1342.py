# Generated by Django 2.2.24 on 2024-11-02 10:42

from django.db import migrations

def link_flats_to_owners(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        owner, created = Owner.objects.get_or_create(
            user=flat.owner,
            owners_phonenumber=flat.owners_phonenumber,
            owner_pure_phone=flat.owner_pure_phone,
        )
        flat.owners.add(owner)

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0017_auto_20241102_1339'),
    ]

    operations = [
        migrations.RunPython(link_flats_to_owners)
    ]
