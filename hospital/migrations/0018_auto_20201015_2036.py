
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0017_auto_20200622_1835'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='doctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='appointment',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='assignedDoctorId',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='patientdischargedetails',
            name='patientId',
            field=models.PositiveIntegerField(null=True),
        ),
    ]
