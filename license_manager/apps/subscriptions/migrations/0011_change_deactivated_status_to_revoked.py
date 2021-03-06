# Generated by Django 2.2.15 on 2020-08-27 12:38

from django.db import migrations, models

from license_manager.apps.subscriptions.constants import (
    DEACTIVATED,
    REVOKED,
)


def flip_deactivated_to_revoked(apps, schema_editor):
    """
    Change all licenses with a status of `DEACTIVATED` to have a status of `REVOKED`.
    """
    License = apps.get_model('subscriptions', 'License')
    License.objects.filter(status=DEACTIVATED).update(status=REVOKED)


class Migration(migrations.Migration):

    dependencies = [
        ('subscriptions', '0010_add_assigned_date_revoked_date_to_license'),
    ]

    operations = [
        migrations.AlterField(
            model_name='historicallicense',
            name='status',
            field=models.CharField(choices=[('activated', 'Activated'), ('assigned', 'Assigned'), ('unassigned', 'Unassigned'), ('revoked', 'Revoked')], default='unassigned', help_text='The status fields has the following options and definitions:\nActive: A license which has been created, assigned to a learner, and the learner has activated the license. The license also must not have expired.\nAssigned: A license which has been created and assigned to a learner, but which has not yet been activated by that learner.\nUnassigned: A license which has been created but does not have a learner assigned to it.\nRevoked: A license which has been created but is no longer active (intentionally revoked or has expired). A license in this state may or may not have a learner assigned.', max_length=25),
        ),
        migrations.AlterField(
            model_name='license',
            name='status',
            field=models.CharField(choices=[('activated', 'Activated'), ('assigned', 'Assigned'), ('unassigned', 'Unassigned'), ('revoked', 'Revoked')], default='unassigned', help_text='The status fields has the following options and definitions:\nActive: A license which has been created, assigned to a learner, and the learner has activated the license. The license also must not have expired.\nAssigned: A license which has been created and assigned to a learner, but which has not yet been activated by that learner.\nUnassigned: A license which has been created but does not have a learner assigned to it.\nRevoked: A license which has been created but is no longer active (intentionally revoked or has expired). A license in this state may or may not have a learner assigned.', max_length=25),
        ),
        # There is no reverse function as we can't flip the status back to Deactivated as it's no longer a valid choice
        migrations.RunPython(flip_deactivated_to_revoked, migrations.RunPython.noop),
    ]
