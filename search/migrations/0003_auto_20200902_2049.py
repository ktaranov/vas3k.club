# Generated by Django 3.1 on 2020-09-02 20:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('search', '0002_searchindex_tags'),
    ]

    operations = [
        migrations.RenameField(
            model_name='searchindex',
            old_name='profile',
            new_name='user',
        ),
        migrations.AddField(
            model_name='searchindex',
            name='type',
            field=models.CharField(choices=[('post', 'post'), ('comment', 'comment'), ('user', 'user')], db_index=True, max_length=32, null=True),
        ),
    ]
