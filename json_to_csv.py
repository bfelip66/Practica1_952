import pandas as pd

df = pd.read_json(r'dades_paginacio.json')
df.to_csv(r'dades_paginacio.csv', index = None)