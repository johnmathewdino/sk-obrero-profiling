# Generated by Django 4.0.4 on 2022-04-23 11:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiling', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='civil_status',
            field=models.CharField(choices=[('Single', 'Single'), ('Married', 'Married'), ('Widowed', 'Widowed'), ('Divorced', 'Divorced'), ('Separated', 'Separated'), ('Annulled', 'Annulled'), ('Unknown', 'Unknown'), ('Live-n', 'Live-n')], max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='educational_background',
            field=models.CharField(choices=[('Elementary Level', 'Elementary Level'), ('Elementary Graduate', 'Elementary Graduate'), ('High School Level', 'High School Level'), ('High School Graduate', 'High School Graduate'), ('Vocational Graduate', 'Vocational Graduate'), ('College Level', 'College Level'), ('College Graduate', 'College Graduate'), ('Masters Level', 'Masters Level'), ('Masters Graduate', 'Masters Graduate'), ('Doctorate Level', 'Doctorate Level'), ('Doctorate Graduate', 'Doctorate Graduate')], max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='national_voter',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='sk_voter',
            field=models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='work_status',
            field=models.CharField(choices=[('Employed', 'Employed'), ('Unemployed', 'Unemployed'), ('Self-Employed', 'Self-Employed'), ('Currently Looking For a Job', 'Currently Looking For a Job'), ('Not interested Looking for a Job', 'Not interested Looking for a Job')], max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='youth_age_group',
            field=models.CharField(choices=[('Child Youth', 'Child Youth'), ('Core Youth', 'Core Youth'), ('Young Adult', 'Young Adult')], max_length=250),
        ),
        migrations.AlterField(
            model_name='profile',
            name='youth_classification',
            field=models.CharField(choices=[('In School Youth', 'In School Youth'), ('Out of School youth', 'Out of School youth'), ('Working Youth', 'Working Youth'), ('Youth With Special Needs - PWD', 'Person with Disability'), ('Youth With Special Needs - CCL', 'Children in Conflict with Law'), ('Youth With Special Needs - IP', 'Indigenous People')], max_length=250),
        ),
    ]
