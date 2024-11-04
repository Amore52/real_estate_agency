from django.db import migrations
from django.db.models import Case, When, BooleanField

def make_new_building(app, schema_editor):
    Flat = app.get_model('property', 'Flat')
    Flat.objects.update(
        new_building=Case(
            When(construction_year__gte=2015, then=True),
            When(construction_year__lt=2015, then=False),
            default=False,
            output_field=BooleanField(),
        )
    )

class Migration(migrations.Migration):

    dependencies = [
        ('property', '0003_flat_new_building'),
    ]

    operations = [
        migrations.RunPython(make_new_building)
    ]
