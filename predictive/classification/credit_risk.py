import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

from config import settings

from icecream import ic

base_credit = pd.read_csv(settings.CREDIT_DATA)

ic('# Visualizando todos os dados ( os 5 primeiros e os 5 últimos)')
ic(base_credit)
print('-' * 100)
ic('# Visualizando os 5 primeiros')
ic(base_credit.head())
print('-' * 100)
ic('# Visualizando os 10 primeiros')
ic(base_credit.head(10))
print('-' * 100)
ic('# Visualizando os 5 últimos')
ic(base_credit.tail())
print('-' * 100)

ic('# Dados estatísticos')
ic(base_credit.describe())
print('-' * 100)

ic('# Obtendo os dados do maior valor de renda')
ic(base_credit[base_credit['income'] >= 69995.685578])
print('-' * 100)

ic('# Obtendo os dados do menor valor de dívida')
ic(base_credit[base_credit['loan'] <= 1.377630])
print('-' * 100)

ic('# Obtendo os valores únicos da coluna default e as quantidades')
ic(np.unique(base_credit['default'], return_counts=True))
print('-' * 100)

### Visualização de Dados

ic(sns.countplot(x = base_credit['default']))
print('-' * 100)