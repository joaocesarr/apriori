#Exercicio 1
import pandas as pd
from apyori import apriori
import pandas as pd
data = pd.read_csv('data2.csv')
data = pd.read_excel('exercicio1_apriori.xlsx', index_col=0)
data = data.T
data = data.values.tolist()
association_rules = apriori(data, min_support=0.2, min_confidence=0.5)
for item in association_rules:
    print(item)