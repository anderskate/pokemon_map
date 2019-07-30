import folium
import json

from django.http import HttpResponseNotFound
from django.shortcuts import render
from .models import Pokemon, PokemonEntity
import os


MOSCOW_CENTER = [55.751244, 37.618423]
DEFAULT_IMAGE_URL = "https://vignette.wikia.nocookie.net/pokemon/images/6/6e/%21.png/revision/latest/fixed-aspect-ratio-down/width/240/height/240?cb=20130525215832&fill=transparent"


def add_pokemon(folium_map, lat, lon, name, image_url=DEFAULT_IMAGE_URL):
    icon = folium.features.CustomIcon(
        image_url,
        icon_size=(50, 50),
    )
    folium.Marker(
        [lat, lon],
        tooltip=name,
        icon=icon,
    ).add_to(folium_map)


def show_all_pokemons(request):
    pokemons_entities = PokemonEntity.objects.select_related('pokemon')
    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)
    for pokemon_entity in pokemons_entities:
        img_url = os.path.abspath(pokemon_entity.pokemon.image.url[1:])
        add_pokemon(
                folium_map, pokemon_entity.lat, pokemon_entity.lon,
                pokemon_entity.pokemon.title, img_url)

    pokemons_on_page = []
    pokemons = Pokemon.objects.all()
    for pokemon in pokemons:
        if pokemon.image:
            img_url = pokemon.image.url
        else:
            img_url = pokemon.image
        pokemons_on_page.append({
            'pokemon_id': pokemon.id,
            'img_url': img_url,
            'title_ru': pokemon.title,
        })

    return render(request, "mainpage.html", context={
        'map': folium_map._repr_html_(),
        'pokemons': pokemons_on_page,
    })


def show_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
        
    if pokemon.id == int(pokemon_id):
        requested_pokemon = pokemon
    else:
        return HttpResponseNotFound('<h1>Такой покемон не найден</h1>')

    folium_map = folium.Map(location=MOSCOW_CENTER, zoom_start=12)

    requested_pokemon_entities = PokemonEntity.objects.select_related('pokemon').filter(pokemon=requested_pokemon)
    for pokemon_entity in requested_pokemon_entities:
        img_url = os.path.abspath(pokemon_entity.pokemon.image.url[1:])
        add_pokemon(
            folium_map, pokemon_entity.lat, pokemon_entity.lon,
            pokemon_entity.pokemon.title, img_url)


    return render(request, "pokemon.html", context={'map': folium_map._repr_html_(),
                                                    'pokemon': pokemon})
