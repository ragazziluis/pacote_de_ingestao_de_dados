import pytest
from pacote_de_ingestao_de_dados.meu_pacote.api import PokeAPI

def test_get_pokemon_data():
    data = PokeAPI.get_pokemon_data("pikachu")
    assert "name" in data
    assert data["name"] == "pikachu"

def test_get_pokemon_data_invalid():
    data = PokeAPI.get_pokemon_data("pokemon_inexistente")
    assert data == {}
