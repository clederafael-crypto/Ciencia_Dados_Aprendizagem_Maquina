# %% [markdown]
# # CRISP-DM aplicado a emissões de CO₂ e desenvolvimento dos países
# Execução completa do estudo. Cada bloco `# %%` vira uma célula do notebook.

# %% Ambiente e pastas
import sys, json, hashlib
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import sklearn
from sklearn.base import clone
from sklearn.model_selection import GroupKFold, StratifiedGroupKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.dummy import DummyRegressor, DummyClassifier
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.cluster import KMeans
from sklearn.metrics import (mean_absolute_error, r2_score, accuracy_score, roc_auc_score,
                             confusion_matrix, recall_score, precision_score, silhouette_score, roc_curve)

SEMENTE = 42
ANO = 2022            # último ano com PIB na base
ANO_INICIO_PAINEL = 2000   # o painel vai de 2000 a 2022
JANELA = 10           # a pergunta de mudança olha 10 anos à frente

try:
    RAIZ = Path(__file__).resolve().parent.parent
except NameError:                      # dentro do notebook (pasta notebooks/)
    RAIZ = Path('..').resolve()
BRUTOS, TRATADOS = RAIZ / 'dados' / 'brutos', RAIZ / 'dados' / 'tratados'
RESULT, FIGS = RAIZ / 'resultados', RAIZ / 'figuras'
for p in (BRUTOS, TRATADOS, RESULT, FIGS):
    p.mkdir(parents=True, exist_ok=True)

URL = 'https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv'
CSV = BRUTOS / 'owid-co2-data.csv'
if not CSV.exists():                   # Colab: baixa o arquivo original
    import urllib.request
    urllib.request.urlretrieve(URL, CSV)

plt.rcParams.update({'figure.dpi': 110, 'axes.spines.top': False, 'axes.spines.right': False,
                     'axes.grid': True, 'grid.alpha': .25, 'font.size': 10})
AZUL, LARANJA, CINZA = '#1f5f8b', '#d9822b', '#8a8f98'
print('Python', sys.version.split()[0], '| numpy', np.__version__, '| pandas', pd.__version__,
      '| scikit-learn', sklearn.__version__, '| matplotlib', matplotlib.__version__)
R = {'versoes': {'python': sys.version.split()[0], 'numpy': np.__version__, 'pandas': pd.__version__,
                 'sklearn': sklearn.__version__, 'matplotlib': matplotlib.__version__},
     'semente': SEMENTE, 'ano_fim': ANO, 'ano_inicio_painel': ANO_INICIO_PAINEL, 'janela_anos': JANELA}

# %% Fase 2 — entendimento dos dados
bruto = pd.read_csv(CSV)
R['sha256_bruto'] = hashlib.sha256(CSV.read_bytes()).hexdigest()
agregados = bruto[bruto['iso_code'].isna() | bruto['iso_code'].astype(str).str.startswith('OWID')]
paises = bruto[~bruto.index.isin(agregados.index)].copy()
print('Linhas brutas:', bruto.shape, '| países (com código ISO):', paises['country'].nunique(),
      '| agregados/regiões descartados:', agregados['country'].nunique())
print('Anos:', bruto['year'].min(), 'a', bruto['year'].max())
R['dados'] = {'linhas': int(len(bruto)), 'colunas': int(bruto.shape[1]),
              'paises': int(paises['country'].nunique()), 'agregados': int(agregados['country'].nunique())}

cols = ['co2_per_capita', 'gdp', 'population', 'energy_per_capita', 'methane_per_capita',
        'land_use_change_co2_per_capita', 'coal_co2', 'oil_co2', 'gas_co2']
corte = paises[paises['year'] == ANO]
cobertura = (1 - corte[cols].isna().mean()).mul(100).round(1)
print(f'\nCobertura (% de países com valor) em {ANO}:'); print(cobertura.to_string())
R['cobertura_2022'] = cobertura.to_dict()
R['paises_em_2022'] = int(len(corte))

# %% Fase 3 — preparação: o painel país-ano
def prepara(df):
    d = df.copy()
    d['pib_per_capita'] = d['gdp'] / d['population']                # US$ internacionais de 2011
    d['part_carvao'] = d['coal_co2'] / d['co2']
    d['part_petroleo'] = d['oil_co2'] / d['co2']
    d['part_gas'] = d['gas_co2'] / d['co2']
    d = d.rename(columns={'country': 'pais', 'year': 'ano', 'population': 'populacao',
                          'energy_per_capita': 'energia_per_capita', 'methane_per_capita': 'metano_per_capita'})
    return d[['iso_code', 'pais', 'ano', 'populacao', 'pib_per_capita', 'co2_per_capita', 'energia_per_capita',
              'metano_per_capita', 'part_carvao', 'part_petroleo', 'part_gas']]

todos_anos = prepara(paises)
P = (todos_anos[todos_anos['ano'].between(ANO_INICIO_PAINEL, ANO)]
     .dropna(subset=['co2_per_capita', 'pib_per_capita', 'populacao']).query('co2_per_capita > 0').copy())
P['log_co2'] = np.log10(P['co2_per_capita'])
P['log_pib'] = np.log10(P['pib_per_capita'])
P['log_pop'] = np.log10(P['populacao'])
P['log_energia'] = np.log10(P['energia_per_capita'].where(P['energia_per_capita'] > 0))
P = P.reset_index(drop=True)
print('PAINEL país-ano:', len(P), 'linhas |', P['iso_code'].nunique(), 'países |', P['ano'].min(), 'a', P['ano'].max())
print('Linhas por país (mín/mediana/máx):', P.groupby('iso_code').size().agg(['min', 'median', 'max']).tolist())
print('Ausências nas colunas usadas:'); print(P[['log_energia', 'metano_per_capita', 'part_carvao', 'part_petroleo', 'part_gas']].isna().sum().to_string())
R['painel'] = {'linhas': int(len(P)), 'paises': int(P['iso_code'].nunique()), 'ano_min': int(P['ano'].min()), 'ano_max': int(P['ano'].max()),
               'linhas_por_pais': P.groupby('iso_code').size().agg(['min', 'median', 'max']).astype(int).tolist(),
               'ausentes': P[['log_energia', 'metano_per_capita', 'part_carvao', 'part_petroleo', 'part_gas']].isna().sum().astype(int).to_dict()}

# janelas de 10 anos: atributos no ano inicial, alvo no ano final (só para a classificação)
co2_serie = paises.set_index(['iso_code', 'year'])['co2_per_capita']
def co2_em(anos):
    idx = pd.MultiIndex.from_arrays([P['iso_code'], P['ano'] + anos])
    return co2_serie.reindex(idx).values
J = P[P['ano'] <= ANO - JANELA].copy()
J['ano_final'] = J['ano'] + JANELA
J['co2_final'] = co2_em(JANELA)[J.index]
J['co2_5_anos_antes'] = co2_em(-5)[J.index]
J = J[J['co2_final'] > 0].copy()
J['reduziu'] = (J['co2_final'] < J['co2_per_capita']).astype(int)
J['variacao_pct'] = (J['co2_final'] / J['co2_per_capita'] - 1) * 100
J['tendencia_5a'] = J['log_co2'] - np.log10(J['co2_5_anos_antes'].where(J['co2_5_anos_antes'] > 0))
J = J.reset_index(drop=True)
print('\nJANELAS de 10 anos:', len(J), 'linhas |', J['iso_code'].nunique(), 'países | anos iniciais', J['ano'].min(), 'a', J['ano'].max())
print('Reduziram:', int(J['reduziu'].sum()), f"({J['reduziu'].mean():.1%}) | não reduziram: {int((1 - J['reduziu']).sum())}")
R['janelas'] = {'linhas': int(len(J)), 'paises': int(J['iso_code'].nunique()), 'reduziram': int(J['reduziu'].sum()),
                'prop_reduziu': float(J['reduziu'].mean())}

# separação por PAÍS (um país nunca fica nos dois lados), feita antes de qualquer ajuste
isos = np.array(sorted(P['iso_code'].unique()))
teste_isos = set(np.random.default_rng(SEMENTE).choice(isos, size=int(round(0.25 * len(isos))), replace=False))
P['conjunto'] = np.where(P['iso_code'].isin(teste_isos), 'teste', 'treino')
J['conjunto'] = np.where(J['iso_code'].isin(teste_isos), 'teste', 'treino')
print('\nPaíses de teste:', len(teste_isos), '| países de treino:', len(isos) - len(teste_isos))
print('Painel — treino:', int((P.conjunto == 'treino').sum()), 'linhas | teste:', int((P.conjunto == 'teste').sum()), 'linhas')
print('Janelas — treino:', int((J.conjunto == 'treino').sum()), 'linhas | teste:', int((J.conjunto == 'teste').sum()), 'linhas')
R['separacao'] = {'paises_teste': len(teste_isos), 'paises_treino': int(len(isos) - len(teste_isos)),
                  'painel_treino': int((P.conjunto == 'treino').sum()), 'painel_teste': int((P.conjunto == 'teste').sum()),
                  'janelas_treino': int((J.conjunto == 'treino').sum()), 'janelas_teste': int((J.conjunto == 'teste').sum()),
                  'brasil_no': 'teste' if 'BRA' in teste_isos else 'treino'}
P.to_csv(TRATADOS / 'painel_pais_ano.csv', index=False); J.to_csv(TRATADOS / 'janelas_10_anos.csv', index=False)

# %% Figura 1 — visão geral dos dados
fig, ax = plt.subplots(1, 2, figsize=(12, 4.4))
ax[0].hist(P['log_co2'], bins=40, color=AZUL); ax[0].set_xlabel('log10 do CO₂ per capita (cada linha = um país em um ano)')
ax[0].set_ylabel('Linhas do painel'); ax[0].set_title(f'{len(P):,}'.replace(',', '.') + ' linhas país-ano, em escala log')
ax[1].scatter(P['pib_per_capita'], P['co2_per_capita'], s=5, color=CINZA, alpha=.35, label='Todos os países e anos')
brp = P[P['iso_code'] == 'BRA'].sort_values('ano')
ax[1].plot(brp['pib_per_capita'], brp['co2_per_capita'], color=LARANJA, lw=2, label='Brasil, 2000–2022')
ax[1].set_xscale('log'); ax[1].set_yscale('log'); ax[1].set_xlabel('PIB per capita (US$ intern. 2011, log)')
ax[1].set_ylabel('CO₂ per capita (t, log)'); ax[1].set_title('Países mais ricos emitem mais por pessoa'); ax[1].legend(frameon=False, loc='lower right')
plt.tight_layout(); plt.savefig(FIGS / '01-visao-geral.png', dpi=130); plt.close()
r_log = float(np.corrcoef(P.log_pib, P.log_co2)[0, 1])
print('Correlação entre log PIB per capita e log CO2 per capita (todas as linhas):', round(r_log, 3))
R['correlacao_log_pib_log_co2'] = r_log

# %% Fase 4A — regressão: quanto um país emite por pessoa, dado seu perfil?
conjuntos = {'1 só PIB per capita': ['log_pib'],
             '2 PIB + população + metano + ano': ['log_pib', 'log_pop', 'metano_per_capita', 'ano'],
             '3 PIB + pop. + metano + ano + energia': ['log_pib', 'log_pop', 'metano_per_capita', 'ano', 'log_energia']}
tr = P[P.conjunto == 'treino'].reset_index(drop=True); te = P[P.conjunto == 'teste'].reset_index(drop=True)
print('Treino:', len(tr), 'linhas de', tr.iso_code.nunique(), 'países | Teste:', len(te), 'linhas de', te.iso_code.nunique(), 'países')

def divisoes_regressao(g, reps=3, k=5):
    out = []
    for r in range(reps):
        out += list(GroupKFold(n_splits=k, shuffle=True, random_state=SEMENTE + r).split(np.zeros(len(g)), groups=g))
    return out
cvr = divisoes_regressao(tr['iso_code'])

def pipe_reg(modelo):
    etapas = [('imp', SimpleImputer(strategy='median'))]
    if isinstance(modelo, LinearRegression):
        etapas.append(('esc', StandardScaler()))
    return Pipeline(etapas + [('m', modelo)])

def modelos():
    return {'Linear': LinearRegression(),
            'Floresta': RandomForestRegressor(n_estimators=150, min_samples_leaf=5, random_state=SEMENTE, n_jobs=1)}

linhas = []
for nome, cs in conjuntos.items():
    for mn, m in modelos().items():
        s = cross_validate(pipe_reg(m), tr[cs], tr['log_co2'], cv=cvr, scoring={'mae': 'neg_mean_absolute_error', 'r2': 'r2'})
        linhas.append({'conjunto': nome, 'modelo': mn, 'mae_val': -s['test_mae'].mean(),
                       'mae_desvio': s['test_mae'].std(), 'r2_val': s['test_r2'].mean()})
base = cross_validate(Pipeline([('m', DummyRegressor())]), tr[['log_pib']], tr['log_co2'], cv=cvr,
                      scoring={'mae': 'neg_mean_absolute_error', 'r2': 'r2'})
linhas.append({'conjunto': 'referência (média)', 'modelo': 'Dummy', 'mae_val': -base['test_mae'].mean(),
               'mae_desvio': base['test_mae'].std(), 'r2_val': base['test_r2'].mean()})
reg_cv = pd.DataFrame(linhas)
print(reg_cv.round(4).to_string(index=False))
reg_cv.round(4).to_csv(RESULT / 'regressao_validacao.csv', index=False)
melhor = reg_cv[reg_cv.modelo != 'Dummy'].sort_values('mae_val', kind='stable').iloc[0]     # regra: menor MAE médio de validação
print('\nEscolhido pela validação:', melhor['conjunto'], '+', melhor['modelo'])

# %% Fase 5A — avaliação final da regressão (países de teste, usados uma única vez)
cs_final = conjuntos[melhor['conjunto']]
modelo_reg = pipe_reg(modelos()[melhor['modelo']]).fit(tr[cs_final], tr['log_co2'])
pred = modelo_reg.predict(te[cs_final])
dummy = Pipeline([('m', DummyRegressor())]).fit(tr[['log_pib']], tr['log_co2'])
mae_te, r2_te = mean_absolute_error(te['log_co2'], pred), r2_score(te['log_co2'], pred)
mae_ref = mean_absolute_error(te['log_co2'], dummy.predict(te[['log_pib']]))
print(f'MAE (log10) teste: {mae_te:.4f} → erro típico de ×{10 ** mae_te:.2f} | referência: {mae_ref:.4f} (×{10 ** mae_ref:.2f})')
print(f'R² teste: {r2_te:.4f}')
R['regressao'] = {'conjunto': melhor['conjunto'], 'modelo': melhor['modelo'], 'n_treino': int(len(tr)), 'n_teste': int(len(te)),
                  'mae_log10': float(mae_te), 'fator_erro': float(10 ** mae_te), 'r2_teste': float(r2_te),
                  'mae_referencia_log10': float(mae_ref), 'fator_erro_referencia': float(10 ** mae_ref),
                  'validacao': reg_cv.round(4).to_dict('records')}
extra = {}
for nome, cs in conjuntos.items():      # descritivo: já conhecido o teste, não altera a escolha
    m = pipe_reg(modelos()[melhor['modelo']]).fit(tr[cs], tr['log_co2'])
    extra[nome] = {'mae': float(mean_absolute_error(te['log_co2'], m.predict(te[cs]))), 'r2': float(r2_score(te['log_co2'], m.predict(te[cs])))}
R['regressao']['teste_por_conjunto_descritivo'] = extra
print('\nDescritivo (teste por conjunto, mesmo modelo):'); print(pd.DataFrame(extra).T.round(4).to_string())

res = te['log_co2'] - pred
fig, ax = plt.subplots(1, 2, figsize=(11, 4.4))
ax[0].scatter(te['log_co2'], pred, s=7, color=AZUL, alpha=.5)
lim = [min(te['log_co2'].min(), pred.min()) - .1, max(te['log_co2'].max(), pred.max()) + .1]
ax[0].plot(lim, lim, '--', color='black', lw=1); ax[0].set_xlabel('Observado (log10 t/pessoa)')
ax[0].set_ylabel('Previsto'); ax[0].set_title(f'Teste ({len(te)} linhas, {te.iso_code.nunique()} países): R² = {r2_te:.2f}, MAE = {mae_te:.2f}', fontsize=9.5)
ax[1].scatter(pred, res, s=7, color=AZUL, alpha=.5); ax[1].axhline(0, color='black', ls='--', lw=1)
ax[1].set_xlabel('Previsto'); ax[1].set_ylabel('Resíduo (observado − previsto)'); ax[1].set_title('Resíduos no teste')
plt.tight_layout(); plt.savefig(FIGS / '02-regressao.png', dpi=130); plt.close()
print(f'Resíduos: média {res.mean():.3f}, desvio {res.std():.3f}')
te = te.assign(previsto=pred, residuo=res)
por_pais = te.groupby(['iso_code', 'pais']).agg(linhas=('ano', 'size'), residuo_medio=('residuo', 'mean')).reset_index()
R['regressao']['teste_acima_previsto'] = por_pais.nlargest(5, 'residuo_medio').round(3).to_dict('records')
R['regressao']['teste_abaixo_previsto'] = por_pais.nsmallest(5, 'residuo_medio').round(3).to_dict('records')
print('\nTeste — emitem mais que o previsto (resíduo médio 2000–2022):'); print(por_pais.nlargest(5, 'residuo_medio').round(3).to_string(index=False))
print('Teste — emitem menos que o previsto:'); print(por_pais.nsmallest(5, 'residuo_medio').round(3).to_string(index=False))
# O Brasil caiu no treino. Para uma comparação honesta, prevejo o Brasil com um modelo ajustado SEM o Brasil.
sem_br = tr[tr.iso_code != 'BRA']
m_br = pipe_reg(modelos()[melhor['modelo']]).fit(sem_br[cs_final], sem_br['log_co2'])
bra = P[P.iso_code == 'BRA'].sort_values('ano').copy()
bra['previsto'] = m_br.predict(bra[cs_final]); bra['residuo'] = bra['log_co2'] - bra['previsto']
r22 = bra[bra.ano == ANO].iloc[0]
R['brasil_regressao'] = {'no_conjunto': R['separacao']['brasil_no'], 'residuo_medio_log10': float(bra['residuo'].mean()),
                         'fator_medio': float(10 ** bra['residuo'].mean()), 'co2_2022': float(r22['co2_per_capita']),
                         'previsto_2022_t': float(10 ** r22['previsto']), 'anos_abaixo_do_previsto': int((bra['residuo'] < 0).sum()), 'anos': int(len(bra))}
print('\nBrasil (previsto por um modelo sem o Brasil):', {k: (round(v, 3) if isinstance(v, float) else v) for k, v in R['brasil_regressao'].items()})
te[['iso_code', 'pais', 'ano', 'co2_per_capita', 'previsto', 'residuo']].assign(previsto_t=lambda d: 10 ** d['previsto']).to_csv(TRATADOS / 'previsoes_regressao_teste.csv', index=False)

# %% Fase 4B — classificação: o país reduziu o CO2 per capita nos 10 anos seguintes?
atrib = ['ano', 'log_co2', 'log_pib', 'log_pop', 'log_energia', 'metano_per_capita',
         'part_carvao', 'part_petroleo', 'part_gas', 'tendencia_5a']
jtr = J[J.conjunto == 'treino'].reset_index(drop=True); jte = J[J.conjunto == 'teste'].reset_index(drop=True)
print('Treino:', len(jtr), 'janelas de', jtr.iso_code.nunique(), 'países | Teste:', len(jte), 'janelas de', jte.iso_code.nunique(), 'países')
print(f'% que reduziu: treino {jtr.reduziu.mean():.3f} | teste {jte.reduziu.mean():.3f}')
cvc = []
for r in range(3):
    cvc += list(StratifiedGroupKFold(n_splits=5, shuffle=True, random_state=SEMENTE + r).split(jtr[atrib], jtr['reduziu'], groups=jtr['iso_code']))

def pipe_cls(m, escala=False):
    et = [('imp', SimpleImputer(strategy='median'))]
    if escala:
        et.append(('esc', StandardScaler()))
    return Pipeline(et + [('m', m)])

cand = {'Referência (classe mais frequente)': pipe_cls(DummyClassifier(strategy='most_frequent')),
        'Regressão logística': pipe_cls(LogisticRegression(max_iter=1000), True),
        'Árvore (prof. 4)': pipe_cls(DecisionTreeClassifier(max_depth=4, min_samples_leaf=20, random_state=SEMENTE)),
        'Floresta': pipe_cls(RandomForestClassifier(n_estimators=150, min_samples_leaf=10, random_state=SEMENTE, n_jobs=1))}
linhas = []
for nome, m in cand.items():
    s = cross_validate(m, jtr[atrib], jtr['reduziu'], cv=cvc, scoring=['accuracy', 'roc_auc'])
    linhas.append({'modelo': nome, 'acc_val': s['test_accuracy'].mean(), 'acc_desvio': s['test_accuracy'].std(),
                   'auc_val': s['test_roc_auc'].mean(), 'auc_desvio': s['test_roc_auc'].std()})
cls_cv = pd.DataFrame(linhas); print(cls_cv.round(4).to_string(index=False))
cls_cv.round(4).to_csv(RESULT / 'classificacao_validacao.csv', index=False)
melhor_c = cls_cv.iloc[1:].sort_values('auc_val', ascending=False, kind='stable').iloc[0]['modelo']   # regra: maior AUC médio
print('\nEscolhido pela validação (maior AUC médio):', melhor_c)

# %% Fase 5B — avaliação final da classificação (países de teste, usados uma única vez)
mc = cand[melhor_c].fit(jtr[atrib], jtr['reduziu'])
ref = cand['Referência (classe mais frequente)'].fit(jtr[atrib], jtr['reduziu'])
prev, prob = mc.predict(jte[atrib]), mc.predict_proba(jte[atrib])[:, 1]
yb_te = jte['reduziu']
cm = confusion_matrix(yb_te, prev, labels=[0, 1]); tn, fp, fn, tp = cm.ravel()
acc, acc_ref = accuracy_score(yb_te, prev), accuracy_score(yb_te, ref.predict(jte[atrib]))
auc = roc_auc_score(yb_te, prob)
print(f'Acurácia teste: {acc:.4f} | referência: {acc_ref:.4f} | AUC: {auc:.4f}')
print('Matriz [linhas reais, colunas previstas] (0 = não reduziu, 1 = reduziu):'); print(cm)
sens = tp / (tp + fn); prec = tp / (tp + fp) if tp + fp else float('nan')
print(f'Sensibilidade (reduziu): {sens:.4f} | Precisão: {prec:.4f}')
R['classificacao'] = {'modelo': melhor_c, 'n_treino': int(len(jtr)), 'n_teste': int(len(jte)),
                      'acuracia_teste': float(acc), 'acuracia_referencia': float(acc_ref), 'auc_teste': float(auc),
                      'matriz': cm.tolist(), 'sensibilidade': float(sens), 'precisao': float(prec),
                      'validacao': cls_cv.round(4).to_dict('records')}
fig, ax = plt.subplots(1, 2, figsize=(10, 4.2))
ax[0].imshow(cm, cmap='Blues')
for i in range(2):
    for j in range(2):
        ax[0].text(j, i, cm[i, j], ha='center', va='center', fontsize=14, color='white' if cm[i, j] > cm.max() / 2 else 'black')
ax[0].set_xticks([0, 1], ['Não reduziu', 'Reduziu']); ax[0].set_yticks([0, 1], ['Não reduziu', 'Reduziu'])
ax[0].set_xlabel('Previsto'); ax[0].set_ylabel('Real'); ax[0].set_title(f'Teste: acurácia {acc:.2f} ({melhor_c})'); ax[0].grid(False)
fpr, tpr, _ = roc_curve(yb_te, prob); ax[1].plot(fpr, tpr, color=AZUL, lw=2, label=melhor_c); ax[1].legend(frameon=False, loc='lower right')
ax[1].set_xlabel('Taxa de falsos positivos'); ax[1].set_ylabel('Sensibilidade')
ax[1].plot([0, 1], [0, 1], '--', color=CINZA); ax[1].set_title(f'Curva ROC no teste (AUC {auc:.2f})')
plt.tight_layout(); plt.savefig(FIGS / '03-classificacao.png', dpi=130); plt.close()

lr = cand['Regressão logística'].fit(jtr[atrib], jtr['reduziu'])
coef = pd.Series(lr.named_steps['m'].coef_[0], index=atrib).sort_values()
print('\nCoeficientes padronizados da logística (treino):'); print(coef.round(3).to_string())
R['classificacao']['coef_logistica'] = coef.round(4).to_dict()
sem_br_j = jtr[jtr.iso_code != 'BRA']
m_brj = clone(cand[melhor_c]).fit(sem_br_j[atrib], sem_br_j['reduziu'])
bj = J[J.iso_code == 'BRA'].sort_values('ano').copy()
bj['prob_reduzir'] = m_brj.predict_proba(bj[atrib])[:, 1]; bj['previsto'] = (bj['prob_reduzir'] >= .5).astype(int)
R['brasil_classificacao'] = {'no_conjunto': R['separacao']['brasil_no'], 'janelas': int(len(bj)), 'reduziu_real': int(bj['reduziu'].sum()),
                             'acertos': int((bj['previsto'] == bj['reduziu']).sum()),
                             'por_janela': bj[['ano', 'ano_final', 'reduziu', 'previsto']].assign(prob=bj['prob_reduzir'].round(2)).to_dict('records')}
print('\nBrasil (modelo sem o Brasil):', {k: v for k, v in R['brasil_classificacao'].items() if k != 'por_janela'})
print(bj[['ano', 'ano_final', 'reduziu', 'previsto', 'prob_reduzir']].round(2).to_string(index=False))
jte.assign(previsto=prev, prob_reduzir=prob.round(3))[['iso_code', 'pais', 'ano', 'ano_final', 'reduziu', 'previsto', 'prob_reduzir']].to_csv(TRATADOS / 'previsoes_classificacao_teste.csv', index=False)

# %% Fase 4C — agrupamento de países em 2022
atrib_c = ['log_co2', 'log_pib', 'log_energia', 'metano']
print('Agrupamento: um corte (2022), um país por linha')
C = P[P['ano'] == ANO].set_index('iso_code').rename(columns={'metano_per_capita': 'metano'}).dropna(subset=atrib_c).copy()
Z = StandardScaler().fit_transform(C[atrib_c])
print('Países no agrupamento:', len(C))
sil = {}
for k in range(2, 8):
    km = KMeans(n_clusters=k, n_init=20, random_state=SEMENTE).fit(Z)
    sil[k] = float(silhouette_score(Z, km.labels_))
print({k: round(v, 3) for k, v in sil.items()})
k_ok = max((k for k in sil if 3 <= k <= 6), key=sil.get)      # regra fixada: melhor silhueta entre 3 e 6 grupos
km = KMeans(n_clusters=k_ok, n_init=20, random_state=SEMENTE).fit(Z)
C['grupo'] = km.labels_
perfil = C.groupby('grupo').agg(paises=('pais', 'size'), co2_pc=('co2_per_capita', 'median'),
                                pib_pc=('pib_per_capita', 'median'), energia_pc=('energia_per_capita', 'median'),
                                metano_pc=('metano', 'median')).round(2)
ordem = perfil['co2_pc'].sort_values().index
perfil = perfil.loc[ordem]; perfil.index = range(1, k_ok + 1)
C['grupo'] = C['grupo'].map({old: i + 1 for i, old in enumerate(ordem)})
print(f'\nk escolhido: {k_ok} (silhueta {sil[k_ok]:.3f})'); print(perfil.to_string())
gbr = int(C.loc['BRA', 'grupo']); print('Brasil está no grupo', gbr)
exemplos = {int(g): C[C.grupo == g].sort_values('populacao', ascending=False)['pais'].head(6).tolist() for g in range(1, k_ok + 1)}
for g, e in exemplos.items(): print(g, e)
R['agrupamento'] = {'n': int(len(C)), 'silhueta_por_k': sil, 'k': int(k_ok), 'perfil': perfil.reset_index().rename(columns={'index': 'grupo'}).to_dict('records'),
                    'grupo_brasil': gbr, 'maiores_paises_por_grupo': exemplos}
C[['pais', 'grupo', 'co2_per_capita', 'pib_per_capita', 'energia_per_capita', 'metano']].to_csv(TRATADOS / 'grupos_2022.csv')

# Complemento descritivo (a regra de escolha não muda): como ficaria com k = 4?
km4 = KMeans(n_clusters=4, n_init=20, random_state=SEMENTE).fit(Z)
C4 = C.assign(g4=km4.labels_)
p4 = C4.groupby('g4').agg(paises=('pais', 'size'), co2_pc=('co2_per_capita', 'median'), pib_pc=('pib_per_capita', 'median'),
                          energia_pc=('energia_per_capita', 'median'), metano_pc=('metano', 'median')).round(2).sort_values('co2_pc')
ordem4 = list(p4.index); p4.index = range(1, 5)
C4['g4'] = C4['g4'].map({o: i + 1 for i, o in enumerate(ordem4)})
print('\nDescritivo, k = 4 (silhueta %.3f):' % sil[4]); print(p4.to_string())
ex4 = {int(g): C4[C4.g4 == g].sort_values('populacao', ascending=False)['pais'].head(6).tolist() for g in range(1, 5)}
for g, e in ex4.items(): print(g, e)
print('Brasil no k=4: grupo', int(C4.loc['BRA', 'g4']))
R['agrupamento_k4_descritivo'] = {'silhueta': sil[4], 'perfil': p4.reset_index().rename(columns={'index': 'grupo'}).to_dict('records'),
                                  'maiores_paises_por_grupo': ex4, 'grupo_brasil': int(C4.loc['BRA', 'g4'])}

fig, ax = plt.subplots(1, 2, figsize=(12, 4.6))
cores = ['#1f5f8b', '#2a9d8f', '#e9c46a', '#d9822b', '#b5483a', '#6d597a'][:k_ok]
for g in range(1, k_ok + 1):
    s = C[C.grupo == g]
    ax[0].scatter(s['pib_per_capita'], s['co2_per_capita'], s=22, color=cores[g - 1], alpha=.85, label=f'Grupo {g} (n={len(s)})')
ax[0].scatter(C.loc['BRA', 'pib_per_capita'], C.loc['BRA', 'co2_per_capita'], s=90, facecolors='none', edgecolors='black', lw=1.6)
ax[0].annotate('Brasil', (C.loc['BRA', 'pib_per_capita'], C.loc['BRA', 'co2_per_capita']), xytext=(8, 8), textcoords='offset points')
ax[0].set_xscale('log'); ax[0].set_yscale('log'); ax[0].set_xlabel('PIB per capita (log)'); ax[0].set_ylabel('CO₂ per capita (t, log)')
ax[0].legend(fontsize=8, frameon=False); ax[0].set_title(f'Agrupamento k-means, k = {k_ok}')
ax[1].plot(list(sil), list(sil.values()), 'o-', color=AZUL); ax[1].axvline(k_ok, color=LARANJA, ls='--')
ax[1].set_xlabel('Número de grupos (k)'); ax[1].set_ylabel('Silhueta média'); ax[1].set_title('Escolha de k')
plt.tight_layout(); plt.savefig(FIGS / '04-agrupamento.png', dpi=130); plt.close()

# %% Brasil no tempo, comparado ao mundo
def serie(nome):
    return paises[paises.country == nome].set_index('year')['co2_per_capita'] if nome != 'World' else \
        bruto[bruto.country == 'World'].set_index('year')['co2_per_capita']
s_br, s_mu = serie('Brazil'), serie('World')
fig, ax = plt.subplots(figsize=(8, 4))
for s, n, c in ((s_mu, 'Mundo', CINZA), (s_br, 'Brasil', LARANJA)):
    t = s.loc[1990:2024]; ax.plot(t.index, t.values, label=n, color=c, lw=2)
ax.axvline(ANO_INICIO_PAINEL, color='black', ls=':', lw=1); ax.axvline(ANO, color='black', ls=':', lw=1)
ax.set_ylabel('CO₂ per capita (t/pessoa)'); ax.set_title('Emissões per capita desde 1990'); ax.legend(frameon=False)
plt.tight_layout(); plt.savefig(FIGS / '05-brasil-mundo.png', dpi=130); plt.close()
R['brasil_mundo'] = {'brasil_2000': float(s_br.loc[2000]), 'brasil_2022': float(s_br.loc[2022]), 'brasil_pico_ano': int(s_br.loc[1990:2024].idxmax()), 'brasil_pico': float(s_br.loc[1990:2024].max()),
                     'mundo_2000': float(s_mu.loc[2000]), 'mundo_2022': float(s_mu.loc[2022]), 'brasil_2012': float(s_br.loc[2012]), 'mundo_2012': float(s_mu.loc[2012]),
                     'brasil_1990': float(s_br.loc[1990]), 'mundo_1990': float(s_mu.loc[1990])}
print({k: round(v, 2) for k, v in R['brasil_mundo'].items()})

# %% Registro dos resultados
with open(RESULT / 'resultados.json', 'w', encoding='utf-8') as f:
    json.dump(R, f, ensure_ascii=False, indent=2, default=float)
print('Gravado: resultados/resultados.json')
