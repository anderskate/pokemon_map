from django.db import models


class Pokemon(models.Model):
    title = models.CharField('название', max_length=200)
    title_en = models.CharField('название на англ.', max_length=200)
    title_jp = models.CharField('название на яп.', max_length=200)
    image = models.ImageField('изображение', blank=True)
    description = models.TextField('описание')
    next_evolution = models.ForeignKey(
        'self', 
        verbose_name='следующий покемон в эволюции', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )
    previous_evolution = models.ForeignKey(
        'self', 
        verbose_name='предыдущий покемон в эволюции', 
        related_name='+', 
        on_delete=models.SET_NULL, 
        blank=True, 
        null=True
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, verbose_name='покемон', on_delete=models.CASCADE)
    lat = models.FloatField('широта')
    lon = models.FloatField('долгота')
    appeared_at = models.DateTimeField('когда появится')
    disappeared_at = models.DateTimeField('когда исчезнет')
    level = models.IntegerField('уровень')
    health = models.IntegerField('здоровье')
    strength = models.IntegerField('сила')
    defence = models.IntegerField('защита')
    stamina = models.IntegerField('выносливость')

    def __str__(self):
        return "{entity_id} cущность покемона - '{pokemon}'".format(
            pokemon = self.pokemon.title,
            entity_id = self.id
        )

