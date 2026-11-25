"""Testes de integridade: os dados e os resultados gravados são coerentes entre si.
Uso (na pasta do projeto): python3 -m pytest tests -q"""
import hashlib, json
from pathlib import Path
import pandas as pd

RAIZ = Path(__file__).resolve().parent.parent
R = json.loads((RAIZ / 'resultados' / 'resultados.json').read_text(encoding='utf-8'))
P = pd.read_csv(RAIZ / 'dados' / 'tratados' / 'painel_pais_ano.csv')
J = pd.read_csv(RAIZ / 'dados' / 'tratados' / 'janelas_10_anos.csv')


def test_arquivo_bruto_nao_foi_alterado():
    h = hashlib.sha256((RAIZ / 'dados' / 'brutos' / 'owid-co2-data.csv').read_bytes()).hexdigest()
    assert h == R['sha256_bruto']


def test_base_tem_pelo_menos_mil_registros():
    assert len(P) >= 1000 and len(J) >= 1000
    assert len(P) == R['painel']['linhas'] and len(J) == R['janelas']['linhas']


def test_so_paises_no_painel():
    assert not P['iso_code'].str.startswith('OWID').any()
    assert not P.duplicated(['iso_code', 'ano']).any()
    assert (P['co2_per_capita'] > 0).all() and P['pib_per_capita'].notna().all()
    assert P['ano'].between(2000, 2022).all()


def test_nenhum_pais_nos_dois_conjuntos():
    for t in (P, J):
        tr = set(t.loc[t.conjunto == 'treino', 'iso_code']); te = set(t.loc[t.conjunto == 'teste', 'iso_code'])
        assert tr.isdisjoint(te)
    assert R['separacao']['paises_teste'] == P.loc[P.conjunto == 'teste', 'iso_code'].nunique()


def test_alvo_da_classificacao():
    assert ((J['co2_final'] < J['co2_per_capita']).astype(int) == J['reduziu']).all()
    assert (J['ano_final'] == J['ano'] + 10).all() and J['ano_final'].max() <= 2022
    assert int(J['reduziu'].sum()) == R['janelas']['reduziram']


def test_matriz_de_confusao_bate_com_a_acuracia():
    c = R['classificacao']; m = c['matriz']
    assert sum(map(sum, m)) == c['n_teste'] == int((J.conjunto == 'teste').sum())
    assert abs((m[0][0] + m[1][1]) / c['n_teste'] - c['acuracia_teste']) < 1e-9
    assert abs(m[1][1] / (m[1][0] + m[1][1]) - c['sensibilidade']) < 1e-9


def test_modelos_batem_a_referencia():
    assert R['regressao']['mae_log10'] < R['regressao']['mae_referencia_log10']
    assert R['classificacao']['acuracia_teste'] > R['classificacao']['acuracia_referencia']


def test_todos_os_grupos_tem_paises():
    ag = R['agrupamento']
    assert sum(p['paises'] for p in ag['perfil']) == ag['n']


def test_planilha_tem_os_mesmos_dados():
    x = pd.ExcelFile(RAIZ / 'dados' / 'planilha_base_de_dados.xlsx')
    assert {'Resumo', 'Dados', 'Janelas_10_anos', 'Dicionário', 'Estatisticas_por_ano', 'Resultados'} <= set(x.sheet_names)
    d = x.parse('Dados'); j = x.parse('Janelas_10_anos')
    assert len(d) == len(P) >= 1000 and len(j) == len(J) >= 1000
    assert abs(d['co2_per_capita'].sum() - P['co2_per_capita'].sum()) < 1e-6
    assert int(j['reduziu'].sum()) == int(J['reduziu'].sum())
