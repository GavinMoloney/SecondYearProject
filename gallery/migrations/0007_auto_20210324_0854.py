# Generated by Django 3.1.6 on 2021-03-24 08:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0006_auto_20210323_1644'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='votes',
            name='voted_by',
        ),
        migrations.AddField(
            model_name='picture',
            name='voted_by',
            field=models.ManyToManyField(related_name='voter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='picture',
            name='total_votes',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='picture',
            name='votes_this_month',
            field=models.IntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='votes',
            name='voted_picture',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='vote_pic', to='gallery.picture'),
        ),
    ]