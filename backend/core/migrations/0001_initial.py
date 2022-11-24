# Generated by Django 4.1.3 on 2022-11-21 12:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Albums',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('volume', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)])),
                ('album_title', models.CharField(blank=True, max_length=100, null=True)),
                ('album_logo', models.ImageField(blank=True, null=True, upload_to='AlbumLogos')),
            ],
        ),
        migrations.CreateModel(
            name='Singer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('singer_name', models.CharField(choices=[('Hana Takle', 'hana takle'), ('Pastor Tesfaye Gabiso', 'tesfaye gabiso'), ('Tamirat Haile', 'tamirat haile'), ('Yosef Kassa', 'yosef kassa'), ('Fenan Befikadu', 'fenan befikadu'), ('Sofia Shibabaw', 'sofia shibabaw'), ('Meskerem Getu', 'meskerem getu'), ('Aster Abebe', 'aster abebe'), ('Zerfe Kebede', 'zerfe kebede'), ('Dereje Masebo', 'dereje masebo'), ('Ephrem Alem', 'ephrem alemu'), ('Yishak Sedik', 'yishak sedik'), ('Workneh Alaro', 'workneh alaro'), ('Addisalem Assefe', 'addisalem assefe'), ('Kalkidan Tilahun', 'kalkidan tilahun'), ('Pastor Tekeste Getnet', 'tekeste getnet'), ('Pastor Endale Woldegiorgis', 'endale woldegiorgis'), ('Selam Desta', 'selam desta'), ('Azeb Hailu', 'azeb hailu'), ('Eyerusalem Ayele', 'eyerusalem ayele')], max_length=60, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Songs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('song', models.FileField(upload_to='songs/')),
                ('song_title', models.CharField(blank=True, max_length=50, null=True)),
                ('lyric', models.TextField(blank=True, null=True)),
                ('volume', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13), (14, 14), (15, 15)])),
                ('is_favorite', models.BooleanField(default=False)),
                ('album', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.albums')),
                ('singer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.singer')),
            ],
        ),
        migrations.AddField(
            model_name='albums',
            name='singer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.singer'),
        ),
    ]
