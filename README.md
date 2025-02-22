# Pacote de Ingestão de Dados da Pokédex

Este pacote Python coleta dados da API da Pokédex e os armazena na AWS S3.

## Instalação

Clone o repositório e instale as dependências:

```bash
git clone https://github.com/ragazziluis/pacote_de_ingestao_de_dados.git
cd pacote_de_ingestao_de_dados
pip install -r requirements.txt

```

## Uso

### Obter dados de um Pokémon:

```python
from pacote_de_ingestao_de_dados.meu_modulo.api import PokeAPI
data = PokeAPI.get_pokemon_data("pikachu")
print(data)

```

### Armazenar no S3:

```python
from pacote_de_ingestao_de_dados.meu_modulo.storage import Storage
storage = Storage("meu-bucket")
storage.upload_to_s3(data, "pikachu.json")

```
