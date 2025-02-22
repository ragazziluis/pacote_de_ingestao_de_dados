import requests

class PokeAPI:
    BASE_URL = "https://pokeapi.co/api/v2/"

    @staticmethod
    def get_pokemon_data(pokemon_name: str) -> dict:
        """Busca dados de um Pokémon na API da PokeAPI."""
        url = f"{PokeAPI.BASE_URL}pokemon/{pokemon_name.lower()}"
        try:
            response = requests.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Erro ao buscar dados do Pokémon {pokemon_name}: {e}")
            return {}
