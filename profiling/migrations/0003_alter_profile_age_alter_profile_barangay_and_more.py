# Generated by Django 4.0.4 on 2022-04-23 12:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0002_alter_profile_civil_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='age',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='barangay',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='birthday',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='civil_status',
            field=models.CharField(blank=True, choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced'), ('Separated', 'Separated'), ('Annulled', 'Annulled'), ('Unknown', 'Unknown'), ('Live-in', 'Live-in')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='contact_number',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='educational_background',
            field=models.CharField(blank=True, choices=[('Elementary Level', 'Elementary Level'), ('Elementary Graduate', 'Elementary Graduate'), ('High School Level', 'High School Level'), ('High School Graduate', 'High School Graduate'), ('Vocational Graduate', 'Vocational Graduate'), ('College Level', 'College Level'), ('College Graduate', 'College Graduate'), ('Masters Level', 'Masters Level'), ('Masters Graduate', 'Masters Graduate'), ('Doctorate Level', 'Doctorate Level'), ('Doctorate Graduate', 'Doctorate Graduate')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='municipality',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='national_voter',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='province',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='purok',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='region',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sk_voter',
            field=models.CharField(blank=True, choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='suffix',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_status',
            field=models.CharField(blank=True, choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Self-Employed', 'Self-Employed'), ('Currently Looking For a Job', 'Currently Looking For a Job'), ('Not interested Looking for a Job', 'Not interested Looking for a Job')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='youth_age_group',
            field=models.CharField(blank=True, choices=[('Child Youth', 'Child Youth (15-17 yrs. old)'), ('Core Youth', 'Core Youth (18-24 yrs. old)'), ('Young Adult', 'Young Adult (25-30 yrs. old)')], max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='youth_classification',
            field=models.CharField(blank=True, choices=[('In School Youth', 'In School Youth'), ('Out of School youth', 'Out of School youth'), ('Working Youth', 'Working Youth'), ('Person with Disability', 'Youth With Special Needs - PWD'), ('Children in Conflict with Law', 'Youth With Special Needs - CCL'), ('Indigenous People', 'Youth With Special Needs - IP')], max_length=250, null=True),
        ),
    ]
