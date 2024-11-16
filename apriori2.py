# Exercicio 2
import pandas as pd
from mlxtend.frequent_patterns import apriori
from mlxtend.association_rules import association_rules
data = pd.read_csv("data3.csv")
for min_confidence in [0.5, 0.75]:
    frequent_itemsets = apriori(data, min_support=0.5, use_colnames=True)
    rules = association_rules(frequent_itemsets, metric="confidence", min_confidence=min_confidence)
    print(f"Regras para confiança mínima de {min_confidence * 100}%:")
    print(rules)