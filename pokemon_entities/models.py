from django.db import models


class Pokemon(models.Model):
    title = models.CharField('название', max_length=200)
    title_en = models.CharField('название на англ.', max_length=200, blank=True)
    title_jp = models.CharField('название на яп.', max_length=200, blank=True)
    image = models.ImageField('изображение', blank=True, null=True)
    description = models.TextField('описание', blank=True)
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
    lat = models.FloatField('широта', blank=True, null=True)
    lon = models.FloatField('долгота', blank=True, null=True)
    appeared_at = models.DateTimeField('когда появится', blank=True, null=True)
    disappeared_at = models.DateTimeField('когда исчезнет', blank=True, null=True)
    level = models.IntegerField('уровень', blank=True, null=True)
    health = models.IntegerField('здоровье', blank=True, null=True)
    strength = models.IntegerField('сила', blank=True, null=True)
    defence = models.IntegerField('защита', blank=True, null=True)
    stamina = models.IntegerField('выносливость', blank=True, null=True)

    def __str__(self):
        return "{entity_id} cущность покемона - '{pokemon}'".format(
            pokemon = self.pokemon.title,
            entity_id = self.id
        )

