from django.contrib import admin
from .models import Pokemon, PokemonEntity

# Register your models here.
admin.site.register(Pokemon)
admin.site.register(PokemonEntity)