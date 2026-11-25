"""Baixa o arquivo original do Our World in Data e grava a procedência (dados/brutos/FONTES.json).
Uso: python3 scripts/obter_dados.py"""
import hashlib, json, urllib.request
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
BRUTOS = RAIZ / 'dados' / 'brutos'
BRUTOS.mkdir(parents=True, exist_ok=True)
BASE = 'https://raw.githubusercontent.com/owid/co2-data/master/'
ARQUIVOS = ['owid-co2-data.csv', 'owid-co2-codebook.csv']

fontes = {'projeto': 'Our World in Data — CO₂ and Greenhouse Gas Emissions',
          'repositorio': 'https://github.com/owid/co2-data', 'licenca': 'CC BY 4.0',
          'acessado_em': date.today().isoformat(), 'arquivos': []}
for nome in ARQUIVOS:
    destino = BRUTOS / nome
    urllib.request.urlretrieve(BASE + nome, destino)
    dados = destino.read_bytes()
    fontes['arquivos'].append({'arquivo': nome, 'url': BASE + nome, 'bytes': len(dados),
                               'sha256': hashlib.sha256(dados).hexdigest()})
    print(nome, len(dados), 'bytes')
(BRUTOS / 'FONTES.json').write_text(json.dumps(fontes, ensure_ascii=False, indent=2), encoding='utf-8')
print('Gravado dados/brutos/FONTES.json')
