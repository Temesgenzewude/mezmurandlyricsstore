from django.db import models


# Create your models here.

# Singers model

class Singer(models.Model):
    SINGERS= (
        ("Hana Takle", "hana takle"),
        ("Pastor Tesfaye Gabiso", "tesfaye gabiso"),
        ("Tamirat Haile", "tamirat haile"),
        ("Yosef Kassa", "yosef kassa"),
        ("Fenan Befikadu", "fenan befikadu"),
        ("Sofia Shibabaw", "sofia shibabaw"),
        ("Meskerem Getu", "meskerem getu"),
        ("Aster Abebe", "aster abebe"),
        ("Zerfe Kebede", "zerfe kebede"),
        ("Dereje Masebo", "dereje masebo"),
        ("Ephrem Alem","ephrem alemu"),
        ("Yishak Sedik", "yishak sedik"),
        ("Workneh Alaro", "workneh alaro"),
        ("Addisalem Assefe", "addisalem assefe"),
        ("Kalkidan Tilahun", "kalkidan tilahun"),
        ("Pastor Tekeste Getnet", "tekeste getnet"),
        ("Pastor Endale Woldegiorgis", "endale woldegiorgis"),
        ("Selam Desta", "selam desta"),
        ("Azeb Hailu", "azeb hailu"),
        ("Eyerusalem Ayele", "eyerusalem ayele"), 
    )
    
    
    singer_name=models.CharField(max_length=60, choices=SINGERS, unique=True)
    
    class Meta:
        ordering=['singer_name']

    
    def __str__(self):
        return f"{self.singer_name}"
    



class Album(models.Model):
    VOLUMES=(
        (1, 1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
        (11,11),
        (12,12),
        (13,13),
        (14,14),
        (15,15),
        
    )

    volume=models.IntegerField( choices=VOLUMES, default=VOLUMES[0][0])
    singer=models.ForeignKey(Singer, related_name='albums', on_delete=models.CASCADE)
    album_title=models.CharField(max_length=100, blank=True, null=True)
    album_logo=models.ImageField(upload_to="AlbumLogos", blank=True, null=True)
    
    class Meta:
        unique_together=['singer', 'volume']
        ordering=['volume']
    
    def __str__(self):
        return f"{self.singer} {self.album_title} volume {self.volume}"
    



class Song(models.Model):

    VOLUMES=(
        (1, 1),
        (2,2),
        (3,3),
        (4,4),
        (5,5),
        (6,6),
        (7,7),
        (8,8),
        (9,9),
        (10,10),
        (11,11),
        (12,12),
        (13,13),
        (14,14),
        (15,15), 
    )
    
    
    singer=models.ForeignKey(Singer, related_name='songs', on_delete=models.CASCADE)

    song=models.FileField(upload_to="songs/")
    song_title=models.CharField(max_length=50, blank=True, null=True)
    lyric=models.TextField(blank=True, null=True)
    volume=models.IntegerField(choices=VOLUMES, default=VOLUMES[0][0])
    album=models.ForeignKey(Album, related_name='songs', on_delete=models.CASCADE)
    is_favorite=models.BooleanField(default=False)
    
    
    class Meta:
        unique_together=['singer', 'volume', 'album']
        ordering=['volume']
    
    def __str__(self):
        return f"{self.song_title} by {self.singer} volume {self.volume}"
    
    
    
    
    
    


