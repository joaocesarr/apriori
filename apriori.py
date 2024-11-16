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
    import pandas as pd

def apriori_simplificado(df, min_support, min_confidence):

    item_counts = df.stack().value_counts(normalize=True)
    frequent_items = item_counts[item_counts >= min_support]
  
    itemsets = list(frequent_items.index)
    combinations = []
    for i in range(len(itemsets)):
        for j in range(i+1, len(itemsets)):
            itemset = frozenset([itemsets[i], itemsets[j]])
            support = df[df.apply(lambda x: all(item in set(x) for item in itemset), axis=1)].shape[0] / df.shape[0]
            confidence = support / frequent_items[itemsets[i]]
            if confidence >= min_confidence:
                combinations.append((itemset, support, confidence))

    frequent_combinations = [itemset for itemset, support, confidence in combinations if confidence >= min_confidence]

    return frequent_combinations

data = {'transacao': [1, 1, 2, 2, 3],
        'itens': [['leite', 'pao'], ['cerveja', 'fritas'], ['leite', 'frutas'], ['cerveja', 'pao'], ['leite']]}
df = pd.DataFrame(data)

rules = apriori_simplificado(df, min_support=0.4, min_confidence=0.6)

for rule in rules:
    print(rule)
